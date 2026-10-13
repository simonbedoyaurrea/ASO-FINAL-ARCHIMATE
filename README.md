# Diseño de Arquitectura Empresarial con ArchiMate y DDD

**Tema 4 — Recaudo del sistema integrado de transporte de una ciudad mediana**
**Estado:** repositorio simplificado; el diseño y las evidencias requieren revisión y validación del equipo.

## Presentación

Este proyecto académico organiza el entendimiento del negocio y el diseño de una aplicación para apoyar el recaudo de un sistema integrado de transporte. El equipo elaborará y justificará sus decisiones usando **ArchiMate** y **Domain-Driven Design (DDD)**.

### Problema de negocio

El caso asignado aborda el recaudo asociado a buses alimentadores, buses articulados y metro. El sistema debe considerar pagos con tarjeta VAMOS y tarjetas débito/crédito, el ciclo de vida de VAMOS, tarifas plenas o especiales, perfiles y transbordos, y la consolidación por modo, ruta y operador para distribución y conciliación. Estos puntos describen el caso asignado; su interpretación y las decisiones de diseño deben ser validadas por el equipo.

### Objetivos académicos

- Entender el negocio mediante una entrevista y analizar sus hallazgos.
- Modelar motivación, capacidades y proceso de extremo a extremo.
- Descomponer servicios y documentar sus contratos.
- Aplicar DDD estratégico y táctico, con trazabilidad entre vistas.
- Justificar las decisiones del equipo con evidencia verificable.

### Alcance y exclusiones del caso

El alcance de negocio incluye las operaciones de recaudo, medios de pago, tarifas, perfiles, transbordos, consolidación y conciliación descritas en el enunciado asignado. Los validadores, lectores, otros dispositivos e IoT están fuera del alcance indicado: la aplicación recibe transacciones y no administra esos equipos. Las interoperabilidades con atención al cliente, finanzas, planeación, redes de pago, certificadores de perfiles y autoridad de transporte son aspectos por investigar; esta lista no afirma que estén diseñados o validados.

**Fuente académica:** existe una copia local del enunciado, excluida de Git por privacidad y revisión de publicación. Confirmar con el profesor que su versión esté vigente antes de cerrar la trazabilidad o declarar cumplimiento. La descripción de este README no sustituye al enunciado oficial.

## Índice

- [Fases F0–F6](#fases-f0-f6)
  - [F0 — Entrevista](#fase-f0)
  - [F1 — Motivación, capacidades y E2E](#fase-f1)
  - [F2 — Servicios](#fase-f2)
  - [F3 — DDD estratégico](#fase-f3)
  - [F4 — DDD táctico](#fase-f4)
  - [F5 — Contextos delimitados](#fase-f5)
  - [F6 — Bounded Context Canvas](#fase-f6)
- [Vistas V01–V11](#vistas-v01-v11)
  - [V01 — Motivación](#vista-v01)
  - [V02 — Capacidades](#vista-v02)
  - [V03 — Cadena de valor y E2E](#vista-v03)
  - [V04 — Servicios](#vista-v04)
  - [V05 — Dominios](#vista-v05)
  - [V06 — Agregados, comandos y eventos](#vista-v06)
  - [V07 — Lenguaje ubicuo](#vista-v07)
  - [V08 — Contextos](#vista-v08)
  - [V09 — Interoperabilidad](#vista-v09)
  - [V10 — Trazabilidad](#vista-v10)
  - [V11 — Bounded Context Canvas](#vista-v11)
- [Alcance y reglas](#alcance-y-reglas)
- [Servicios y contratos](#servicios-y-contratos)
- [Lenguaje ubicuo](#lenguaje-ubicuo)
- [Decisiones y supuestos](#decisiones-y-supuestos)
- [Trazabilidad](#trazabilidad)
- [Aportes del equipo](#aportes-del-equipo)
- [Modelo y exportaciones](#modelo-y-exportaciones)
- [Checklist de entrega](#checklist-de-entrega)
- [Principios de documentación](#principios-de-documentación)

<a id="fases-f0-f6"></a>

## Fases F0–F6

Checklist de avance académico. Las casillas se marcarán solo cuando el equipo valide los entregables y su evidencia.

- [ ] **F0 — Entrevista al experto:** guion, instrucción de rol, conversación completa autorizada y análisis de hallazgos del equipo.
- [ ] **F1 — Motivación, capacidades y proceso E2E:** modelo del negocio, capacidades impactadas, motivación y proceso de extremo a extremo.
- [ ] **F2 — Descomposición de servicios:** capas de servicios, inclusión/exclusión justificada, interoperabilidad y contratos Contract First.
- [ ] **F3 — DDD estratégico:** dominios clasificados y lenguaje ubicuo validado.
- [ ] **F4 — DDD táctico:** entidades y objetos de valor, agregados con límites e invariantes, comandos y eventos por dominio.
- [ ] **F5 — Mapa de contextos delimitados:** contextos, relaciones y patrones documentados.
- [ ] **F6 — Bounded Context Canvas:** Canvas del contexto principal, completo y coherente con el modelo.

### <a id="fase-f0"></a>F0 — Entrevista al experto del negocio

**Objetivo:** comprender el negocio mediante preguntas, registrar la conversación autorizada y analizar qué hallazgos acepta, descarta o contrasta el equipo. La IA puede aportar conocimiento del negocio durante la entrevista; no debe producir los artefactos de diseño evaluados.

**Evidencia:** PENDIENTE. No se encontraron archivos de entrevista autorizados en el árbol actual.
**Explicación y análisis:** PENDIENTE.
**Justificación y validación:** PENDIENTE.
**Relaciones y trazabilidad:** conectar hallazgos validados con las fases y vistas correspondientes, PENDIENTE.
**Estado:** PENDIENTE.

### <a id="fase-f1"></a>F1 — Motivación, capacidades y proceso E2E

**Objetivo:** representar por qué se requiere la aplicación, las capacidades de negocio relevantes y la ubicación del proceso E2E.
**Evidencia:** diagramas V01–V03 están presentes estructuralmente en el modelo; revisión del equipo y exportaciones PNG PENDIENTES.
**Explicación, justificación y relaciones entre vistas:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

### <a id="fase-f2"></a>F2 — Descomposición de servicios

**Objetivo:** descomponer el proceso E2E en servicios, justificar inclusiones y exclusiones, documentar interoperabilidad y aplicar Contract First. El requisito registrado para el curso indica al menos cuatro capas; confirmar vigencia con el enunciado oficial.
**Evidencia:** V04 está presente estructuralmente en el modelo; matriz y contratos PENDIENTES.
**Explicación, justificación y trazabilidad:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

### <a id="fase-f3"></a>F3 — DDD estratégico

**Objetivo:** analizar el ecosistema, identificar y justificar dominios y sus clasificaciones, y acordar lenguaje ubicuo.
**Evidencia:** V05 y V07 están presentes estructuralmente en el modelo; glosario validado PENDIENTE.
**Explicación, justificación y relaciones:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

### <a id="fase-f4"></a>F4 — DDD táctico

**Objetivo:** documentar entidades y objetos de valor, límites e invariantes de agregados, y diagramas de comandos y eventos para cada dominio identificado por el equipo.
**Evidencia:** V06 está presente estructuralmente en el modelo; revisión del número y alcance de diagramas PENDIENTE.
**Explicación, justificación y relaciones:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

### <a id="fase-f5"></a>F5 — Mapa de contextos delimitados

**Objetivo:** documentar contextos delimitados, relaciones entre ellos y patrones de integración coherentes con las decisiones del equipo.
**Evidencia:** V08 y V09 están presentes estructuralmente en el modelo; validación PENDIENTE.
**Explicación, justificación y relaciones:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

### <a id="fase-f6"></a>F6 — Bounded Context Canvas

**Objetivo:** documentar el contexto principal en un Canvas de una página, con decisiones y supuestos justificados por el equipo.
**Evidencia:** V11 está presente estructuralmente en el modelo; revisión del contenido y de la herramienta PENDIENTE.
**Explicación, justificación y relaciones:** PENDIENTES.
**Estado:** PENDIENTE de validación académica.

<a id="vistas-v01-v11"></a>

## Vistas V01–V11

Checklist de vistas; la casilla permanece pendiente hasta que el equipo revise el contenido y la exportación correspondiente.

- [ ] V01 — Motivación.
- [ ] V02 — Mapa de capacidades.
- [ ] V03 — Cadena de valor y proceso E2E.
- [ ] V04 — Descomposición de servicios.
- [ ] V05 — Dominios.
- [ ] V06 — Agregados, comandos y eventos por dominio.
- [ ] V07 — Lenguaje ubicuo.
- [ ] V08 — Mapa de contextos delimitados.
- [ ] V09 — Interoperabilidad y anticorrupción.
- [ ] V10 — Trazabilidad vertical.
- [ ] V11 — Bounded Context Canvas.

El archivo [`modelo/recaudo-multimodal.archimate`](modelo/recaudo-multimodal.archimate) contiene diagramas cuyo nombre corresponde a V1–V11. La lista siguiente registra su presencia en el XML; no acredita que el contenido sea correcto, que corresponda a la versión vigente del enunciado ni que haya sido aprobado por el equipo. No hay exportaciones PNG en el árbol actual.

### <a id="vista-v01"></a>V01 — Motivación

**Objetivo:** explicar la razón empresarial para la aplicación y sus relaciones motivacionales.
**Evidencia:** diagrama `V1 · Motivación: de los interesados a los requerimientos` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v02"></a>V02 — Mapa de capacidades

**Objetivo:** representar capacidades del negocio e identificar las impactadas, según validación del equipo.
**Evidencia:** diagrama `V2 · Mapa de capacidades del negocio` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v03"></a>V03 — Cadena de valor y proceso E2E

**Objetivo:** situar la aplicación dentro de la cadena de valor y el proceso de extremo a extremo.
**Evidencia:** diagrama `V3 · Cadena de valor y proceso E2E: dónde se ubica la aplicación` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v04"></a>V04 — Descomposición de servicios

**Objetivo:** documentar capas, alcance, inclusión/exclusión e interoperabilidad del proceso E2E.
**Evidencia:** diagrama `V4 · Descomposición de servicios: seis capas, alcance y contratos` en el modelo; PNG PENDIENTE. La mención de seis capas es solo el título guardado en el modelo y requiere validación.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v05"></a>V05 — Dominios

**Objetivo:** documentar dominios y justificar su clasificación a partir del entendimiento del negocio.
**Evidencia:** diagrama `V5 · Dominios y su clasificación` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v06"></a>V06 — Agregados, comandos y eventos por dominio

**Objetivo:** mostrar, para cada dominio que acuerde el equipo, agregados con límites/invariantes y sus comandos y eventos.
**Evidencia:** diagrama `V6 · Agregados, comandos y eventos: un diagrama por dominio` en el modelo; PNG PENDIENTE. La cobertura por dominio debe verificarse.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v07"></a>V07 — Lenguaje ubicuo

**Objetivo:** registrar términos y significados validados por contexto.
**Evidencia:** diagrama `V7 · Lenguaje ubicuo: glosario por contexto y palabras con varios significados` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v08"></a>V08 — Mapa de contextos delimitados

**Objetivo:** documentar contextos y relaciones acordadas por el equipo.
**Evidencia:** diagrama `V8 · Mapa de contextos delimitados` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v09"></a>V09 — Interoperabilidad y anticorrupción

**Objetivo:** documentar intercambios con procesos, sistemas u organizaciones externas y los mecanismos acordados por el equipo.
**Evidencia:** diagrama `V9 · Interoperabilidad y anticorrupción` en el modelo; PNG PENDIENTE.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v10"></a>V10 — Trazabilidad vertical

**Objetivo:** relacionar metas y requisitos con elementos de las capas pertinentes, según el diseño validado.
**Evidencia:** diagrama `V10 · Trazabilidad vertical: de cada requerimiento a sus componentes (REQ01-REQ12)` en el modelo; PNG PENDIENTE. Los identificadores del título requieren verificación con el enunciado vigente.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

### <a id="vista-v11"></a>V11 — Bounded Context Canvas

**Objetivo:** documentar en una página el contexto seleccionado, sus decisiones y supuestos, de acuerdo con el enunciado vigente.
**Evidencia:** diagrama `V11 · Bounded Context Canvas: Tarifas y transbordos` en el modelo; PNG PENDIENTE. El contexto indicado por el título requiere aprobación del equipo.
**Explicación:** PENDIENTE. **Justificación:** PENDIENTE. **Relaciones/trazabilidad:** PENDIENTE.
**Estado:** presente estructuralmente; revisión del equipo PENDIENTE.

<a id="alcance-y-reglas"></a>

## Alcance y reglas

| Elemento | Regla, evidencia o decisión validada | Fuente/estado |
|---|---|---|
| Reglas de negocio | PENDIENTE de entrevista y validación del equipo | PENDIENTE |
| Inclusión de servicios | PENDIENTE; justificar cada servicio incluido | PENDIENTE |
| Exclusión de servicios | PENDIENTE; justificar cada exclusión | PENDIENTE |
| Límites del sistema y actores | PENDIENTE de validar con el enunciado y el equipo | PENDIENTE |

<a id="servicios-y-contratos"></a>

## Servicios y contratos

**Contract First:** contratos por definir cuando el equipo valide los servicios y sus consumidores/proveedores.

| Servicio/versión | Propósito | Consumidor/proveedor | Operaciones y esquemas | Errores, reglas y seguridad | Estado |
|---|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

<a id="lenguaje-ubicuo"></a>

## Lenguaje ubicuo

| Término | Definición acordada | Contexto | Ambigüedades/ejemplos | Fuente y validación |
|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

<a id="decisiones-y-supuestos"></a>

## Decisiones y supuestos

No se registran decisiones del equipo en esta entrega. Completar la tabla con autoría, fecha y evidencia verificables; distinguir decisiones acordadas de supuestos aún por validar.

| ID | Decisión o supuesto | Alternativas/forma de validación | Responsable y fecha | Evidencia | Estado |
|---|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

<a id="trazabilidad"></a>

## Trazabilidad

| Meta/requisito y fuente | Capacidad | Servicio | Componente | Vista/evidencia | Brecha/estado |
|---|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

<a id="aportes-del-equipo"></a>

## Aportes del equipo

Atribuir aportes usando commits, revisiones u otra evidencia acordada por el equipo. Un commit acredita un cambio en el repositorio, no necesariamente toda la participación académica.

| Integrante | Aporte/artefacto | Commit/revisión | Fecha | Evidencia y validación |
|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

<a id="modelo-y-exportaciones"></a>

## Modelo y exportaciones

El modelo canónico es [`modelo/recaudo-multimodal.archimate`](modelo/recaudo-multimodal.archimate). Se conserva el archivo existente sin cambios de contenido. El equipo debe revisar el modelo en Archi y comprobar compatibilidad, consistencia, semántica y correspondencia con el enunciado vigente antes de marcarlo como validado.

Exportar las vistas PNG desde este modelo y añadir solo archivos reales. No hay exportaciones PNG incorporadas actualmente; este README no enlaza imágenes inexistentes. Mantener los nombres V01–V11 y registrar qué versión del modelo produjo cada exportación.

<a id="checklist-de-entrega"></a>


## Checklist de entrega

- [ ] Entrevista documentada y analizada con autorización.
- [ ] Modelo ArchiMate único validado por el equipo.
- [ ] Todas las vistas exportadas desde el modelo.
- [ ] Decisiones arquitectónicas justificadas con evidencia.
- [ ] Contratos de servicios documentados.
- [ ] Tabla de aportes verificable.
- [x] README con índice navegable.
- [x] Repositorio publicado en GitHub.
- [ ] Sustentación preparada.
- [ ] Sustentación grabada en Teams.

<a id="principios-de-documentación"></a>

## Principios de documentación

- Mantener este README como única fuente documental del repositorio.
- Escribir en español técnico y claro.
- Identificar explícitamente todo lo pendiente.
- No declarar terminado un entregable sin revisión y evidencia.
- No generar con IA mapas de capacidades, dominios, agregados, contextos ni vistas evaluadas.
- Proteger entrevistas, datos personales y materiales académicos privados; incorporar solo archivos autorizados.
