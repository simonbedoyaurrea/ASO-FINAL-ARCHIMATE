"""Traslada las escenas revisadas a Archi nativo sin reserializar V2 ni V8.

Los rótulos son expresiones visuales; los conceptos reutilizados conservan su
nombre y su identidad. No hay capturas incrustadas ni elementos ficticios de
Grouping usados como notas. La distribución sale del mismo JSON que el SVG.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import json
import uuid
import re
import textwrap
import hashlib

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'modelo/recaudo_tema4.archimate'
X='{http://www.w3.org/2001/XMLSchema-instance}type'
E.register_namespace('xsi','http://www.w3.org/2001/XMLSchema-instance')

def uid(key): return 'id-'+uuid.uuid5(uuid.NAMESPACE_URL,'aos-v10-v11/'+key).hex
def add(parent,tag,**attrs): return E.SubElement(parent,tag,{k:str(v) for k,v in attrs.items()})
def typed(parent,tag,kind,**attrs):
    n=add(parent,tag,**attrs); n.set(X,'archimate:'+kind); return n
def bounds(n,x,y,w,h): add(n,'bounds',x=int(x),y=int(y),width=int(w),height=int(h))
def font(size,bold=False): return f'1|Arial|{size:.1f}|{1 if bold else 0}|COCOA|1|ArialMT'
def view_fragment(text,number):
    m=re.search(r'^\s*<element[^\n]*name="'+number+r'(?: ·| -)[^\n]*',text,re.M)
    if not m: return None
    start=m.start()
    return (start,text.index('</element>',start)+len('</element>'))
def digest_view(text,number):
    span=view_fragment(text,number)
    assert span is not None,number
    a,b=span
    return hashlib.sha256(text[a:b].encode()).hexdigest()

class Model:
    def __init__(self,text):
        self.original=text; self.root=E.fromstring(text)
        self.elements={n.get('id'):n for n in self.root.iter('element')}
        self.created={}; self.newrels={}; self.views=[]; self.geometry=[]
        self.used=set(); self.usedrels=set()
    def concept(self,key,kind,name,doc='',reuse=None):
        if reuse:
            assert reuse in self.elements,(name,reuse)
            assert self.elements[reuse].get(X)=='archimate:'+kind,(name,kind)
            self.used.add(reuse); return reuse
        exact=next((n.get('id') for n in self.elements.values() if n.get(X)=='archimate:'+kind and n.get('name')==name),None)
        if exact:
            self.used.add(exact); return exact
        id=uid('concept/'+key)
        if id not in self.elements:
            n=E.Element('element',{X:'archimate:'+kind,'id':id,'name':name})
            add(n,'documentation').text=doc or name
            add(n,'property',key='Fuente de diseño',value='Bocetos/Analisis-V10-V11.md; Tema 4; revisión V10/V11')
            self.created[id]=n; self.elements[id]=n
        self.used.add(id); return id
    def rel(self,kind,a,b,doc=''):
        exact=next((n.get('id') for n in self.elements.values() if n.get(X)=='archimate:'+kind+'Relationship' and n.get('source')==a and n.get('target')==b),None)
        if exact:
            if kind=='Access' and exact==uid(f'rel/{kind}/{a}/{b}'):
                self.elements[exact].set('accessType','0')
            self.usedrels.add(exact); return exact
        id=uid(f'rel/{kind}/{a}/{b}')
        n=E.Element('element',{X:'archimate:'+kind+'Relationship','id':id,'source':a,'target':b})
        if kind=='Access': n.set('accessType','0') # Archi native default = Write (1 is Read).
        add(n,'documentation').text=doc or 'Relación de la revisión V10/V11. No representa una secuencia de despliegue.'
        self.newrels[id]=n; self.elements[id]=n
        self.usedrels.add(id); return id
    def build(self,number,scene,semantics,linktypes):
        name='V10 · Trazabilidad vertical' if number=='V10' else 'V11 · Canvas de Tarifas y transbordos'
        v=E.Element('element',{X:'archimate:ArchimateDiagramModel','id':uid('view/'+number),'name':name,'viewpoint':'layered'})
        version='04' if number=='V11' else '03'
        add(v,'documentation').text='Versión compacta derivada de '+number+'-boceto-'+version+'.scene.json. Conceptos editables y relaciones formales; no es una imagen incrustada.'
        nodes=[]; incoming={}; index={}
        # No canvas-size white note: keep Archi's normal grey background.
        for i,c in enumerate(scene['cards']):
            if i in semantics:
                eid=semantics[i]
                n=typed(v,'child','DiagramObject',id=uid(f'{number}/card/{i}'),archimateElement=eid,
                        fillColor=c['fill'],font=font(c['size']*.75),textAlignment='1',textPosition='0')
                # Use the default native figure. Alternate icon+label figures
                # are not rectangular cards and can detach text from the symbol.
                # Fixed line breaks match the conservative wrapping used in the sketch.
                parts=[]
                if c['kind']: parts.extend([c['kind'].upper(),''])
                wrap=lambda t,size: '\n'.join('\n'.join(textwrap.wrap(p,width=max(8,int((c['width']-36)/(size*.61))),break_long_words=False)) for p in t.split('\n'))
                parts.append(wrap(c['title'],c['size']+1))
                if c['body']: parts.extend(['',wrap(c['body'],c['size'])])
                label='\n'.join(parts)
                add(n,'feature',name='labelExpression',value=label)
            else:
                n=typed(v,'child','Note',id=uid(f'{number}/card/{i}'),fillColor=c['fill'],font=font(c['size']*.75),textAlignment='1',borderType='2')
                add(n,'content').text=c['title']+'\n\n'+c['body']
            bounds(n,c['x'],c['y'],c['width'],c['height']); nodes.append(n)
            incoming[i]=[]; index[n.get('id')]=i
        for t in scene['texts']:
            # Skip SVG decorative horizontal rule: only textual annotations exist here.
            n=typed(v,'child','Note',id=uid(f"{number}/text/{t['x']}/{t['y']}"),font=font(t['size']*.75,t['bold']),
                    textAlignment='1',fillColor='#ffffff',borderType='2')
            # Headers/footers use the available line, not a font-width guess.
            # This also accommodates the post-implementation footer wording.
            width=t.get('width',scene['width']-t['x']-48)
            bounds(n,t['x'],t['y']-t['size']-4,width,t['size']*1.8)
            content=t['text'].replace('Boceto, no modelo implementado.','Vista implementada; rótulos resumidos sin renombrar elementos.').replace('Boceto previo a Archi.','Canvas implementado con elementos editables.')
            add(n,'content').text=content
        def endpoint(pt):
            x,y=pt
            hits=[i for i,c in enumerate(scene['cards']) if c['x']<=x<=c['x']+c['width'] and c['y']<=y<=c['y']+c['height']]
            assert len(hits)==1,(number,pt,hits)
            return hits[0]
        for i,(link,kind) in enumerate(zip(scene['links'],linktypes)):
            a=endpoint(link['points'][0]); b=endpoint(link['points'][-1])
            assert a in semantics and b in semantics,(number,a,b)
            rid=self.rel(kind,semantics[a],semantics[b],f'{number}: '+scene['cards'][a]['title']+' → '+scene['cards'][b]['title'])
            conn=typed(nodes[a],'sourceConnection','Connection',id=uid(f'{number}/edge/{i}'),source=nodes[a].get('id'),target=nodes[b].get('id'),archimateRelationship=rid,font=font(9),lineColor='#202020')
            ca,cb=scene['cards'][a],scene['cards'][b]
            for px,py in link['points'][1:-1]:
                add(conn,'bendpoint',startX=int(px-ca['x']-ca['width']/2),startY=int(py-ca['y']-ca['height']/2),endX=int(px-cb['x']-cb['width']/2),endY=int(py-cb['y']-cb['height']/2))
            add(conn,'feature',name='labelExpression',value=link.get('label') or ' ')
            incoming[b].append(conn.get('id'))
        for i,ids in incoming.items():
            if ids: nodes[i].set('targetConnections',' '.join(ids))
        assert len(linktypes)==len(scene['links'])
        self.views.append(v)
        self.geometry.append({'view':number,'cards':len(nodes),'connections':len(scene['links']),'rectangles':[(c['x'],c['y'],c['width'],c['height']) for c in scene['cards']]})
        return v
    def write(self):
        text=self.original
        # Remove only our own generated folders/views for repeatable regeneration.
        for category in ('business','application','motivation','relations'):
            id=uid('folder/'+category)
            m=re.search(r'<folder[^>]*id="'+id+r'"[^>]*>',text)
            if m:
                end=text.index('</folder>',m.start())+len('</folder>')
                text=text[:m.start()]+text[end:]
        for number in ('V10','V11'):
            span=view_fragment(text,number)
            if span: text=text[:span[0]]+text[span[1]:]
        # Include existing own concepts in regenerated folders too.
        mine={uid('folder/'+x) for x in ('business','application','motivation','relations')}
        allnew={**self.created,**self.newrels}
        for folder in self.root.iter('folder'):
            if folder.get('id') in mine:
                for n in folder.findall('element'):
                    if n.get('id') in self.used|self.usedrels:
                        allnew.setdefault(n.get('id'),n)
        buckets={'business':[],'application':[],'motivation':[],'relations':[]}
        for n in allnew.values():
            typ=n.get(X).split(':')[-1]
            bucket='relations' if typ.endswith('Relationship') else ('business' if typ.startswith('Business') else 'application' if typ.startswith('Application') or typ=='DataObject' else 'motivation')
            buckets[bucket].append(n)
        for category,items in buckets.items():
            if not items: continue
            f=E.Element('folder',{'name':'V10–V11 · Trazabilidad y canvas','id':uid('folder/'+category)})
            for item in sorted(items,key=lambda e:e.get('id')): f.append(item)
            E.indent(f,space='  ')
            header=re.search(r'<folder[^>]*type="'+category+r'"[^>]*>',text)
            assert header is not None
            pos=header.end(); text=text[:pos]+'\n'+E.tostring(f,encoding='unicode')+text[pos:]
        # Append to Views without reserializing any other view.
        existing=view_fragment(text,'V8'); assert existing is not None
        pos=existing[1]
        chunks=[]
        for v in self.views:
            E.indent(v,space='  '); chunks.append(E.tostring(v,encoding='unicode'))
        text=text[:pos]+'\n    '+'\n    '.join(chunks)+text[pos:]
        parsed=E.fromstring(text)
        ids=[n.get('id') for n in parsed.iter() if n.get('id')]
        assert len(ids)==len(set(ids)),'IDs duplicados'
        indexed={n.get('id'):n for n in parsed.iter() if n.get('id')}
        for v in self.views:
            for node in v.iter('child'):
                if node.get('archimateElement'): assert node.get('archimateElement') in indexed
            for c in v.iter('sourceConnection'):
                r=indexed[c.get('archimateRelationship')]
                assert indexed[c.get('source')].get('archimateElement')==r.get('source')
                assert indexed[c.get('target')].get('archimateElement')==r.get('target')
        for num in ('V2','V8'): assert digest_view(self.original,num)==digest_view(text,num)
        backup=P.with_name('recaudo_tema4.pre-v10-v11.bak')
        if not backup.exists(): backup.write_text(self.original)
        P.write_text(text)
        report={'views':self.geometry,'V2_preservada':True,'V8_preservada':True,'ids_unicos':True,'referencias_validas':True,'backup':backup.name}
        (ROOT/'Bocetos/V10-V11-integracion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
        print(json.dumps({k:v for k,v in report.items() if k!='views'},ensure_ascii=False))

def main():
    m=Model(P.read_text())
    scene10=json.loads((ROOT/'Bocetos/V10-boceto-03.scene.json').read_text())
    scene11=json.loads((ROOT/'Bocetos/V11-boceto-04.scene.json').read_text())
    goal='id-63ea7c03c0df5ff48c45324059448cf9'
    requirements=['id-6364f857fddf5beeba44345c1180dab6','id-ca11ad822ab6573db32566d916e0119a','id-5ac6b0a263ef54baba36839e5839b215','id-dc8f1c3f82b158d39c5558ebe77520fb','id-6364f857fddf5beeba44345c1180dab6','id-00d315235aa157aca4bbe201615e7282']
    caps=['id-acd893170dbd4168864214d7fbc51865','id-e1e6405a22c8496a84e780a984a510fb','id-4ef9b5cef54c411dbd868b7759aed1d3','id-4ef9b5cef54c411dbd868b7759aed1d3','id-e1e6405a22c8496a84e780a984a510fb','id-3c856e1ba07245ddaae436312aac33f4']
    services=['id-8a8918b5aa0c562e9fe171a901effaf6','id-93f1ea5fd26050ce85b2a44021b00eac','id-ea76c06a118457d592478154bf1a8eda','id-2da963bbd32859c799fd40a2c81753e0','id-f3ccc4a0846c54e2ab02cb6ed31e47ea','id-1787478c5a7e54ad9fc2ea9c5ec9837c']
    components=['id-88c37b33bc0d5ff49b14677382db09c2','id-4564e1008063577ba3227a09b07e4f58','id-3103aa5df4c55dd6a2d73e4b826bd5f4','id-fbdd857cfde15f2881d313951803bfef','id-0953ed94b1125f26bf204b6e91f036ae','id-61ba9719635454f3801c54958cfc03f1']
    mapping={}
    processnames=['Recibir y registrar validaciones','Gestionar la tarjeta VAMOS','Verificar elegibilidad del usuario','Determinar tarifa del viaje','Cobrar el viaje con tarjeta bancaria','Consolidar el recaudo atribuido']
    types=['Requirement','Capability','BusinessProcess','ApplicationService','ApplicationComponent']
    mapping[0]=m.concept('goal','Goal','Pago ágil y tarifa correcta',reuse=goal)
    for row in range(6):
        cards=scene10['cards'][1+row*5:1+row*5+5]
        reused=[requirements[row],caps[row],None,services[row],components[row]]
        for col,(c,old) in enumerate(zip(cards,reused)):
            name=processnames[row] if col==2 else c['title']
            key=f'v10/{row}/4' if col==2 else f'v10/{row}/{col}'
            mapping[1+row*5+col]=m.concept(key,types[col],name,doc='Fila de trazabilidad del componente '+cards[-1]['title']+'. '+c['title'],reuse=old)
    # D1 is a documented derived requirement, not an extra domain.
    d1=m.concept('d1','Requirement','Registrar cada transacción una sola vez y en el día de servicio en que pasó',reuse='id-802d616e654357b1a53b50a747d0314f')
    m.rel('Realization',caps[0],d1,'D1: contribución a recepción confiable, sin atribuirla al enunciado literal.')
    m.rel('Realization',d1,goal,'D1 contribuye a la meta de pago correcto sin duplicados.')
    m.build('V10',scene10,mapping,['Realization','Realization','Realization','Serving','Realization']*6)

    # V11: every semantic card has its correct behavior/passive type.
    # Descriptive canvas sections are diagram-only notes, not invented concepts.
    kinds={0:'ApplicationComponent',1:'ApplicationProcess',2:'ApplicationProcess',3:'ApplicationEvent',4:'ApplicationEvent',5:'ApplicationProcess',6:'ApplicationEvent'}
    names={0:'Contexto Tarifas y transbordos',1:'Registrar versión tarifaria',2:'Versionar las reglas tarifarias',3:'Versión tarifaria publicada',4:'Transacción aceptada',5:'Tarifar validación',6:'Validación tarificada'}
    mapping11={}
    for i,kind in kinds.items():
        c=scene11['cards'][i]
        mapping11[i]=m.concept('v11/'+str(i),kind,names[i],c['title']+'\n'+c['body'],reuse=components[3] if i==0 else None)
    m.build('V11',scene11,mapping11,['Triggering']*4)
    for i in (1,2,5):
        m.rel('Assignment',components[3],mapping11[i],'Responsabilidad del contexto Tarifas y transbordos.')
    m.write()

if __name__=='__main__': main()
