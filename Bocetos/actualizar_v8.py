"""Genera únicamente V8 en el modelo existente, preservando literalmente V2."""
from pathlib import Path
import xml.etree.ElementTree as E
import hashlib
import uuid
import re

P = Path(__file__).resolve().parents[1] / 'modelo/recaudo_tema4.archimate'
X = '{http://www.w3.org/2001/XMLSchema-instance}type'
E.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
def ident(key):
    return 'id-' + uuid.uuid5(uuid.NAMESPACE_URL, 'aos-v8-final/' + key).hex
def el(parent, tag, **attrs):
    return E.SubElement(parent, tag, attrs)
def typed(parent, tag, kind, **attrs):
    node = el(parent, tag, **attrs); node.set(X, 'archimate:' + kind); return node
FONT = '1|Arial|10.0|0|COCOA|1|ArialMT'
def bounds(n, x, y, w, h):
    el(n, 'bounds', x=str(x), y=str(y), width=str(w), height=str(h))
def note(parent, key, text, x, y, w, h, size=10):
    n = typed(parent, 'child', 'Note', id=ident(key), font=FONT.replace('10.0', str(size)+'.0'), textAlignment='1', fillColor='#ffffff', borderType='2')
    bounds(n,x,y,w,h); el(n,'content').text=text; return n

def main():
    original = P.read_text()
    root = E.fromstring(original)
    elements = {n.get('id'): n for n in root.iter('element')}
    view = E.Element('element', {X:'archimate:ArchimateDiagramModel', 'id':'id-6a83f7520a9a42e4b11e79a1', 'name':'V8 · Mapa de contextos delimitados'})
    # Keep Archi's normal background; white is only used for annotations.
    note(view,'title','V8 · Mapa de contextos — recaudo integrado en buses y metro',48,20,1704,40,16)
    note(view,'subtitle','Tema 4 · Seis contextos internos. Los equipos, la conciliación, liquidación y pago a operadores permanecen externos.',48,70,1704,36)
    note(view,'heading','Aplicación y sistemas con los que intercambia información',48,120,1704,30,12)
    nodes={}; geom={}; incoming={}
    def node(key, eid, rect, external=False, service=None, interface=None):
        assert eid in elements, eid
        n=typed(view,'child','DiagramObject', id=ident(key), archimateElement=eid, font=FONT, fillColor='#ededed' if external else '#f7dfaa', textPosition='0')
        n.set('font',FONT.replace('|10.0|0|','|10.0|1|'))
        bounds(n,*rect); nodes[key]=n; geom[key]=rect; incoming[key]=[]
        if service:
            assert service in elements
            s=typed(n,'child','DiagramObject',id=ident(key+'/service'),archimateElement=service,font=FONT,fillColor='#ffffff')
            bounds(s,16,70,rect[2]-32,44)
        if interface:
            assert interface in elements
            i=typed(n,'child','DiagramObject',id=ident(key+'/interface'),archimateElement=interface,font=FONT,fillColor='#eaf2f8')
            bounds(i,16,124,rect[2]-32,44)
        return n
    node('trx','id-88c37b33bc0d5ff49b14677382db09c2',(48,410,340,194),service='id-8a8918b5aa0c562e9fe171a901effaf6',interface='id-010b131671b25a0c9288f1b4cdc9af1e')
    node('tar','id-fbdd857cfde15f2881d313951803bfef',(488,410,340,194),service='id-2da963bbd32859c799fd40a2c81753e0',interface='id-42c3df845d1f51ac88e8aca15e769f4d')
    node('bank','id-0953ed94b1125f26bf204b6e91f036ae',(928,410,340,194),service='id-f3ccc4a0846c54e2ab02cb6ed31e47ea',interface='id-14151d1cfe1d5912bce9e30f5b0dc9bf')
    node('con','id-61ba9719635454f3801c54958cfc03f1',(1368,410,384,194),service='id-1787478c5a7e54ad9fc2ea9c5ec9837c',interface='id-abed1efd6d02533698f63ba6da50c220')
    node('per','id-3103aa5df4c55dd6a2d73e4b826bd5f4',(48,744,340,194),service='id-ea76c06a118457d592478154bf1a8eda',interface='id-1d50acfefc315e66ab6a1c7a24979f72')
    node('vamos','id-4564e1008063577ba3227a09b07e4f58',(928,744,340,194),service='id-93f1ea5fd26050ce85b2a44021b00eac',interface='id-98f9d1f112435c9faa2a9bec1fd4db95')
    for key,eid,rect in [
        ('devices','id-cc8f72f42d7659d58025432e0ac0de4e',(48,180,340,110)),
        ('authority','id-973c7120092d50889cc1968008ece290',(488,180,340,110)),
        ('acquirer','id-2ab3a37dc65052d79ab360e89c4cc460',(928,180,340,110)),
        ('planning','id-d3466ed2231a5ae5bf8fa8c198f72cc9',(1368,180,384,110)),
        ('cert','id-e25391e531cb5fa0a00fe115a73a8f5b',(488,771,340,140)),
        ('recharge','id-60f045bc23d55f71aa5d0518ba4aa57c',(1368,771,384,140)),
        ('pqrs','id-72bc9af26c1e5503b23799dde9e07d42',(48,1040,340,100)),
        ('erp','id-f983fc45a02556809b0180d1568d20d0',(928,1040,340,100)),
        ('settlement','id-2a429073a0955a51b678cd7890600a09',(1368,1040,384,100)),
        ('metro','id-4cc89b4ba4a755c08d37b8580f5e0bfe',(48,310,340,60)),
    ]: node(key,eid,rect,True)
    extra=[]
    def connect(a,b,label,points=(),rid=None):
        src=nodes[a].get('archimateElement'); dst=nodes[b].get('archimateElement')
        if rid:
            r=elements[rid]; assert r.get('source')==src and r.get('target')==dst
        else:
            rid=ident('relationship/'+a+'/'+b)
            r=E.Element('element',{X:'archimate:FlowRelationship','id':rid,'source':src,'target':dst,'name':label})
            el(r,'documentation').text='Relación explícita de V8; patrón y sentido del intercambio indicado en la etiqueta. No implica operación síncrona.'
            if rid not in elements:
                extra.append(r)
        c=typed(nodes[a],'sourceConnection','Connection',id=ident('connection/'+a+'/'+b),source=nodes[a].get('id'),target=nodes[b].get('id'),archimateRelationship=rid,font=FONT.replace('10.0','9.0'))
        # Short two-line labels stay in the channels between cards.
        pattern,_,caption=label.partition('] ')
        shown=pattern+']\n'+caption if caption else label
        if (a,b) in {('pqrs','trx'),('con','erp'),('con','settlement')}:
            shown=' '
        el(c,'feature',name='labelExpression',value=shown)
        c.set('lineColor','#4a4a4a')
        ax,ay,aw,ah=geom[a]; bx,by,bw,bh=geom[b]
        # Every intermediate segment must be orthogonal and avoid unrelated boxes.
        route=[(ax+aw/2,ay+ah/2),*points,(bx+bw/2,by+bh/2)]
        for (x1,y1),(x2,y2) in zip(route,route[1:]):
            assert x1==x2 or y1==y2, (a,b,'segmento diagonal')
            for key,(rx,ry,rw,rh) in geom.items():
                if key in (a,b):
                    continue
                if x1==x2:
                    hit=rx<x1<rx+rw and max(min(y1,y2),ry)<min(max(y1,y2),ry+rh)
                else:
                    hit=ry<y1<ry+rh and max(min(x1,x2),rx)<min(max(x1,x2),rx+rw)
                assert not hit,(a,b,'atraviesa',key)
        for x,y in points:
            # Archi stores integer relative coordinates (EInt), not decimals.
            el(c,'bendpoint',startX=str(int(x-ax-aw/2)),startY=str(int(y-ay-ah/2)),endX=str(int(x-bx-bw/2)),endY=str(int(y-by-bh/2)))
        incoming[b].append(c.get('id'))
    connect('trx','tar','[C/P] transacción',rid='id-62c7b6469adc5b439517103efc8fb665')
    connect('per','tar','[C/P] perfil',[(438,841),(438,507)],rid='id-4fd85b0f297c5e2f97ba6aa67b88c56d')
    connect('tar','bank','[C/P] tarifa',rid='id-fcc71b75c8415e87b0dcbcfb048697fb')
    connect('bank','con','[C/P] cobro',rid='id-1d65fe718d925b2a9e8fb7dce6eec9c2')
    connect('tar','vamos','[C/P] movimiento',[(658,710),(1098,710)],rid='id-e1871404e119540695e22c539299b010')
    connect('tar','con','[C/P] viaje tarificado',[(868,507),(868,650),(1560,650)],rid='id-ab9c031843b951a7bce25418e737db9f')
    connect('vamos','con','[C/P] recargas',[(1318,841),(1318,685),(1560,685)],rid='id-b2452441eb685f9285cb0d43c3e6279c')
    connect('devices','trx','[ACL] buses',[(414,235),(414,385),(218,385)])
    connect('metro','trx','[ACL] transacciones metro')
    connect('authority','tar','[CF] acto tarifario')
    connect('acquirer','bank','[CF + ACL] resultado')
    connect('planning','con','[C/P + ACL] rutas y operadores')
    connect('cert','per','[CF] evidencia de perfil')
    connect('recharge','vamos','[ACL] recarga')
    connect('pqrs','per','[OHS/PL] consulta de perfil')
    connect('pqrs','trx','[OHS/PL] historial',[(16,1090),(16,507)])
    connect('pqrs','vamos','[OHS/PL] ajuste',[(438,1090),(438,986),(1098,986)])
    connect('con','erp','[PL] resumen',[(1795,507),(1795,990),(1098,990)])
    connect('con','settlement','[PL] base',[(1830,507),(1830,1010),(1560,1010)])
    for key,ids in incoming.items():
        if ids: nodes[key].set('targetConnections',' '.join(ids))
    note(view,'pqrs-history-label','[OHS/PL]\nHistorial de viajes',26,638,140,48,9)
    note(view,'erp-label','[PL]\nResumen contable',1760,816,140,48,9)
    note(view,'settlement-label','[PL]\nBase consolidada',1760,926,140,48,9)
    note(view,'legend','Dorado: contexto interno · Gris: sistema externo. C/P: cliente-proveedor · CF: conformista · ACL: capa anticorrupción · OHS/PL: servicio abierto / lenguaje publicado. Las flechas muestran información, no la secuencia de un proceso.',48,1180,1704,65)
    E.indent(view,space='  ')
    old=next(n for n in root.iter('element') if n.get('id')==view.get('id'))
    # Replace only the known view region. Other views remain byte-for-byte intact.
    match=re.search(r'^    <element[^\n]*name="V8[^\n]*',original,re.M)
    assert match is not None
    start=match.start()
    end=original.index('</element>',start)+len('</element>')
    output=original[:start]+'    '+E.tostring(view,encoding='unicode')+original[end:]
    relations=root.find("folder[@type='relations']")
    anchor='  <folder name="Relations"'
    pos=output.index('>',output.index(anchor))+1
    addition=('\n'+''.join('    '+E.tostring(n,encoding='unicode')+'\n' for n in extra)) if extra else ''
    output=output[:pos]+addition+output[pos:]
    parsed=E.fromstring(output)
    allids=[n.get('id') for n in parsed.iter() if n.get('id')]
    assert len(allids)==len(set(allids)), 'IDs duplicados; no se escribió el archivo'
    indexed={n.get('id'):n for n in parsed.iter() if n.get('id')}
    for c in view.iter('sourceConnection'):
        r=indexed[c.get('archimateRelationship')]
        assert indexed[c.get('source')].get('archimateElement')==r.get('source')
        assert indexed[c.get('target')].get('archimateElement')==r.get('target')
    def v2(text):
        match=re.search(r'name="V2[^"\n]*"',text)
        assert match is not None
        s=match.start()
        e=text.index('\n    </element>',s)
        return hashlib.sha256(text[s:e].encode()).hexdigest()
    assert v2(original)==v2(output)
    P.write_text(output)
    print('V8 generada: 6 contextos, 10 sistemas externos, 19 conexiones. Rutas ortogonales sin atravesar cajas ajenas; V2 idéntica; XML, IDs y extremos verificados.')

if __name__=='__main__': main()
