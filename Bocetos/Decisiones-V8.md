# Registro breve — V8: mapa de contextos

**Estado:** diseño implementado y adoptado en la base canónica de la rama `CHANDA`, 2026-10-15. El modelo es la referencia; las V8 anteriores a esta iteración se descartan. V2 conserva su contenido canónico.

## Alcance y decisiones

- Tema 4: buses alimentadores, buses articulados y metro. La aplicación recibe transacciones de sus sistemas de validación; no administra validadores, lectores ni IoT.
- Mapa compacto de seis contextos: **Recepción de transacciones**, **Perfiles**, **Tarifas y transbordos**, **Tarjetas VAMOS y saldos**, **Pago con tarjeta bancaria**, **Consolidación del recaudo**. Los modos de transporte y los cuatro tipos de perfil no son dominios.
- Se separan perfiles de tarifas: las certificadoras aportan evidencia; Perfiles verifica y conserva la elegibilidad y vigencia; Tarifas decide el importe y la integración.
- Se separan VAMOS del pago bancario: saldo/recarga/bloqueo y autorización/cobro bancario tienen ciclos y contrapartes externas distintos.
- Consolidación entrega una base por modo, ruta y operador. Conciliación, liquidación y pago a operadores permanecen externos: el Tema 4 pide una base para esos procesos, no que la aplicación los ejecute.
- Relaciones internas cliente-proveedor: Recepción y Perfiles → Tarifas; Tarifas → VAMOS y Pago bancario; Tarifas → Consolidación (viajes tarificados); VAMOS → Consolidación (recargas separadas); Pago bancario → Consolidación (resultado del cobro).
- Relaciones externas: equipos de validación y canales de recarga (ACL), autoridad y certificadoras (conformista), planeación de rutas (cliente-proveedor + ACL), adquirente/red de pago (conformista + ACL), PQRS (servicio abierto/lenguaje publicado), consumidores financieros de la base consolidada (lenguaje publicado).
- Los actores y sistemas externos no se convierten en dominios de la aplicación.

## Fuente y cautela

Decisión derivada del enunciado del Tema 4, la V2 canónica y las responsabilidades distintas de los flujos descritos. V8 está incorporada en `modelo/recaudo_tema4.archimate`, con seis contextos, servicios, interfaces y relaciones. Se retiró únicamente la nota blanca que cubría todo el fondo: los rótulos blancos, las cajas y las conexiones se conservan. `V8-boceto-04` es una referencia de composición, no una exportación actual de Archi.
