"""Verifica fidelidad geométrica y produce un modelo mínimo para QA semántico MCP."""
from pathlib import Path
import xml.etree.ElementTree as E
import copy
import json
import re
from implementar_v10_v11 import ROOT,P,X,uid,digest_view

def main():
    text=P.read_text(); root=E.fromstring(text)
    indexed={n.get('id'):n for n in root.iter() if n.get('id')}
    concepts={}; rels={}; views=[]; report={}
    types={'Realization':0,'Serving':0,'Triggering':0,'Access':0}
    for number in ('V10','V11'):
        v=indexed[uid('view/'+number)]; views.append(copy.deepcopy(v))
        version='04' if number=='V11' else '03'
        scene=json.loads((ROOT/f'Bocetos/{number}-boceto-{version}.scene.json').read_text())
        for i,card in enumerate(scene['cards']):
            n=indexed[uid(f'{number}/card/{i}')]
            b=n.find('bounds'); assert b is not None
            for key in ('x','y','width','height'): assert int(b.attrib[key])==card[key]
            if n.get('archimateElement'):
                label=next(f.get('value') for f in n.findall('feature') if f.get('name')=='labelExpression')
                for word in (card['title']+' '+card['body']).split(): assert word in label
                concepts[n.get('archimateElement')]=copy.deepcopy(indexed[n.get('archimateElement')])
            else:
                content=n.findtext('content') or ''
                for word in (card['title']+' '+card['body']).split(): assert word in content
        assert not any(n.get('id')==uid(number+'/background') for n in v.iter('child'))
        for c in v.iter('sourceConnection'):
            r=indexed[c.get('archimateRelationship')]
            rels[r.get('id')]=copy.deepcopy(r)
            typ=r.attrib[X].split(':')[-1].removesuffix('Relationship'); types[typ]+=1
            assert indexed[c.get('source')].get('archimateElement')==r.get('source')
            assert indexed[c.get('target')].get('archimateElement')==r.get('target')
            if typ=='Access': assert r.get('accessType','0')=='0'
        report[number]={'tarjetas':len(scene['cards']),'geometria_identica_al_boceto':True,'contenido_completo_en_rotulos':True,'sin_panel_blanco_de_fondo':True,'conexiones':len(list(v.iter('sourceConnection')))}
    before=P.with_name('recaudo_tema4.pre-v10-v11.bak').read_text()
    report['V2_identica']=digest_view(before,'V2')==digest_view(text,'V2')
    # Subsequently authorised V8 change: remove only the known empty backdrop.
    before_v8=re.sub(r'  <child\b[^>]*id="id-588cf0c8662e5beabd81ec332a8bd5b8"[^>]*>.*?</child>\n','',before,count=1,flags=re.S)
    report['V8_solo_retiro_de_fondo']=digest_view(before_v8,'V8')==digest_view(text,'V8')
    assert report['V2_identica'] and report['V8_solo_retiro_de_fondo']
    # Include only the two views and the formal concepts/relationships they show.
    # This isolates our change from the unnamed inherited concepts in the full file.
    qa=E.Element(root.tag,dict(root.attrib)); qa.set('name','QA aislado — V10 y V11')
    for category,prefixes in [('application',('Application','DataObject')),('business',('Business',)),('strategy',('Capability',)),('motivation',('Goal','Outcome','Requirement','Meaning','Constraint','Assessment'))]:
        folder=E.SubElement(qa,'folder',{'name':category.title(),'id':uid('qa-'+category),'type':category})
        folder.extend(n for n in concepts.values() if n.attrib[X].split(':')[-1].startswith(prefixes))
    rf=E.SubElement(qa,'folder',{'name':'Relations','id':uid('qa-rels'),'type':'relations'}); rf.extend(rels.values())
    vf=E.SubElement(qa,'folder',{'name':'Views','id':uid('qa-views'),'type':'diagrams'}); vf.extend(views)
    out=ROOT/'modelo/V10-V11-qa.xml'
    E.register_namespace('archimate',root.tag.split('}')[0][1:])
    E.indent(qa,space='  '); E.ElementTree(qa).write(out,encoding='utf-8',xml_declaration=True)
    report['relaciones_visibles']=types
    report['modelo_QA']=str(out)
    (ROOT/'Bocetos/V10-V11-verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
