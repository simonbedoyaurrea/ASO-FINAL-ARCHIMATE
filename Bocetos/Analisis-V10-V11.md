# Decisiones vigentes — V10 y V11 · CHANDA

Estado: **implementado y adoptado como base canónica de la rama CHANDA**, 2026-10-15. El modelo editable prevalece sobre los bocetos y las previsualizaciones.

## Fuentes y evidencia

- Enunciado local del proyecto, Tema 4 y requisitos de V10/V11. El documento se conserva privado y no se publica.
- V2 canónica: nombres de capacidades y objetivo de negocio.
- V8 actual: seis contextos y sus servicios, sin tomar como aprobadas las vistas anteriores descartadas.
- [Bounded Context Canvas v5 de DDD Crew](https://github.com/ddd-crew/bounded-context-canvas): referencia de secciones, adaptada bajo CC BY 4.0.

No se dispone de la entrevista íntegra referenciada por la documentación anterior. Las decisiones nuevas no se presentan como afirmaciones de esa entrevista ni como normas verificadas. El equipo conserva la responsabilidad de revisión y sustentación académica.

## Alcance literal usado en la trazabilidad

| Clave visual | Alcance de Tema 4 | Requirement reutilizado |
|---|---|---|
| R1 | Recaudar en los tres modos con VAMOS, débito y crédito | `id-6364f857fddf5beeba44345c1180dab6` |
| R2 | Emitir/recargar VAMOS, consultar saldo y bloquear por pérdida | `id-ca11ad822ab6573db32566d916e0119a` |
| R3 | Tarifa plena y especial para escolares, universitarios, adultos mayores y movilidad reducida, validando condiciones | `id-5ac6b0a263ef54baba36839e5839b215` |
| R4 | Aplicar tarifa correcta considerando integración entre modos | `id-dc8f1c3f82b158d39c5558ebe77520fb` |
| R5 | Consolidar por modo, ruta y operador como base de distribución y conciliación | `id-00d315235aa157aca4bbe201615e7282` |

**G01:** residentes y visitantes pagan de forma ágil y con la tarifa que les corresponde. Se reutiliza `id-63ea7c03c0df5ff48c45324059448cf9`; no se inventa un SLA numérico.

**D1:** decisión derivada de recepción confiable: no duplicar una transacción identificada ni convertir su reenvío en otro viaje. No es una cita literal del enunciado ni exige una cola o un nuevo dominio.

Los rótulos de las vistas son resúmenes. Los nombres completos de los elementos reutilizados permanecen en el modelo.

## V10 — una meta, seis cadenas

Versión de composición: **V10-boceto-03**, 1800 × 950. Una meta compartida, cinco columnas de detalle y seis filas. No se repite seis veces la meta ni se añade una columna de resultados solo por completar la lámina.

Cada componente conserva una cadena formal:

**Goal ← Requirement ← Capability ← BusinessProcess ← ApplicationService ← ApplicationComponent**

| Componente | Requisito | Capacidad de V2 |
|---|---|---|
| Recepción de transacciones | R1 / D1 | Validación y entrada |
| Tarjetas VAMOS y saldos | R2 | Medios de pago |
| Perfiles y descuentos | R3 | Tarifas y descuentos |
| Tarifas y transbordos | R3 / R4 | Tarifas y descuentos |
| Pago con tarjeta del banco | R1 | Medios de pago |
| Consolidación del recaudo | R5 | Consolidación y reparto, únicamente su parte de consolidación |

Relaciones: realización desde requisito a meta, capacidad a requisito, proceso a capacidad y componente a servicio; **Serving** desde servicio de aplicación a proceso de negocio. Las combinaciones se comprobaron con el MCP. No son flechas de secuencia de ejecución.

Se reutilizan las mismas identidades cuando una capacidad, requisito o meta aparece en varias cadenas. Los resúmenes de procesos no introducen nuevos dominios. La vista tiene 31 tarjetas semánticas, dos notas y 30 conexiones visuales.

Los resultados explicativos se mantienen en las capacidades y objetivos: recepción sin duplicados, VAMOS gestionable, beneficios solo con perfil vigente, tarifa/integración correcta, visitantes sin comprar VAMOS y base consolidada disponible. No se modifican por ello los resultados canónicos de V2.

## V11 — canvas de Tarifas y transbordos

Versión de composición: **V11-boceto-04**, 1800 × 970. Trece tarjetas y cuatro conexiones visibles. Se conservan todas las secciones exigidas:

- **Propósito:** calcular la tarifa y la integración aplicables a cada validación.
- **Clasificación:** contexto central de reglas específicas del recaudo integrado.
- **Rol:** especificar/versionar reglas y ejecutar el cálculo. No implica un microservicio.
- **Entradas:** registro de acto/vigencia por el gestor; transacción aceptada desde Recepción.
- **Salidas:** versión publicada a la integración de equipos; validación tarificada para VAMOS/Pago bancario y Consolidación.
- **Lenguaje:** validación, transbordo, perfil vigente y tarifa calculada. Esta última no es la tarifa técnica del operador ni una autorización bancaria.
- **Decisiones:** autoridad define, gestor registra; Perfiles verifica; Tarifas calcula; VAMOS mueve saldo; banco cobra; Consolidación agrupa sin conciliar. Corregir con rastro, sin editar cobros históricos.
- **Supuestos:** identidad estable y vigencia histórica disponibles; valores y ventanas obtenidos de reglas autorizadas.

La consulta no necesita otro carril completo: se explica en una tarjeta con el contrato. Consultar una tarifa devuelve respuesta al solicitante y no genera un consumo o un cobro. Tarifas consulta Perfiles (C/P) y Planeación (C/P + ACL); no absorbe sus datos ni responsabilidades.

### Reglas operacionales cerradas

- La misma entrada y contexto versionado producen el mismo resultado; recalcular no vuelve a cobrar.
- No se inventan importes, porcentajes o ventanas. Son configuración de reglas autorizadas, no decisiones estructurales pendientes.
- Si no hay datos/reglas suficientes, devolver **no tarifable** con causa, no una tarifa arbitraria ni una orden de negar físicamente acceso.
- Los mensajes C/Q/E son comandos, consultas y eventos lógicos; no obligan a implementar un bus de eventos.
- Verificar casos por modo/medio/perfil/transbordo, causas de no tarifables, diferencias con equipos y tiempo de cálculo, sin SLA inventados.
- Fuera: dispositivos, certificación externa, saldos, cobro bancario, conciliación, liquidación y pago a operadores.

### Representación en Archi

El contexto usa su ApplicationComponent existente. Las colaboraciones principales usan ApplicationProcess y ApplicationEvent con relaciones Triggering. Los campos descriptivos del canvas son **notas rectangulares**, no Meaning/Assessment/Constraint inventados para decorar.

Se descartaron las figuras alternativas que dejaban nubes, pergamino o lupa separados del texto. No hay panel blanco de tamaño completo: se conserva el fondo normal de Archi y el blanco se limita a rótulos. V2 permanece intacta; en V8 solo se retiró su fondo blanco.

## Verificación y recuperación

- Los SVG/escenas son generados por `compactar_v10_v11.py`; las mismas escenas se usan para construir las vistas. Se comprueban dimensiones, contenido, tarjetas sin solapamientos y rutas sin atravesar otras tarjetas.
- `implementar_v10_v11.py` modifica solo V10/V11, reutiliza conceptos y conserva las otras vistas. La copia `.bak` es local y no se publica.
- `verificar_v10_v11.py` comprueba las referencias y la preservación de V2 y V8, permitiendo únicamente el retiro autorizado del fondo de V8 respecto del respaldo anterior.
- QA semántico MCP aislado: **34 conceptos, 33 relaciones únicas, cero incidencias**. Son 34 conexiones visuales porque una relación compartida se representa más de una vez.
- El modelo completo carga y sus referencias visuales son válidas. La validación semántica global permanece bloqueada por un elemento heredado sin nombre; no se declara validado el contenido de las versiones descartadas.
- Las imágenes del MCP no reproducen exactamente fuentes y rótulos de Archi. Los PNG de los bocetos son referencias de composición, no capturas de la aplicación.
