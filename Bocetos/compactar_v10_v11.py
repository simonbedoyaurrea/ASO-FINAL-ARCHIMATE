"""Versión compacta: tamaños cercanos a V2/V8, sin la lámina de 42 tarjetas."""
from generar_v10_v11 import Sheet,OUT,MOT,STR,BUS,APP,GREY

def main():
    s=Sheet(1800,950,'V10 · Trazabilidad de la meta al componente','Tema 4 · Una meta compartida y seis componentes',compact=True)
    s.text(48,375,'Meta común',14,bold=True,width=220)
    s.card(48,400,220,100,'G01 · Pago ágil y tarifa correcta',fill=MOT,size=14)
    widths=[250,230,240,250,250]; xs=[350]
    for w in widths[:-1]: xs.append(xs[-1]+w+45)
    for x,t in zip(xs,['Requerimiento','Capacidad de V2','Proceso de negocio','Servicio de aplicación','Componente de V8']): s.text(x,133,t,13,bold=True)
    rows=[
        ['G01 · Pago ágil y tarifa correcta','R1 / D1 · Recibir los tres modos sin duplicados','Validación y entrada','Recibir y registrar validaciones','Recibir transacciones','Recepción de transacciones'],
        ['G01 · Pago ágil y tarifa correcta','R2 · Emitir, recargar, consultar saldo y bloquear por pérdida','Medios de pago','Gestionar VAMOS','Manejar tarjetas y saldos','Tarjetas VAMOS y saldos'],
        ['G01 · Pago ágil y tarifa correcta','R3 · Verificar los cuatro perfiles especiales','Tarifas y descuentos','Verificar elegibilidad','Manejar perfiles','Perfiles y descuentos'],
        ['G01 · Pago ágil y tarifa correcta','R3 / R4 · Aplicar tarifa e integración entre modos','Tarifas y descuentos','Determinar tarifa del viaje','Calcular la tarifa de los viajes','Tarifas y transbordos'],
        ['G01 · Pago ágil y tarifa correcta','R1 · Pagar con débito y crédito sin adquirir VAMOS','Medios de pago','Cobrar con tarjeta bancaria','Cobrar viajes a la tarjeta del banco','Pago con tarjeta del banco'],
        ['G01 · Pago ágil y tarifa correcta','R5 · Consolidar por modo, ruta y operador','Consolidación y reparto (solo consolidar)','Consolidar el recaudo','Consolidar y entregar la base','Consolidación del recaudo'],
    ]
    for i,row in enumerate(rows):
        y=160+i*105
        for x,w,t,fill in zip(xs,widths,row[1:],[MOT,STR,BUS,APP,STR]): s.card(x,y,w,90,t,fill=fill,size=14)
        s.line([(350,y+45),(320,y+45),(285,450),(268,450)],'r')
        for j in range(4): s.line([(xs[j+1],y+45),(xs[j]+widths[j],y+45)],'s' if j==2 else 'r')
    s.card(48,825,840,90,'Lectura','Discontinua: realiza. Continua: sirve al proceso. Las seis cadenas llegan a la misma meta; no representan pasos de ejecución.',GREY,12)
    s.card(912,825,840,90,'Alcance','R1–R5: Tema 4. D1: no duplicar transacciones. Se consolida la base; conciliar, liquidar y pagar operadores queda fuera.',GREY,12)
    s.text(48,935,'Capacidades de V2 y componentes de V8 reutilizados. El detalle de resultados y decisiones permanece documentado.',11)
    s.save('V10-boceto-03')

    s=Sheet(1800,970,'V11 · Canvas — Tarifas y transbordos','Tema 4 · Un contexto principal en una página',compact=True)
    s.card(48,120,1704,90,'Propósito · clasificación · rol','Calcular tarifa e integración por validación. Contexto central: versiona reglas y calcula importes. Perfiles, saldos y cobros pertenecen a otros contextos.',STR,14)
    for x,t in [(48,'Entradas'),(632,'Dentro de Tarifas y transbordos'),(1216,'Salidas')]: s.text(x,245,t,14,bold=True)
    lanes=[
        ('Ente gestor','C · Registrar acto y vigencia. La autoridad define; el gestor registra.','Versionar reglas','Conservar tarifas y reglas de integración versionadas.','Equipos externos','E · Versión vigente a equipos mediante ACL; no administrar hardware.'),
        ('Recepción','E · Validación: ID, instante, modo, medio y viaje. C/P.','Calcular tarifa','C · Calcular importe con regla, perfil e integración vigentes.','VAMOS / Banco / Consolidación','E · Tarifa a VAMOS/banco y Consolidación. No concilia. C/P.'),
    ]
    for i,(a,b,c,d,e,f) in enumerate(lanes):
        y=270+110*i
        s.card(48,y,520,98,a,b,GREY,13)
        s.card(632,y,520,98,c,d,STR,13)
        s.card(1216,y,536,98,e,f,APP,13)
        s.line([(568,y+49),(632,y+49)])
        s.line([(1152,y+49),(1216,y+49)])
    s.card(48,505,1704,90,'Consultas y contrato','Consulta tarifa/regla: responde al solicitante, sin cobrar. Consulta Perfiles (C/P) y Planeación (C/P + ACL). Entrada: validación y contexto. Salida: importe, regla, versión y estado. Recalcular no vuelve a cobrar.',APP,12)
    s.card(48,620,552,170,'Lenguaje ubicuo','Validación: acceso registrado.\nTransbordo: continuación integrada por una regla.\nPerfil vigente: elegibilidad en el instante del viaje.\nTarifa: importe central, no tarifa técnica del operador.',BUS,13)
    s.card(624,620,552,170,'Decisiones de negocio','Autoridad define; gestor registra.\nPerfiles valida; Tarifas calcula.\nVAMOS mueve saldo; banco cobra.\nConsolidación agrupa, no concilia.\nCorregir con rastro, sin editar cobros históricos.',STR,13)
    s.card(1200,620,552,170,'Supuestos y configuración','ID estable y vigencia histórica disponibles. Importes y ventanas vienen de reglas autorizadas. Sin datos suficientes: «no tarifable», con causa.',GREY,13)
    s.card(48,815,840,90,'Verificación','Exactitud por modo, medio, perfil y transbordo; causas de no tarifables; diferencias con equipos; tiempo de cálculo.',APP,12)
    s.card(912,815,840,90,'Límites','Fuera: dispositivos, certificación externa, saldos, cobro bancario, conciliación y pago a operadores.',GREY,12)
    s.text(48,930,'C: comando · Q: consulta · E: evento. Las flechas son colaboraciones lógicas; no requieren un bus de mensajes.',11)
    s.text(48,951,'Adaptación de DDD Crew · Bounded Context Canvas v5 · CC BY 4.0 · Detalle: Analisis-V10-V11.md',10)
    s.save('V11-boceto-04')
    print('V10 03 y V11 04: fondo gris, una meta compartida y canvas simplificado.')

if __name__=='__main__': main()
