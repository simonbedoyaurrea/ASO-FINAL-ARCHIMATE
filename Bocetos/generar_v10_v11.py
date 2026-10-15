"""Bocetos reproducibles. No lee ni modifica el modelo ArchiMate."""
from pathlib import Path
from html import escape
import textwrap
import json

OUT=Path(__file__).resolve().parent
MOT='#ded8f4'; STR='#f7dfaa'; BUS='#fff0c7'; APP='#dceef3'; GREY='#edf0f2'

class Sheet:
    def __init__(self,w,h,title,subtitle,compact=False):
        self.w,self.h=w,h; self.parts=[]; self.cards=[]; self.routes=[]
        self.scene={'width':w,'height':h,'title':title,'cards':[],'texts':[],'links':[]}
        self.in_card=False
        self.compact=compact
        pagew,pageh=(420,round(420*h/w,2)) if compact else (594,420)
        self.parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{pagew}mm" height="{pageh}mm" viewBox="0 0 {w} {h}"><defs>
<marker id="r" markerWidth="11" markerHeight="10" refX="10" refY="5" orient="auto"><path d="M1 1L10 5L1 9Z" fill="white" stroke="#202020" stroke-width="1.2"/></marker>
<marker id="s" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M1 1L9 4L1 7" fill="none" stroke="#202020" stroke-width="1.5"/></marker>
<marker id="f" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0L9 4L0 8Z" fill="#202020"/></marker>
</defs><rect width="{w}" height="{h}" fill="{'#707070' if compact else 'white'}"/>''')
        self.text(48,42 if compact else 65,title,24 if compact else 34,bold=True)
        self.text(48,71 if compact else 103,subtitle,14 if compact else 19,color='#525d64')
        self.parts.append(f'<line x1="48" y1="{92 if compact else 125}" x2="{w-48}" y2="{92 if compact else 125}" stroke="#c9cdd0"/>')
    def text(self,x,y,t,size=18,bold=False,color='#283239',anchor='start',width=None):
        if not self.in_card:
            spec=dict(x=x,y=y,text=t,size=size,bold=bold,color=color,anchor=anchor)
            if width is not None: spec['width']=width
            self.scene['texts'].append(spec)
            if self.compact:
                boxw=width if width is not None else self.w-x-48
                self.parts.append(f'<rect x="{x-4}" y="{y-size-4}" width="{boxw}" height="{size*1.8}" fill="white"/>')
        self.parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}">{escape(t)}</text>')
    def para(self,x,y,w,t,size=18,leading=None):
        leading=leading or size*1.42
        lines=[]
        # Conservative wrapping keeps even long Spanish labels inside their card.
        for p in t.split('\n'):
            lines.extend(textwrap.wrap(p,width=max(8,int(w/(size*.61))),break_long_words=False) or [''])
        for i,line in enumerate(lines): self.text(x,y+i*leading,line,size)
        return y+len(lines)*leading
    def card(self,x,y,w,h,title,body='',fill='#fff',size=18,kind=None):
        self.scene['cards'].append(dict(x=x,y=y,width=w,height=h,title=title,body=body,fill=fill,size=size,kind=kind))
        self.in_card=True
        self.cards.append((x,y,w,h,title))
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="#a2a9ac" stroke-width="1.3"/>')
        ty=y+(24 if self.compact else 31)
        if kind:
            self.text(x+18,ty,kind.upper(),12,color='#596870'); ty+=29
        end=self.para(x+18,ty,w-36,title,size+1,leading=(size+1)*1.35)
        if body:
            self.parts.append(f'<line x1="{x+18}" y1="{end+4}" x2="{x+w-18}" y2="{end+4}" stroke="#a2a9ac" stroke-opacity=".5"/>')
        if body:
            end=self.para(x+18,end+(18 if self.compact else 33),w-36,body,size)
        last_baseline=end-(size*1.42 if body else (size+1)*1.35)
        assert last_baseline <= y+h-12,(title,'texto no cabe',last_baseline,y+h)
        self.in_card=False
        return (x,y,w,h)
    def line(self,pts,typ='f',label=None,labelpos=None):
        self.scene['links'].append(dict(points=pts,type=typ,label=label,labelpos=labelpos))
        self.routes.append(pts)
        path='M'+' L'.join(f'{x},{y}' for x,y in pts)
        self.parts.append(f'<path d="{path}" fill="none" stroke="#202020" stroke-width="2" {"stroke-dasharray=\"6 4\"" if typ=="r" else ""} marker-end="url(#{typ})"/>')
        if label:
            assert labelpos is not None
            x,y=labelpos; width=len(label)*7+12
            self.parts.append(f'<rect x="{x-width/2}" y="{y-19}" width="{width}" height="27" rx="4" fill="white"/>')
            self.in_card=True  # Stored as a connection label, not a second floating note.
            self.text(x,y,label,13,anchor='middle')
            self.in_card=False
    def save(self,name):
        for route in self.routes:
            for (x1,y1),(x2,y2) in zip(route,route[1:]):
                for x,y,w,h,title in self.cards:
                    lo,hi=0.0,1.0
                    hit=True
                    for p,d,low,high in ((x1,x2-x1,x+1e-6,x+w-1e-6),(y1,y2-y1,y+1e-6,y+h-1e-6)):
                        if d==0:
                            if not low<=p<=high: hit=False; break
                        else:
                            a,b=sorted(((low-p)/d,(high-p)/d))
                            lo=max(lo,a); hi=min(hi,b)
                            if lo>hi: hit=False; break
                    assert not hit,('flecha atraviesa tarjeta',title)
        for i,a in enumerate(self.cards):
            for b in self.cards[i+1:]:
                assert not(a[0]<b[0]+b[2] and b[0]<a[0]+a[2] and a[1]<b[1]+b[3] and b[1]<a[1]+a[3]),('cajas solapadas',a[4],b[4])
        (OUT/(name+'.svg')).write_text(''.join(self.parts)+'</svg>')
        (OUT/(name+'.scene.json')).write_text(json.dumps(self.scene,ensure_ascii=False,indent=2))

def v10():
    s=Sheet(2700,1909,'V10 · De la meta a los seis componentes','Tema 4 · Trazabilidad vertical · Cada fila es una justificación completa, no una secuencia de ejecución')
    s.para(48,164,2580,'Meta G01 (Tema 4): residentes y visitantes pagan su viaje de forma ágil y con la tarifa que les corresponde.',21)
    widths=[240,310,320,280,300,310,350]; gap=65
    xs=[48]
    for width in widths[:-1]: xs.append(xs[-1]+width+gap)
    headers=['META','RESULTADO','REQUERIMIENTO','CAPACIDAD · V2','PROCESO DE NEGOCIO','SERVICIO DE APLICACIÓN','COMPONENTE · V8']
    for x,w,title in zip(xs,widths,headers):
        s.text(x+8,238,title,15,bold=True)
    rows=[
        ['G01 · Pago ágil y tarifa correcta','Transacciones de los tres modos recibidas sin repetir','R1 + D1\nRecibir transacciones de los tres modos una sola vez','Validación y entrada','Recibir y registrar validaciones','Recibir transacciones','Recepción de transacciones'],
        ['G01 · Pago ágil y tarifa correcta','VAMOS emitida, recargable, consultable y bloqueable','R2\nEmitir, recargar, consultar saldo y bloquear por pérdida','Medios de pago','Gestionar la tarjeta VAMOS','Manejar tarjetas y saldos','Tarjetas VAMOS y saldos'],
        ['G01 · Pago ágil y tarifa correcta','Descuento solo con perfil certificado y vigente','R3\nValidar condiciones de los cuatro perfiles especiales','Tarifas y descuentos','Verificar elegibilidad del usuario','Manejar perfiles','Perfiles y descuentos'],
        ['G01 · Pago ágil y tarifa correcta','Cada validación tiene la tarifa y el transbordo vigentes','R3 + R4\nAplicar tarifa plena o especial e integración entre modos','Tarifas y descuentos','Determinar tarifa del viaje','Calcular la tarifa de los viajes','Tarifas y transbordos'],
        ['G01 · Pago ágil y tarifa correcta','Visitantes viajan sin comprar una tarjeta VAMOS','R1\nPermitir pagar con débito y crédito en los tres modos','Medios de pago','Cobrar el viaje con tarjeta bancaria','Cobrar viajes a la tarjeta del banco','Pago con tarjeta del banco'],
        ['G01 · Pago ágil y tarifa correcta','Base por modo, ruta y operador lista para otros procesos','R5\nConsolidar como base de distribución y conciliación','Consolidación y reparto\n(solo consolidación)','Consolidar el recaudo atribuido','Consolidar y entregar la base de distribución','Consolidación del recaudo'],
    ]
    fills=[MOT,MOT,MOT,STR,BUS,APP,APP]
    for rowi,row in enumerate(rows):
        y=282+rowi*210
        for coli,(x,w,t,fill) in enumerate(zip(xs,widths,row,fills)):
            s.card(x,y,w,180,t,fill=fill,size=17,kind=['Goal','Outcome','Requirement','Capability','BusinessProcess','ApplicationService','ApplicationComponent'][coli])
        for j in range(6):
            # Realization goes from concrete (right) to abstract (left).
            typ='s' if j==4 else 'r'
            s.line([(xs[j+1],y+92),(xs[j]+widths[j],y+92)],typ,
                   'sirve' if typ=='s' else 'realiza',((xs[j+1]+xs[j]+widths[j])/2,y+74))
    s.card(48,1575,800,210,'Cobertura cerrada del alcance','R1: tres modos y tres medios. R2: ciclo VAMOS. R3: plena y cuatro perfiles. R4: transbordos. R5: consolidación. Los seis componentes tienen ruta hasta G01.',GREY,18)
    s.card(878,1575,800,210,'Decisión mínima D1 · recepción confiable','D1 deriva del alcance: una transacción repetida no debe duplicar un viaje. No crea otro dominio ni exige colas, microservicios o infraestructura adicional.',GREY,18)
    s.card(1708,1575,944,210,'Cómo se leerá en ArchiMate','Izquierda → derecha: por qué existe cada componente. Flechas ←: el elemento concreto realiza al más abstracto; el servicio de aplicación sirve al proceso. No todo es «realización».',GREY,18)
    s.text(48,1845,'Reutiliza nombres de V2 y V8. Textos resumidos; requisitos literales y correspondencias en Analisis-V10-V11.md. Boceto, no modelo implementado.',17)
    s.save('V10-boceto-01')
    return rows

def v11():
    s=Sheet(2400,1697,'V11 · Bounded Context Canvas — Tarifas y transbordos','Tema 4 · Un contexto principal, una página · Adaptación del Bounded Context Canvas v5 de DDD Crew')
    s.card(48,154,1040,192,'Propósito','Determinar la tarifa correcta de cada validación según versión tarifaria, medio, perfil vigente e integración entre modos. El ente gestor mantiene reglas; el contexto no autoriza tarifas ni cobra al banco.',STR,19)
    s.card(1112,154,608,192,'Clasificación estratégica','Central: materializa la regla diferenciadora del Tema 4. Apoya el ingreso y el cumplimiento tarifario. Diseño a la medida; no es un nuevo sistema de pagos.',MOT,18)
    s.card(1744,154,608,192,'Rol del dominio','Especificación: versiones de tarifas y reglas. Ejecución: cálculo verificable por validación. Un componente lógico; no exige un microservicio.',APP,18)

    s.text(48,387,'COMUNICACIÓN ENTRANTE',17,bold=True)
    s.text(850,387,'DECISIONES DENTRO DEL CONTEXTO',17,bold=True)
    s.text(1648,387,'COMUNICACIÓN SALIENTE',17,bold=True)
    # Three aligned lanes preserve every arrow without crossing card interiors.
    lanes=[
        ('Ente gestor (acto de la autoridad)','C · Registrar versión tarifaria con acto y vigencia. CF con la autoridad.','Versionar las reglas','Guardar tarifa plena, reglas de perfil e integración; validar que la versión sea aplicable.','Equipos de validación (externos)','E · Versión tarifaria publicada, a través de la integración ACL. No administrar el equipo.'),
        ('Recepción de transacciones','E · Transacción aceptada: identificador, instante, modo, medio y referencias del viaje. C/P.','Calcular la tarifa correcta','C · Tarifar validación. Usar versión y perfil vigentes en el instante del viaje; reconocer transbordo.','VAMOS / Pago bancario / Consolidación','E · Validación tarificada: importe y versión. VAMOS mueve saldo; banco cobra; Consolidación atribuye sin conciliar. C/P.'),
        ('Consumidor de la aplicación','Q · Consultar tarifa o regla vigente. Una consulta no cambia saldo ni registra un cobro.','Responder con trazabilidad','Devolver valor y regla aplicada. Si faltan datos o una regla inequívoca, devolver «no tarifable»; no inventar importe.','Consumidor solicitante','Respuesta a Q: tarifa y versión vigente, o estado «no tarifable» con causa. Responder no emite un cobro ni un evento de consumo.'),
    ]
    for i,(it,ib,ct,cb,ot,ob) in enumerate(lanes):
        y=409+i*183
        s.card(48,y,704,160,it,ib,GREY,17)
        s.card(850,y,700,160,ct,cb,STR,17)
        s.card(1648,y,704,160,ot,ob,APP,17)
        s.line([(752,y+80),(850,y+80)])
        s.line([(1550,y+80),(1648,y+80)])
    # Calls initiated here belong in outbound communication (not additional inbound lanes).
    s.card(48,976,1138,152,'Consultas salientes necesarias · sin nuevos contextos','Tarifas → Perfiles: vigencia/elegibilidad en el instante del viaje (Q, C/P). Tarifas → Planeación: referencia de modo/ruta/calendario (Q, C/P + ACL). Las respuestas regresan al mismo contexto; no son nuevas órdenes ni cobros.',GREY,17)
    s.card(1210,976,1142,152,'Contrato mínimo de cálculo','Entrada: ID de transacción, instante, modo y medio; perfil e integración disponibles. Salida: ID, importe, versión, regla y estado. La misma entrada con la misma versión produce el mismo resultado; volver a calcular no vuelve a cobrar.',APP,17)
    s.card(48,1146,740,286,'Lenguaje ubicuo','Validación: acceso registrado por un equipo.\nTransbordo: continuación que una regla integra.\nPerfil vigente: elegibilidad válida en el instante del viaje.\nTarifa calculada: importe central con versión. No es tarifa técnica del operador ni autorización bancaria.',BUS,17)
    s.card(812,1146,740,286,'Decisiones de negocio','1. La autoridad define; el ente gestor registra.\n2. Los cuatro perfiles se verifican en Perfiles.\n3. Los tres modos usan reglas de integración.\n4. VAMOS y banco ejecutan el movimiento/cobro.\n5. No editar un cobro histórico: recalcular con rastro y emitir la corrección autorizada al dueño.',STR,17)
    s.card(1576,1146,776,286,'Supuestos explícitos y configuración','No se inventan importes, ventanas de transbordo ni porcentajes. Se cargan del acto/regla autorizada. Se supone que Recepción identifica la validación y que Perfiles conserva vigencias. Si no es posible decidir, se informa «no tarifable» y se conserva la causa: no se aplica una tarifa arbitraria.',GREY,17)
    s.card(48,1456,1138,152,'Métricas de verificación','Casos de tarifa correcta por modo/medio/perfil; proporción de validaciones no tarifables y su causa; diferencias con la tarifa aplicada por el equipo; tiempo de cálculo. Son criterios de prueba/observación, no SLA inventados.',APP,17)
    s.card(1210,1456,1142,152,'Cierre de diseño y límites','Sin decisiones estructurales abiertas en este boceto. Los valores oficiales son configuración de negocio, no huecos de arquitectura. Fuera: hardware/IoT, certificación externa, saldo VAMOS, cobro bancario, conciliación y pago a operadores.',GREY,17)
    s.text(48,1641,'C = comando · Q = consulta · E = evento. «Evento» no obliga a usar un bus de mensajes. Flechas: colaboración lógica, no despliegue.',16)
    s.text(48,1670,'Fuente de la plantilla: github.com/ddd-crew/bounded-context-canvas · CC BY 4.0 · Adaptación gráfica y textos del proyecto. Boceto previo a Archi.',15)
    s.save('V11-boceto-01')

if __name__=='__main__':
    rows=v10(); v11()
    (OUT/'V10-cobertura.json').write_text(json.dumps({'contextos':6,'requisitos_tema4':['R1','R2','R3','R4','R5'],'decision_derivada':'D1','filas':rows},ensure_ascii=False,indent=2))
    print('V10 y V11 generadas: texto dentro de tarjetas y sin tarjetas solapadas. ArchiMate no modificado.')
