# Recaudo del sistema integrado de transporte de una ciudad mediana

**Proyecto:** «Diseño de la arquitectura de una aplicación empresarial con ArchiMate y DDD», Tema 4. Arquitectura de Software, UPB.

> **Modelo definitivo:** [`modelo/recaudo_tema4.archimate`](modelo/recaudo_tema4.archimate). Se abre en Archi 5.x y contiene once vistas, de V1 a V11.

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
10. [Decisiones principales](#10-decisiones-principales)
11. [Validación, fuentes y limitaciones](#11-validación-fuentes-y-limitaciones)
12. [Tabla de aportes](#12-tabla-de-aportes)

**Acceso directo a las vistas:** [V1](#v1-por-qué-existe-la-aplicación-de-los-interesados-a-los-requerimientos) · [V2](#v2-mapa-de-capacidades-del-negocio) · [V3](#v3-cadena-de-valor-proceso-e2e-y-dónde-se-ubica-la-aplicación) · [V4](#v4-seis-capas-qué-entra-y-qué-no-contratos-y-quién-presta-los-servicios) · [V5](#v5-dominios-y-su-clasificación) · [V6](#v6-un-diagrama-por-dominio-en-una-sola-vista) · [V7](#v7-lenguaje-ubicuo) · [V8](#v8-mapa-de-contextos-delimitados) · [V9](#v9-interoperabilidad-y-anticorrupción) · [V10](#v10-de-la-meta-al-componente) · [V11](#v11-canvas-del-contexto-tarifas-y-transbordos)

---

## 0. Cómo está organizada la entrega

| Ruta | Contenido |
|---|---|
| [`modelo/recaudo_tema4.archimate`](modelo/recaudo_tema4.archimate) | Modelo ArchiMate único y definitivo (Archi 5.x, ArchiMate 3.2) |
| [`vistas/`](vistas/) | Las 11 vistas exportadas por Archi en formato SVG |
| [`entrevista/`](entrevista/) | Conversación, preguntas y análisis de la entrevista |
| [`docs/final/`](docs/final/) | Documentos completos: [inclusión y exclusión](docs/final/inclusion_exclusion.md), [anticorrupción](docs/final/anticorrupcion.md), [contratos](docs/final/contratos_servicios.md), [dominios](docs/final/dominios.md), [lenguaje ubicuo](docs/final/lenguaje_ubicuo.md), [agregados e invariantes](docs/final/agregados.md), [contextos y patrones](docs/final/contextos.md), [trazabilidad](docs/final/trazabilidad.md), [decisiones y supuestos](docs/final/decisiones_y_supuestos.md) y [validación](docs/final/validacion.md) |
| [`herramientas/`](herramientas/) | Scripts de generación, exportación y validación |
| [Enunciado](enunciado/Proyecto_Diseño_Arquitectura_ArchiMate%20(1).docx), [Tema 4](docs/contexto/02_tema4_recaudo.md) y [`diapositivas/`](diapositivas/) | Fuentes académicas utilizadas |

El modelo tiene once vistas, de V1 a V11. La V6 reúne once diagramas independientes, uno por dominio, dentro de una misma vista. Las tablas y especificaciones completas están en `docs/final/`.

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
| V9 Interoperabilidad | Cada intercambio externo con su dirección, la interfaz, el traductor y su contrato |
| V10 Trazabilidad | De la meta al componente, con relaciones visibles, para los 11 contextos |
| V11 Canvas | El contexto principal, Tarifas y transbordos |

---

## 1. Contexto y entrevista

**Solicitud (Tema 4):** «Operamos el sistema integrado de transporte de la ciudad, con tres modos… Necesitamos un software que apoye el proceso de recaudo… y que permita a residentes y visitantes pagar su viaje de forma ágil y con la tarifa que les corresponde». El alcance cubre:
- Tres medios de pago: VAMOS, débito y crédito.
- Gestión de VAMOS.
- Tarifas y perfiles.
- Tarifa correcta con transbordos.
- Consolidación por modo, ruta y operador, como base para la distribución y la conciliación.

Los dispositivos quedan fuera.

La entrevista amplió la información del enunciado sobre la operación diaria, las reglas tarifarias, los reclamos, los intercambios con otros sistemas y la distribución del recaudo. El análisis completo se conserva en la carpeta `entrevista/`. Los principales resultados fueron:
- Las normas que el diseño usa como restricción se contrastaron con su texto publicado: Ley 1581 de 2012 y Ley 1755 de 2015. Las demás no se usan como reglas.
- Los umbrales de indicadores se descartaron porque el experto dijo que no son estándar.
- La integración tarifaria también se aplica cuando el pasajero paga con tarjeta bancaria.

---

## 2. Motivación

### V1. Por qué existe la aplicación: de los interesados a los requerimientos
[![V1 — Motivación: de los interesados a los requerimientos](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)

[Abrir V1 en SVG](vistas/V1%20%C2%B7%20Motivacio%CC%81n%3A%20de%20los%20interesados%20a%20los%20requerimientos.svg)

**Análisis.** La vista se lee de izquierda a derecha. Empieza con las personas y organizaciones interesadas en el sistema, sigue con los problemas que impulsan el proyecto y termina con las metas y los requerimientos de la aplicación. Entre ellos aparecen los resultados esperados y las acciones necesarias para alcanzarlos.

El modelo plantea cuatro metas: asegurar la tarifa correcta, mantener el control del recaudo, verificar los beneficios de los perfiles especiales y facilitar el viaje del pasajero. Los cinco primeros requerimientos vienen directamente del enunciado. Los demás surgieron de la entrevista y cubren asuntos necesarios para operar el sistema, como evitar transacciones duplicadas, registrar los ajustes, proteger los datos bancarios, continuar temporalmente ante una pérdida de conectividad y avisar al usuario sobre el resultado de sus operaciones.

La última columna muestra los principios y las restricciones que condicionan esos requerimientos. Allí aparecen, entre otros, la protección de datos personales, la atención de solicitudes de los usuarios y la exclusión de los dispositivos físicos del alcance de la aplicación.

**Argumentación.** Se sigue el patrón presentado en la diapositiva 41 de la clase de TOGAF:
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

**Argumentación.** El mapa representa el negocio completo, no solo la aplicación. Por eso incluye capacidades que el software no realiza, como la operación de cada modo de transporte, el manejo de efectivo, la gestión jurídica, el talento humano y la infraestructura.
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
  - Entrega a los equipos las tarifas, perfiles, reglas de integración, listas de bloqueo y calendarios que necesitan para validar localmente.
  - Entrega al sistema de conciliación y liquidación una base consolidada que todavía no ha sido comparada con el dinero recibido.
  - Envía a contabilidad un resumen por medio de una interfaz de integración.
  - Los pasos grises están fuera de la aplicación.
- **El registro de la tarifa vigente** (área de recaudo del ente gestor) también está en la V3, porque realiza la primera etapa. Los trámites de tarjeta y perfil y la atención de reclamos son procesos de soporte que no ocurren en cada viaje; están en el modelo y sirven a la V4.

**Recorridos:**
- **Tarjeta bancaria:** escoger cómo pagar → validar. Después de tarificar, solo ella pasa por el cobro agrupado.
- **VAMOS:** ¿tiene tarjeta?
  - Sin tarjeta: compra y recarga.
  - Con tarjeta: ¿saldo suficiente?
    - Saldo insuficiente: recarga.
    - **Saldo suficiente: valida directamente**, sin recargar.
- **La tarifa:** la autoridad autoriza las tarifas y descuentos. El ente gestor registra, versiona y publica las reglas. En el acceso, el equipo calcula y aplica la tarifa con la versión vigente. Si pierde la conexión, puede trabajar temporalmente con la última configuración y sincronizar después. Cuando la aplicación central recibe la transacción, vuelve a calcular la tarifa según la versión, el perfil y las reglas de integración. Después compara ambos resultados y registra cualquier diferencia. En los pagos con tarjeta bancaria, este cálculo define el valor que se cobrará.
- **La consolidación:** el consumo se atribuye por día de servicio, modo, ruta y operador. Las recargas y los resultados de cobro bancario se conservan como líneas de control separadas y no se suman al consumo ni a la base de distribución.

**Argumentación.** Para que la aplicación cupiera en la misma vista sin cruzar líneas, la pregunta del VAMOS se dividió en dos bifurcaciones, ¿tiene tarjeta? y ¿saldo suficiente?, que es además la lógica real del recorrido. Los servicios de la aplicación van justo debajo del paso al que sirven, con la relación «sirve a» de servicio de aplicación a proceso de negocio (6_TOGAF diap. 44).

---

## 4. Descomposición de servicios

Hay seis capas de servicio reales (7_SOA diap. 20 y 28); el proceso E2E está encima y **no se cuenta como capa**. En total son 84 servicios: 74 incluidos y 10 excluidos. Están en la [tabla de inclusión y exclusión](docs/final/inclusion_exclusion.md), con la justificación y la fuente de cada uno.

### V4. Seis capas, qué entra y qué no, contratos y quién presta los servicios
[![V4 — Descomposición de servicios: seis capas, alcance y contratos](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)

[Abrir V4 en SVG](vistas/V4%20%C2%B7%20Descomposicio%CC%81n%20de%20servicios%3A%20seis%20capas%2C%20alcance%20y%20contratos.svg)

**Análisis.**
- **Izquierda, el árbol de servicios:** los pasos del proceso se descomponen primero en servicios de plataforma y después en servicios de dominio. Cada servicio de dominio tiene un contrato que define cómo se usa.
- **Derecha, quién presta los servicios:** el ente gestor asigna los roles; cada rol responde por funciones y cada función utiliza la información necesaria. Los perfiles especiales se dividen en cuatro tipos: estudiante, adulto mayor, persona con discapacidad y beneficiario de subsidio.
- **Debajo, completas, las capas 3 a 6:**
  - Capa 3: servicios básicos, cada uno en el recuadro del servicio de dominio al que sirve.
  - Capa 4: traductores hacia afuera; sus intercambios con dirección están en la V9.
  - Capa 5: datos maestros.
  - Capa 6: servicios comunes.
- **Fuera del alcance:** los elementos grises corresponden a la conciliación financiera, la liquidación y el pago a operadores, la contabilidad, la atención de peticiones y reclamos, la analítica, los dispositivos, el efectivo, las comisiones y la gestión del fraude. El cobro agrupado al pasajero con tarjeta bancaria sí forma parte de la aplicación.

**Argumentación.** La estructura sigue las seis capas presentadas en las diapositivas 20 y 28 de la clase de SOA. El proceso completo aparece encima y no se cuenta como una capa adicional. La responsabilidad sobre los datos ayuda a separar los servicios: el contexto de Tarjetas VAMOS administra el saldo, mientras que Recepción de transacciones administra cada validación recibida.

**Contratos de servicio.** Cada servicio incluido tiene un contrato. La V4 muestra los contratos de los servicios del negocio y la V9 muestra los contratos de integración con sistemas externos. La especificación completa está en [contratos_servicios.md](docs/final/contratos_servicios.md) e incluye:
- operación, entrada y salida;
- precondiciones y postcondiciones (9_DDD diap. 39);
- reglas y errores;
- requisitos no funcionales;
- formato y protocolo;
- versión (7_SOA diap. 44-47).

La justificación de cada inclusión y exclusión está en la [tabla de inclusión y exclusión](docs/final/inclusion_exclusion.md): 84 servicios, de los que 74 entran y 10 no.

---

## 5. Dominios y lenguaje ubicuo

A partir de aquí el diseño pasa a la capa de aplicación. Los dominios se identificaron a partir de tres fuentes:
1. La estructura de la organización y las responsabilidades descritas en la entrevista.
2. Proceso detallado con sus eventos (los de la V6).
3. Puntos de corte donde cambia el dueño del dato. Por ejemplo, la transacción la acepta Recepción de transacciones, le calcula la tarifa Tarifas y transbordos y la asigna a su ruta y operador Consolidación.

La tabla de eventos por dominio y los argumentos completos están en [dominios.md](docs/final/dominios.md).

### V5. Dominios y su clasificación
[![V5 — Dominios y su clasificación](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)

[Abrir V5 en SVG](vistas/V5%20%C2%B7%20Dominios%20y%20su%20clasificaci%C3%B3n.svg)

**Análisis y argumentación.** Cada dominio muestra sus objetos de negocio y el contexto que lo implementa. La clasificación sigue el criterio presentado en la clase de DDD:
- **Centrales:**
  - *Tarifas y transbordos*: concentra las reglas más variables del sistema. Sus errores también están entre las causas más frecuentes de reclamos.
  - *Consolidación del recaudo*: permite saber cuánto consumo corresponde a cada modo, ruta y operador. Esta información sirve como base para la distribución posterior de los ingresos.
- **De soporte:** tarjetas VAMOS y saldos, perfiles y descuentos, pago con tarjeta del banco, recepción de transacciones, ajustes y reclamos, y rutas y calendario. El pago con tarjeta es de soporte y no central, aunque es complejo, porque aplica una práctica del sector (el cobro agrupado) y la decisión de cuánto cobrar la toma Tarifas y transbordos.
- **Genéricos:** usuarios internos y permisos, avisos y auditoría.

Cada dominio tiene responsable, datos y reglas propios; los dominios genéricos corresponden a capacidades comunes que pueden apoyarse en soluciones de mercado. Los eventos que justifican los puntos de corte se muestran en V6 y se detallan en `docs/final/dominios.md`.

### V7. Lenguaje ubicuo
[![V7 — Lenguaje ubicuo: glosario por contexto y palabras con varios significados](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)

[Abrir V7 en SVG](vistas/V7%20%C2%B7%20Lenguaje%20ubicuo%3A%20glosario%20por%20contexto%20y%20palabras%20con%20varios%20significados.svg)

**Análisis.** En la parte superior está el glosario. Cada tarjeta relaciona un término con el objeto del negocio que representa, su definición y el contexto en el que se usa. Allí se aclara que el cobro con tarjeta bancaria puede ejecutarse al superar un umbral o al cerrar el día; que la reposición de una tarjeta traslada el saldo conocido cuando el bloqueo se hace efectivo; que la base de distribución todavía no está conciliada; y que existen cuatro tipos de perfil especial.

Abajo están los términos que **cambian de significado** según quién los use. Cada término se asocia a sus significados y cada significado al contexto o a la parte externa donde vale:
- «Operador»: operador de transporte, concesionario o uso amplio.
- «Viaje»: abordajes integrados, demanda por abordaje u origen-destino.
- «Saldo»: saldo conocido, saldo en la tarjeta o pasivo contable.
- «Tarifa»: correcta, aplicada o técnica.
- «Recaudado» y «Cobro».
- «Base»: puede ser la base consolidada que entrega la aplicación o la base conciliada que se obtiene después de compararla con el dinero recibido.

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
- **Cobro agrupado.** Los viajes pagados con una misma tarjeta bancaria se acumulan antes de solicitar el cobro:
  - cada viaje entra en un solo cargo;
  - hay un cargo al cierre del día o antes si se supera el umbral, hasta un máximo configurado;
  - la suma del día no pasa el tope si se configura;
  - un abordaje posterior a un cargo conserva el transbordo de su viaje.
- **Consolidado.** Las recargas, el consumo y los resultados de cobro bancario se mantienen en líneas separadas. La base de distribución se calcula únicamente con el consumo atribuido. Si la conciliación posterior encuentra diferencias, estas regresan como propuestas de ajuste.
- **Tarjeta VAMOS.** Cuando se repone una tarjeta bloqueada, se traslada el saldo conocido en el momento en que el bloqueo se hizo efectivo.
- **Perfil especial.** Cada perfil corresponde a uno de los cuatro tipos definidos en el enunciado y requiere su certificación.
- **Políticas entre agregados.**
  - El movimiento de saldo lo dispara el abordaje tarificado (relación Tarifas → Tarjetas), y no la transacción aceptada, porque entre Recepción y Tarjetas no hay relación en el mapa de contextos.
  - Las transacciones tardías también se tarifan.
  - El consolidado se rehace solo si la transacción cae en un día ya cerrado.
  - El validador comprueba que cada política entre contextos distintos tenga su relación en la V8.

**Argumentación del alcance.** Cada agregado documenta por qué tiene ese límite:
- La recarga se separa de la tarjeta porque nace en canales externos.
- Cada transacción es su propio agregado, para recibir millones al día sin bloqueos.
- El consolidado del día de servicio es la unidad de cierre diario.

El detalle está en [agregados.md](docs/final/agregados.md). La notación sigue las diapositivas 18 a 23 de la clase de DDD: cada agregado aparece como una agrupación, los datos representan la raíz y sus elementos, los procesos representan comandos y los eventos de aplicación representan hechos que ya ocurrieron.

---

## 7. Mapa de contextos e interoperabilidad

### V8. Mapa de contextos delimitados
[![V8 — Mapa de contextos delimitados](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)

[Abrir V8 en SVG](vistas/V8%20%C2%B7%20Mapa%20de%20contextos%20delimitados.svg)

**Análisis.** Hay un contexto delimitado por dominio. Cada uno muestra su responsabilidad, su interfaz y los servicios que ofrece. Las relaciones principales son:
- **Cliente y proveedor:** un contexto entrega información que otro necesita. Por ejemplo:
  - Recepción → Tarifas, con la transacción aceptada.
  - Tarifas → Consolidación, con el abordaje con su tarifa.
  - Tarjetas → Consolidación, con las recargas separadas del consumo.
- **Servicio abierto con lenguaje publicado:** Rutas y calendario publica una interfaz estable para los demás contextos.
- **Conformista:** Usuarios internos y permisos ofrece un modelo que los consumidores adoptan sin traducirlo.
- **Servicio abierto:** Pago con tarjeta del banco y Perfiles solicitan a Avisos el envío de mensajes cuando ocurre un evento relevante.
- **Núcleo compartido:** limitado a los identificadores (número de tarjeta, token, transacción y día de servicio).
- **Auditoría:** es transversal para las operaciones sensibles y correctivas. La vista omite algunas relaciones para conservar la legibilidad. Los contratos indican cuáles operaciones deben dejar registro, por lo que no toda consulta genera el mismo tipo de evidencia.

Las responsabilidades de cada relación están en [contextos.md](docs/final/contextos.md).

### V9. Interoperabilidad y anticorrupción
[![V9 — Interoperabilidad y anticorrupción](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)

[Abrir V9 en SVG](vistas/V9%20%C2%B7%20Interoperabilidad%20y%20anticorrupci%C3%B3n.svg)

**Análisis.** Esta vista muestra cómo se integra la aplicación con sistemas externos. Para cada integración se presenta:
- el componente externo y cada flujo con nombre y dirección explícitos; cuando existe intercambio en ambos sentidos se modela con relaciones separadas;
- la interfaz anticorrupción, dentro del contexto dueño y asignada a su traductor;
- el servicio de integración que realiza el traductor, junto con su contrato;
- el patrón de relación.

Cada fila enlaza el sistema externo, la interfaz del contexto responsable, el traductor, el servicio, su contrato y el tipo de relación. La tabla de [anticorrupción](docs/final/anticorrupcion.md) contiene el detalle de los 35 intercambios representados.

La aplicación entrega una base consolidada que todavía no ha sido conciliada. El sistema externo devuelve por separado las diferencias monetarias y los cambios que afectan la asignación a cada operador. La conciliación, la liquidación y el pago a operadores se realizan fuera de esta aplicación.

**Argumentación.** El tipo de integración depende de quién define el formato:
- **Capa anticorrupción:** para los formatos propietarios de los equipos, la red, las certificadoras y el sistema legado.
- **Conformista:** con la autoridad, el adquirente y la pasarela.
- **Lenguaje publicado:** hacia el área financiera, la liquidación y los operadores.

El contrato de cada intercambio especifica su formato y su protocolo.

---

## 8. Bounded Context Canvas

### V11. Canvas del contexto Tarifas y transbordos
[![V11 — Bounded Context Canvas: Tarifas y transbordos](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)

[Abrir V11 en SVG](vistas/V11%20%C2%B7%20Bounded%20Context%20Canvas%3A%20Tarifas%20y%20transbordos.svg)

**Análisis.** El canvas está en una página con las secciones de la plantilla de ddd-crew (9_DDD diap. 34-35):
- Propósito, clasificación estratégica (central, ingreso y cumplimiento, hecho a la medida) y roles (contexto de ejecución y de especificación).
- Comunicación entrante y saliente: colaborador y mensaje, con su tipo.
- Lenguaje ubicuo, decisiones de negocio, supuestos, métricas de verificación y preguntas abiertas.

**Argumentación.** Se eligió Tarifas y transbordos porque es uno de los contextos centrales, concentra las reglas tarifarias del enunciado y se comunica con varios contextos internos y sistemas externos. El canvas reutiliza los comandos y eventos de la V6, los términos de la V7 y los colaboradores de las vistas V8 y V9. De esta manera, la información del canvas se puede rastrear hasta las demás partes del modelo.

---

## 9. Trazabilidad vertical

### V10. De la meta al componente
[![V10 — Trazabilidad vertical: de cada requerimiento a sus componentes (REQ01-REQ12)](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)

[Abrir V10 en SVG](vistas/V10%20%C2%B7%20Trazabilidad%20vertical%3A%20de%20cada%20requerimiento%20a%20sus%20componentes%20%28REQ01-REQ12%29.svg)

**Análisis.** La cadena es meta ← resultado ← requerimiento ← capacidad ← servicio de negocio ← servicio de aplicación ← contexto delimitado. Todas son relaciones de realización visibles y cada columna solo se conecta con la siguiente. Una sola vista cubre los doce requerimientos y **los once contextos**.

Los once contextos principales llegan a una meta. Rutas y calendario participa en la recepción y la consolidación; Avisos responde al requerimiento de informar al usuario; Auditoría y soportes responde a los requerimientos de trazabilidad y evidencia. Los sistemas externos y sus adaptadores no realizan directamente las metas de la aplicación, por eso no aparecen como destino final de esta vista.
