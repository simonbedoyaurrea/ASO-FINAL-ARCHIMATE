# Recaudo del sistema integrado de transporte de una ciudad mediana

**Proyecto:** «Diseño de la arquitectura de una aplicación empresarial con ArchiMate y DDD», Tema 4. Arquitectura de Software, UPB.

> **Modelo único y definitivo:** [`modelo/recaudo_tema4.archimate`](modelo/recaudo_tema4.archimate). Se abre en Archi 5.x; sus once vistas V1–V11 están directamente en la carpeta *Views*, sin subcarpetas.
> Integra todas las fases: 799 elementos, 1474 relaciones y 11 vistas.
> Las carpetas `fase 1/` y `fase 2/` son **antecedentes** (borradores anteriores) y no forman parte de la entrega.

## Índice

0. [Cómo está organizada la entrega](#0-cómo-está-organizada-la-entrega)
1. [Contexto y entrevista](#1-contexto-y-entrevista)
2. [Motivación](#2-motivación) · [V1](#v1-por-qué-existe-la-aplicación-de-los-interesados-a-los-requerimientos)
3. [Mapa de capacidades y proceso E2E](#3-mapa-de-capacidades-y-proceso-e2e) · [V2](#v2-mapa-de-capacidades-del-negocio) · [V3](#v3-cadena-de-valor-proceso-e2e-y-dónde-se-ubica-la-aplicación)
4. [Descomposición de servicios](#4-descomposición-de-servicios) · [V4](#v4-seis-capas-qué-entra-y-qué-no-contratos-y-quién-presta-los-servicios)
5. [Dominios y lenguaje ubicuo](#5-dominios-y-lenguaje-ubicuo) · [V5](#v5-dominios-y-su-clasificación) · [V7](#v7-lenguaje-ubicuo)
6. [Agregados, comandos y eventos](#6-agregados-comandos-y-eventos) · [V6](#v6-un-diagrama-por-dominio-en-una-sola-vista)
7. [Mapa de contextos e interoperabilidad](#7-mapa-de-contextos-e-interoperabilidad) · [V8](#v8-mapa-de-contextos-delimitados) · [V9](#v9-interoperabilidad-y-anticorrupción)
8. [Bounded Context Canvas](#8-bounded-context-canvas) · [V11](#v11-canvas-del-contexto-tarifas-y-transbordos)
9. [Trazabilidad vertical](#9-trazabilidad-vertical) · [V10](#v10-de-la-meta-al-componente)
10. [Decisiones y supuestos](#10-decisiones-y-supuestos)
11. [Validación, fuentes y limitaciones](#11-validación-fuentes-y-limitaciones)
12. [Tabla de aportes](#12-tabla-de-aportes)

**Acceso directo a las vistas:** [V1](#v1-por-qué-existe-la-aplicación-de-los-interesados-a-los-requerimientos) · [V2](#v2-mapa-de-capacidades-del-negocio) · [V3](#v3-cadena-de-valor-proceso-e2e-y-dónde-se-ubica-la-aplicación) · [V4](#v4-seis-capas-qué-entra-y-qué-no-contratos-y-quién-presta-los-servicios) · [V5](#v5-dominios-y-su-clasificación) · [V6](#v6-un-diagrama-por-dominio-en-una-sola-vista) · [V7](#v7-lenguaje-ubicuo) · [V8](#v8-mapa-de-contextos-delimitados) · [V9](#v9-interoperabilidad-y-anticorrupción) · [V10](#v10-de-la-meta-al-componente) · [V11](#v11-canvas-del-contexto-tarifas-y-transbordos)

---

## 0. Cómo está organizada la entrega

| Ruta | Contenido |
|---|---|
| [`modelo/recaudo_tema4.archimate`](modelo/recaudo_tema4.archimate) | Modelo ArchiMate único y definitivo (Archi 5.x, ArchiMate 3.2) |
| [`vistas/`](vistas/) | Las 11 vistas exportadas por Archi en formato SVG |
| [`entrevista/`](entrevista/) | [Conversación íntegra](entrevista/conversacion_fase0_completa.txt), [instrucción de rol](entrevista/instruccion_de_rol.md), [guion](entrevista/guion.md), [análisis de hallazgos](entrevista/analisis_hallazgos.md), [índice de referencias](entrevista/indice_referencias.md) y el Word original con capturas |
| [`docs/final/`](docs/final/) | Documentos completos: [inclusión y exclusión](docs/final/inclusion_exclusion.md), [anticorrupción](docs/final/anticorrupcion.md), [contratos](docs/final/contratos_servicios.md), [dominios](docs/final/dominios.md), [lenguaje ubicuo](docs/final/lenguaje_ubicuo.md), [agregados e invariantes](docs/final/agregados.md), [contextos y patrones](docs/final/contextos.md), [trazabilidad](docs/final/trazabilidad.md), [decisiones y supuestos](docs/final/decisiones_y_supuestos.md) y [validación](docs/final/validacion.md) |
| [`herramientas/`](herramientas/) | Catálogo de datos y scripts que generan el modelo, las tablas y los contratos, exportan las vistas y validan el modelo (ver §11) |
| [Enunciado](enunciado/Proyecto_Diseño_Arquitectura_ArchiMate%20(1).docx), [resumen del enunciado](docs/contexto/01_enunciado.md), [Tema 4 literal](docs/contexto/02_tema4_recaudo.md), [`diapositivas/`](diapositivas/), [mapa antecedente](mapa_capacidades_recaudo.pdf) y [Word de evidencia de la entrevista](entrevista/capturas_y_tabla_del_equipo_El_pago_integrado_se_divide_por_reglas.docx) | Fuentes académicas, evidencia y antecedentes disponibles en esta copia |
| `fase 1/`, `fase 2/`, `docs/fase0`, `docs/fase1` | Antecedentes de trabajo anteriores (sin cambios) |

**Cómo se citan las fuentes:** «T4» es el Tema 4 del enunciado. «B3.1» es el bloque 3, sección 1 de la entrevista, y cada referencia indica sus líneas en la conversación (por ejemplo, «Entrevista B3.1 (l. 198-210)»). «D-04» y «S-03» son decisiones y supuestos de [decisiones_y_supuestos.md](docs/final/decisiones_y_supuestos.md). Los elementos que representan hechos, supuestos o decisiones documentan su procedencia en la propiedad «Fuente»; los elementos puramente estructurales o de diagramación pueden no llevarla.

**Organización de las vistas (D-30).** El modelo tiene **exactamente once vistas, V1 a V11**, directamente en la carpeta *Views* de Archi y en ese orden. La V6 es una sola vista con **un diagrama independiente por dominio**: once bloques titulados, que se pueden mover y ampliar por separado y de los que no sale ninguna línea. El enunciado pide «un diagrama por dominio», no una vista por dominio. Las tablas, las especificaciones completas y los ejemplos están en `docs/final/`.

| Vista | Qué muestra |
|---|---|
| V1 Motivación | Interesados, impulsores, evaluaciones, metas, resultados, cursos de acción, requerimientos, principios y restricciones |
| V2 Capacidades | El mapa completo del negocio, el impacto de la aplicación y los recursos dentro de su capacidad |
| V3 Cadena de valor y E2E | La cadena de valor, el proceso por carriles con los recorridos de VAMOS y de tarjeta bancaria, y debajo de cada paso el servicio de la aplicación que lo apoya |
| V4 Servicios | Las seis capas, lo que entra y lo que no, el contrato de cada servicio de dominio, y quién presta los servicios con qué información |
| V5 Dominios | Los once dominios por clasificación, con sus objetos y su contexto |
| V6 Agregados | Once diagramas, uno por dominio, con raíz, límite, comandos, eventos, políticas e invariantes |
| V7 Lenguaje ubicuo | El glosario por contexto, con definición y ejemplo, y las palabras con varios significados |
| V8 Mapa de contextos | Los contextos con su responsabilidad, su API y sus servicios, y los patrones de relación |
| V9 Interoperabilidad | Cada intercambio externo con su dirección, la interfaz, el traductor, el servicio anticorrupción de la Fase 2 y su contrato |
| V10 Trazabilidad | De la meta al componente, con relaciones visibles, para los 11 contextos |
| V11 Canvas | El contexto principal, Tarifas y transbordos |

**Recorrido sugerido para la sustentación (30 minutos):**
1. V1 y V2: por qué existe la aplicación, qué debe cumplir y dónde actúa (5 min).
2. V3: el proceso, sus dos recorridos y dónde está la aplicación (4 min).
3. V4: las capas, lo que entra y lo que no, los contratos y quién presta los servicios (5 min).
4. V5 y V7: dominios y lenguaje (4 min).
5. V6: los dos diagramas de los dominios centrales; los otros se amplían si lo preguntan (4 min).
6. V8, V9 y V11: contextos, intercambios externos y canvas (6 min).
7. V10: trazabilidad de la meta al componente (2 min).

**Nombres en lenguaje cotidiano.** Las cajas y los textos de las vistas usan palabras sencillas («cuadrar la plata» en vez de «conciliar», «tarjeta del banco» en vez de «tarjeta bancaria de pago abierto»). El nombre técnico anterior de cada elemento no se perdió: está en su propiedad «Nombre técnico» dentro del modelo. Quedan con su redacción original los textos que vienen literalmente del Tema 4 (GOL01 y REQ01 a REQ05), los términos del glosario, porque son las palabras del negocio y deben ser las mismas en todo el modelo, y los conceptos del curso (agregado, contexto, dominio, capas de servicio, Contract First, canvas), que en cada vista van acompañados de una explicación corta.

**Frontera de la aplicación (D-01, D-04, D-05, D-06).** La aplicación es la plataforma central de recaudo del ente gestor. **Dentro:** medios VAMOS, perfiles, reglas tarifarias, recepción y recálculo de transacciones, cobro agrupado al pasajero con tarjeta bancaria y consolidación por día de servicio, modo, ruta y operador. **Fuera:** el hardware, la conectividad y el monitoreo de validadores y lectores; la conciliación financiera; la liquidación contractual a operadores; la orden y ejecución del pago a operadores; contabilidad, PQRS, analítica, fraude y efectivo. La aplicación intercambia con los sistemas de los equipos transacciones y confirmaciones de entrada, y parámetros, listas y operaciones pendientes de salida, sin administrar los dispositivos. Entrega al proceso externo una base consolidada sin conciliar; allí se concilia con el dinero, se liquida según contratos y la fiduciaria ejecuta los pagos. El cobro agrupado al pasajero sí permanece dentro del alcance.

---

## 1. Contexto y entrevista

**Solicitud (Tema 4):** «Operamos el sistema integrado de transporte de la ciudad, con tres modos… Necesitamos un software que apoye el proceso de recaudo… y que permita a residentes y visitantes pagar su viaje de forma ágil y con la tarifa que les corresponde». El alcance cubre:
- Tres medios de pago: VAMOS, débito y crédito.
- Gestión de VAMOS.
- Tarifas y perfiles.
- Tarifa correcta con transbordos.
- Consolidación por modo, ruta y operador, como base para la distribución y la conciliación.

Los dispositivos quedan fuera.

**Entrevista (Fase 0).** El equipo configuró un experto simulado con una [instrucción de rol](entrevista/instruccion_de_rol.md) que le prohíbe proponer diseño y le exige marcar cada afirmación como [Norma], [Práctica] o [Supuesto] con su nivel de certeza. La [conversación íntegra](entrevista/conversacion_fase0_completa.txt) tiene diez bloques temáticos (B1-B10), incluido un bloque específico de interoperabilidad (B9). Las preguntas enviadas están en el [guion](entrevista/guion.md), con su redacción literal.

El [análisis de hallazgos](entrevista/analisis_hallazgos.md) clasifica 44 hallazgos en aceptados, aceptados como supuesto configurable, contrastados o descartados, e indica en qué parte del diseño influye cada uno. Algunos resultados de ese análisis:
- Las normas que el diseño usa como restricción se contrastaron con su texto publicado: Ley 1581 de 2012 y Ley 1755 de 2015. Las demás no se usan como reglas.
- Los umbrales de indicadores se descartaron porque el experto dijo que no son estándar.
- La fila 10 de la tabla del equipo («transbordo solo con VAMOS») se corrigió con la entrevista (D-10).
- Los turnos finales de la conversación, en los que se pidió al asistente generar un mapa y modelos, **no** se usan como hallazgos.

---

## 2. Motivación

### V1. Por qué existe la aplicación: de los interesados a los requerimientos
[![V1 — Motivación: de los interesados a los requerimientos](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)

[Abrir V1 en SVG](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)

**Análisis.** Una sola vista recorre toda la motivación, de izquierda a derecha:
- **Interesados (B1.1) e impulsores (B1.2).**
- **Evaluaciones:** los diagnósticos del experto, como «sin caja no hay operación» o los reclamos frecuentes y su causa.
- **Metas:** son cuatro. GOL01 viene literal del Tema 4; GOL02 es lo que busca la gerencia (B1.4); GOL03 sale del requisito de verificar perfiles, y GOL04 responde a las necesidades del usuario.
- **Resultados y cursos de acción:** a la derecha de cada meta. Cada resultado dice en su propiedad «Indicador» cómo se mide (B7.2), sin umbrales, porque el experto aclaró que los suyos no son estándar (B7.3). Cada curso de acción va con las capacidades que lo hacen posible. COA02, «centralizar en el ente gestor las reglas… y recibir las transacciones», es la decisión de frontera D-01 expresada como estrategia.
- **Requerimientos:** a la derecha de cada resultado.
  - REQ01 a REQ05 son el alcance literal del Tema 4; REQ03 nombra los cuatro perfiles especiales (D-29).
  - REQ06 a REQ12 se **derivan** de lo que dijo el experto, porque la entrevista no preguntó requerimientos de forma directa. Cubren idempotencia y día de servicio, ajustes con huella, doble control, tokenización, continuidad temporal ante pérdida de conectividad con la última configuración local, evidencia de perfiles y avisos al usuario (REQ12, B9.12).
- **Principios y restricciones:** en la última columna, influyendo (+ y −) sobre cada requerimiento.
  - Los principios son las «reglas de oro» del experto (B1.6).
  - Las restricciones son lo que no se puede cambiar (B1.5), la exclusión de dispositivos (T4) y las dos leyes contrastadas.
  - Dos principios quedan sin línea a propósito, la separación de dineros y la doble verificación con el banco: aplican a la conciliación y al pago, que están fuera (D-04).

**Argumentación.** Se sigue el patrón de 6_TOGAF diap. 41:
- la evaluación influye en la meta;
- el resultado y el curso de acción realizan la meta;
- el requerimiento realiza el resultado;
- la capacidad realiza el curso de acción.

Juntar todo en una vista muestra la cadena completa de la motivación que pide el enunciado. Es alta, pero se lee en columnas y sin cruces; un elemento se repite cuando se relaciona con varios de la columna anterior.

---

## 3. Mapa de capacidades y proceso E2E

### V2. Mapa de capacidades del negocio
[![V2 — Mapa de capacidades del negocio](vistas/V2%20%C2%B7%20Mapa%20de%20capacidades%20del%20negocio.svg)](vistas/V2%20%C2%B7%20Mapa%20de%20capacidades%20del%20negocio.svg)

[Abrir V2 en SVG](vistas/V2%20%C2%B7%20Mapa%20de%20capacidades%20del%20negocio.svg)

**Análisis.** El mapa tiene 15 grupos de nivel 1 y 57 capacidades de nivel 2, estratégicas, misionales y de apoyo, con la paleta de 7_SOA diap. 35. El impacto se marca así:
- **Alto** (borde naranja): la capacidad la realiza la aplicación. Son 13.
- **Medio** (borde azul): la capacidad intercambia información con la aplicación. Son 23.
- **Sin impacto:** son 21.

Los **recursos** (café claro) van dentro de la capacidad a la que se asignan; ArchiMate permite mostrar la asignación por anidamiento (6_TOGAF diap. 27). Los **cursos de acción** están en la V1, junto a la meta que realizan y a las capacidades que los hacen posibles.

**Argumentación.** El mapa es del **negocio completo** (D-15). Por eso incluye capacidades sin impacto, como la operación de cada modo, el efectivo, la parte jurídica, talento humano e infraestructura. Así se evita el nivel «mapa centrado solo en la aplicación».
- **Las capacidades no se conectan entre sí:** no son pasos de un proceso.
- **Dónde actúa la aplicación:** se ve por el borde. La relación «la aplicación realiza la capacidad» está en el modelo y se recorre en la V10.

### V3. Cadena de valor, proceso E2E y dónde se ubica la aplicación
[![V3 — Cadena de valor y proceso E2E: dónde se ubica la aplicación](vistas/V3%20%C2%B7%20Cadena%20de%20valor%20y%20proceso%20E2E%3A%20do%CC%81nde%20se%20ubica%20la%20aplicacio%CC%81n.svg)](vistas/V3%20%C2%B7%20Cadena%20de%20valor%20y%20proceso%20E2E%3A%20do%CC%81nde%20se%20ubica%20la%20aplicacio%CC%81n.svg)

[Abrir V3 en SVG](vistas/V3%20%C2%B7%20Cadena%20de%20valor%20y%20proceso%20E2E%3A%20do%CC%81nde%20se%20ubica%20la%20aplicacio%CC%81n.svg)

**Análisis.**
- **Arriba, la cadena de valor:** cada paso sube a la etapa que realiza.
- **En el medio, el proceso:** cada paso está en el carril de quien lo hace.
- **Debajo de cada paso apoyado, el servicio de la aplicación (cian) que le sirve.** Así se ve dónde se ubica la aplicación:
  - Hace la venta y la recarga, la tarificación, el cobro agrupado y la consolidación.
  - A los equipos les entrega las versiones de tarifas, perfiles, reglas de integración, listas de bloqueo y calendario que necesitan para validar localmente (D-05).
  - Al sistema externo de conciliación y liquidación le entrega la base consolidada sin conciliar (D-04, D-25).
  - A la contabilidad le envía el resumen por el traductor SA07 (D-08).
  - Los pasos grises están fuera de la aplicación.
- **El registro de la tarifa vigente** (área de recaudo del ente gestor) también está en la V3, porque realiza la primera etapa. Los trámites de tarjeta y perfil y la atención de reclamos son procesos de soporte que no ocurren en cada viaje; están en el modelo y sirven a la V4.

**Recorridos:**
- **Tarjeta bancaria:** escoger cómo pagar → validar. Después de tarificar, solo ella pasa por el cobro agrupado.
- **VAMOS:** ¿tiene tarjeta?
  - Sin tarjeta: compra y recarga.
  - Con tarjeta: ¿saldo suficiente?
    - Saldo insuficiente: recarga.
    - **Saldo suficiente: valida directamente**, sin recargar.
- **La tarifa (D-05):** la autoridad autoriza las tarifas y descuentos. El ente gestor registra, versiona y publica sus reglas. En el acceso, el equipo calcula y aplica localmente la tarifa con la versión vigente; ante una pérdida de conectividad puede continuar temporalmente con la última configuración y sincronizar después. Al recibir la transacción, la aplicación central recalcula la tarifa correcta según versión, perfil e integración, compara el resultado con lo aplicado por el equipo y registra las diferencias. Para tarjeta bancaria, ese cálculo central determina el valor que entra al cobro agrupado.
- **La consolidación:** el consumo se atribuye por día de servicio, modo, ruta y operador. Las recargas y los resultados de cobro bancario se conservan como líneas de control separadas y no se suman al consumo ni a la base de distribución.

**Argumentación.** Para que la aplicación cupiera en la misma vista sin cruzar líneas, la pregunta del VAMOS se dividió en dos bifurcaciones, ¿tiene tarjeta? y ¿saldo suficiente?, que es además la lógica real del recorrido. Los servicios de la aplicación van justo debajo del paso al que sirven, con la relación «sirve a» de servicio de aplicación a proceso de negocio (6_TOGAF diap. 44).

---

## 4. Descomposición de servicios

Hay seis capas de servicio reales (7_SOA diap. 20 y 28); el proceso E2E está encima y **no se cuenta como capa**. En total son 84 servicios: 74 incluidos y 10 excluidos. Están en la [tabla de inclusión y exclusión](docs/final/inclusion_exclusion.md), con la justificación y la fuente de cada uno.

### V4. Seis capas, qué entra y qué no, contratos y quién presta los servicios
[![V4 — Descomposición de servicios: seis capas, alcance y contratos](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)

[Abrir V4 en SVG](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)

**Análisis.**
- **Izquierda, el árbol de servicios:** pasos del proceso → capa 1 (plataforma) → capa 2 (dominio) → **contrato** de cada servicio de dominio (Contract First, D-13).
- **Derecha, quién presta los servicios:** el ente gestor asigna los roles; cada rol responde por funciones; cada función realiza servicios de dominio y usa información del negocio (acceso). El *Perfil especial* se divide en los **cuatro perfiles del Tema 4** (D-29).
- **Debajo, completas, las capas 3 a 6:**
  - Capa 3: servicios básicos, cada uno en el recuadro del servicio de dominio al que sirve.
  - Capa 4: traductores hacia afuera; sus intercambios con dirección están en la V9.
  - Capa 5: datos maestros.
  - Capa 6: servicios comunes.
- **Excluidos:** van en gris (D-12): conciliación financiera, liquidación y pago a operadores (D-04), contabilidad (D-08), PQRS (D-07), analítica, dispositivos (D-06), efectivo y comisiones, y fraude. El cobro agrupado al pasajero con tarjeta bancaria sí está incluido.

**Argumentación.** Son seis capas reales (7_SOA diap. 20 y 28); el proceso E2E está encima y no se cuenta como capa. El tamaño de cada servicio sigue las preguntas de 7_SOA diap. 33: quién es responsable y quién gestiona los datos. Por ejemplo, el saldo pertenece a SD4 y la transacción a SD5.

**Contract First.** Cada servicio incluido tiene su objeto *contract*, en total 74; ArchiMate 3.2 solo permite asociación entre contrato y servicio. La V4 muestra los contratos de dominio y la V9 los de la capa anticorrupción. Todos están en el modelo y su especificación completa en [contratos_servicios.md](docs/final/contratos_servicios.md):
- operación, entrada y salida;
- precondiciones y postcondiciones (9_DDD diap. 39);
- reglas y errores;
- requisitos no funcionales;
- **formato y protocolo** (D-24);
- versión (7_SOA diap. 44-47).

La justificación de cada inclusión y exclusión está en la [tabla de inclusión y exclusión](docs/final/inclusion_exclusion.md): 84 servicios, de los que 74 entran y 10 no.

---

## 5. Dominios y lenguaje ubicuo

A partir de aquí el diseño pasa a la capa de aplicación. **Cómo se extrajeron los dominios** (9_DDD diap. 8-10):
1. Estructura de la organización (B2.1, B4.2).
2. Proceso detallado con sus eventos (los de la V6).
3. Puntos de corte donde cambia el dueño del dato. Por ejemplo, la transacción la acepta Recepción de transacciones, le calcula la tarifa Tarifas y transbordos y la asigna a su ruta y operador Consolidación.

La tabla de eventos por dominio y los argumentos completos están en [dominios.md](docs/final/dominios.md).

### V5. Dominios y su clasificación
[![V5 — Dominios y su clasificación](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)

[Abrir V5 en SVG](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)

**Análisis y argumentación (9_DDD diap. 11).** Cada dominio muestra sus objetos de negocio y el contexto que lo implementa.
- **Centrales:**
  - *Tarifas y transbordos*: es el diferenciador que pide el Tema 4. Tiene las reglas más variables y sus errores causan los reclamos más frecuentes (B3.6, B6.1, B6.3).
  - *Consolidación del recaudo*: sostiene la meta «cada peso llega a quien corresponde» y es la base de la distribución. Las disputas con los operadores son por conteo y atribución (B1.1, B3.6).
- **De soporte:** tarjetas VAMOS y saldos, perfiles y descuentos, pago con tarjeta del banco, recepción de transacciones, ajustes y reclamos, y rutas y calendario. El pago con tarjeta es de soporte y no central, aunque es complejo, porque aplica una práctica del sector (el cobro agrupado) y la decisión de cuánto cobrar la toma Tarifas y transbordos.
- **Genéricos:** usuarios internos y permisos, avisos y auditoría.

Cada dominio tiene responsable, datos y reglas propios; los dominios genéricos corresponden a capacidades comunes que pueden apoyarse en soluciones de mercado. Los eventos que justifican los puntos de corte se muestran en V6 y se detallan en `docs/final/dominios.md`.

### V7. Lenguaje ubicuo
[![V7 — Lenguaje ubicuo: glosario por contexto y palabras con varios significados](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)

[Abrir V7 en SVG](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)

**Análisis.** Arriba está el glosario. Cada tarjeta tiene el término (*representation*), el objeto de negocio que nombra (realización) y su definición (*meaning*); el recuadro indica el contexto donde vale (D-20). Las definiciones precisan:
- «Cobro agrupado»: al cierre del día **o** al superar un umbral (D-11).
- «Reposición»: qué saldo se traslada y cuándo (D-28).
- «Base de distribución»: es consolidada, no conciliada (D-25).
- «Perfil especial»: los cuatro tipos (D-29).

Abajo están los términos que **cambian de significado** según quién los use. Cada término se asocia a sus significados y cada significado al contexto o a la parte externa donde vale:
- «Operador»: operador de transporte, concesionario o uso amplio.
- «Viaje»: abordajes integrados, demanda por abordaje u origen-destino.
- «Saldo»: saldo conocido, saldo en la tarjeta o pasivo contable.
- «Tarifa»: correcta, aplicada o técnica.
- «Recaudado» y «Cobro».
- «Base»: la base **consolidada** que entrega la aplicación frente a la base **conciliada** que produce la conciliación (D-25).

El glosario completo, con definición, contexto, ejemplo y fuente, está en [lenguaje_ubicuo.md](docs/final/lenguaje_ubicuo.md). Los nombres de los elementos de todas las vistas usan estos términos.

---

## 6. Agregados, comandos y eventos

### V6. Un diagrama por dominio, en una sola vista
[![V6 — Agregados, comandos y eventos: un diagrama por dominio](vistas/V6%20%C2%B7%20Agregados%2C%20comandos%20y%20eventos%3A%20un%20diagrama%20por%20dominio.svg)](vistas/V6%20%C2%B7%20Agregados%2C%20comandos%20y%20eventos%3A%20un%20diagrama%20por%20dominio.svg)

[Abrir V6 en SVG](vistas/V6%20%C2%B7%20Agregados%2C%20comandos%20y%20eventos%3A%20un%20diagrama%20por%20dominio.svg)

**Análisis.** La vista tiene **un diagrama por dominio**, como pide el enunciado: once bloques titulados con el dominio y su clasificación, que se pueden mover y ampliar por separado en Archi. Ninguna línea sale de su bloque: cuando un evento dispara un comando de otro agregado (política), ese comando se repite dentro del bloque en lila, con el nombre de su agregado. Son 16 agregados y cada uno muestra:
- su **raíz**, que contiene sus entidades y sus objetos de valor (el **límite**);
- los comandos que escriben en la raíz y los eventos que emiten;
- las **políticas**, es decir, el comando que un evento dispara en otro agregado;
- debajo, sus **invariantes**.

**Reglas destacadas del diseño:**
- **Cobro agrupado (V6, D-11).** Antes decía «un solo cobro por día», lo que contradecía el umbral que describió el experto (B3.3). Ahora:
  - cada viaje entra en un solo cargo;
  - hay un cargo al cierre del día o antes si se supera el umbral, hasta un máximo configurado;
  - la suma del día no pasa el tope si se configura;
  - un abordaje posterior a un cargo conserva el transbordo de su viaje.
- **Consolidado (V6, D-26 y D-25).** Las recargas, el consumo y los resultados de cobro bancario van en líneas separadas que no se suman. La base de distribución se calcula solo desde el consumo atribuido; la conciliación externa devuelve sus diferencias como propuestas de ajuste.
- **Tarjeta VAMOS (V6, D-28).** El saldo de la reposición es el saldo conocido a la hora del bloqueo efectivo, calculado cuando cerraron esos días.
- **Perfil especial (V6, D-29).** El tipo es uno de los cuatro del Tema 4 y cada uno exige su certificación.
- **Políticas entre agregados.**
  - El movimiento de saldo lo dispara el abordaje tarificado (relación Tarifas → Tarjetas), y no la transacción aceptada, porque entre Recepción y Tarjetas no hay relación en el mapa de contextos.
  - Las transacciones tardías también se tarifan.
  - El consolidado se rehace solo si la transacción cae en un día ya cerrado.
  - El validador comprueba que cada política entre contextos distintos tenga su relación en la V8.

**Argumentación del alcance.** Cada agregado documenta por qué tiene ese límite:
- La recarga se separa de la tarjeta porque nace en canales externos.
- Cada transacción es su propio agregado, para recibir millones al día sin bloqueos.
- El consolidado del día de servicio es la unidad de cierre diario.

El detalle está en [agregados.md](docs/final/agregados.md). **Notación (D-19):** agrupación por agregado, objetos de datos para la raíz, las entidades y los objetos de valor, procesos de aplicación para los comandos y eventos de aplicación para los eventos (9_DDD diap. 18-23).

---

## 7. Mapa de contextos e interoperabilidad

### V8. Mapa de contextos delimitados
[![V8 — Mapa de contextos delimitados](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)

[Abrir V8 en SVG](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)

**Análisis.** Hay un contexto delimitado por dominio, modelado como componente de aplicación con su **responsabilidad** (la nota de arriba), su interfaz y sus servicios (D-17, 9_DDD diap. 25-27). Los patrones son:
- **[C/P] Cliente-proveedor:** entre los contextos centrales y los de soporte, como flujo del proveedor al consumidor. Por ejemplo:
  - Recepción → Tarifas, con la transacción aceptada.
  - Tarifas → Consolidación, con el abordaje con su tarifa.
  - Tarjetas → Consolidación, con las recargas **aparte del consumo** (D-26).
- **[OHS/PL] Servicio abierto con lenguaje publicado:** desde Rutas y calendario.
- **[CF] Conformista:** hacia Usuarios internos y permisos.
- **[OHS] Servicio abierto:** Avisos **sirve a** Pago con tarjeta del banco y a Perfiles. Es una relación «servida por» y no un flujo, porque son ellos los que le piden el envío cuando ocurre su evento (D-27).
- **Núcleo compartido:** limitado a los identificadores (número de tarjeta, token, transacción y día de servicio).
- **Auditoría:** es transversal para operaciones sensibles y correctivas. La vista omite sus relaciones para conservar la legibilidad; la cobertura exacta se especifica mediante SI2 y los contratos, por lo que no debe interpretarse que toda consulta genera el mismo tipo de registro.

Las responsabilidades de cada relación están en [contextos.md](docs/final/contextos.md).

### V9. Interoperabilidad y anticorrupción
[![V9 — Interoperabilidad y anticorrupción](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)

[Abrir V9 en SVG](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)

**Análisis.** Es la capa anticorrupción completa. Para cada servicio externo, de SA01 a SA15, la vista muestra:
- el componente externo y cada flujo con nombre y dirección explícitos; cuando existe intercambio en ambos sentidos se modela con relaciones separadas;
- la interfaz anticorrupción, dentro del contexto dueño y asignada a su traductor;
- el **servicio anticorrupción de la Fase 2** que ese traductor realiza, con su **contrato**;
- el patrón de relación.

Cada fila enlaza el sistema externo, la interfaz del contexto dueño, el traductor, el servicio anticorrupción de Fase 2, su contrato y el patrón. La tabla de [anticorrupción](docs/final/anticorrupcion.md) documenta 35 flujos dirigidos correspondientes a los 15 servicios SA01–SA15.

En SA08 sale la base consolidada **sin conciliar**. Regresan por flujos separados las diferencias monetarias encontradas por la conciliación y las novedades de atribución que deben corregirse. Fuera de la aplicación, la secuencia es conciliar, liquidar y ordenar o ejecutar el pago a operadores (D-04, D-25, S-09).

**Argumentación.** El patrón depende de quién manda en el formato, y es coherente con la Fase 2:
- **Capa anticorrupción:** para los formatos propietarios de los equipos, la red, las certificadoras y el sistema legado.
- **Conformista:** con la autoridad, el adquirente y la pasarela.
- **Lenguaje publicado:** hacia el área financiera, la liquidación y los operadores.

El formato y el protocolo de cada intercambio están en su contrato (D-24).

---

## 8. Bounded Context Canvas

### V11. Canvas del contexto Tarifas y transbordos
[![V11 — Bounded Context Canvas: Tarifas y transbordos](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)

[Abrir V11 en SVG](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)

**Análisis.** El canvas está en una página con las secciones de la plantilla de ddd-crew (9_DDD diap. 34-35):
- Propósito, clasificación estratégica (central, ingreso y cumplimiento, hecho a la medida) y roles (contexto de ejecución y de especificación).
- Comunicación entrante y saliente: colaborador y mensaje, con su tipo.
- Lenguaje ubicuo, decisiones de negocio, supuestos, métricas de verificación y preguntas abiertas.

**Argumentación.** Se eligió este contexto porque es central, concentra las reglas que pide el Tema 4 y tiene más comunicación entrante y saliente (D-18). Para construirlo en Archi (D-22), las secciones son agrupaciones y se reutilizan elementos del modelo: el componente, los eventos y comandos de la V6, los términos de la V7 y los colaboradores de la V8 y la V9. El propósito, la clasificación, los roles y las métricas son *meaning*; las decisiones son *constraint*, y los supuestos y las preguntas son *assessment*.

---

## 9. Trazabilidad vertical

### V10. De la meta al componente
[![V10 — Trazabilidad vertical: de cada requerimiento a sus componentes (REQ01-REQ12)](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)

[Abrir V10 en SVG](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)

**Análisis.** La cadena es meta ← resultado ← requerimiento ← capacidad ← servicio de negocio ← servicio de aplicación ← contexto delimitado. Todas son relaciones de realización visibles y cada columna solo se conecta con la siguiente. Una sola vista cubre los doce requerimientos y **los once contextos**.

Los once contextos principales llegan a una meta. Rutas y calendario participa en recepción y consolidación; Avisos llega por REQ12; Auditoría y soportes llega por REQ07 y REQ11. Los componentes externos y los adaptadores ACL de V9 no son realizadores directos de metas internas y por eso no aparecen como destino final de esta vista.

La matriz completa está en [trazabilidad.md](docs/final/trazabilidad.md). El validador comprueba que **cada** contexto llega a una meta.

---

## 10. Decisiones y supuestos

El registro completo está en [decisiones_y_supuestos.md](docs/final/decisiones_y_supuestos.md): 30 decisiones (D-01 a D-30), 12 supuestos y los parámetros sin valor. Las decisiones que más cambian el diseño son:

| Código | Decisión | Por qué |
|---|---|---|
| D-01 | La aplicación es la plataforma de recaudo del ente gestor; los equipos los conserva su proveedor | El Tema 4 pide las funciones del sistema central y dice que el software «recibe las transacciones» |
| D-04 | La conciliación financiera, la liquidación contractual y el pago a operadores quedan fuera; la aplicación entrega la base consolidada | Tema 4: consolidación «como base para». La aplicación consolida; el sistema externo concilia y liquida, y la fiduciaria ejecuta el pago (B3.1, B3.5, B2.7). El cobro bancario al pasajero sí está incluido. |
| D-05 | La autoridad autoriza; el ente gestor registra, versiona y publica; el equipo calcula y aplica localmente; la aplicación central recalcula, compara y registra diferencias | Distingue la validación inmediata, incluida la contingencia temporal sin conectividad, de la verificación central exigida por el Tema 4 (B4.4, B9.13). |
| D-02 | El metro es un modo integrado con su propia ACL | El Tema 4 incluye los tres modos; el experto supone un sistema propio del metro |
| D-10 | La tarjeta bancaria paga tarifa plena y sí tiene integración | B2.5, B3.3 |
| D-21 | Las reglas variables son parámetros sin valor inventado | Lo que el experto dio como supuesto o con certeza baja |
| D-30 | Exactamente una vista para cada V1–V11; V6 contiene once bloques independientes, uno por dominio | Cumple la organización compacta del enunciado y permite recorrer el modelo durante la sustentación. |
