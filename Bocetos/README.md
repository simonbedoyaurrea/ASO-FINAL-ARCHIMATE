# Bocetos

Bocetos visuales de apoyo al modelo canónico de `CHANDA`. **`V8-boceto-04.pdf`**, con fuente SVG y PNG del mismo nombre, es una referencia de composición de seis contextos, no una exportación actual de V8. El modelo editable prevalece; las versiones anteriores son borradores superados.

## V10 y V11 — bocetos e implementación

- **V10 vigente, 03:** [PDF](V10-boceto-03.pdf) · [PNG](V10-boceto-03.png) · [SVG](V10-boceto-03.svg). Una meta compartida, cinco columnas de detalle y seis cadenas. Fondo de Archi sin panel blanco de fondo.
- **V11 vigente, 04:** [PDF](V11-boceto-04.pdf) · [PNG](V11-boceto-04.png) · [SVG](V11-boceto-04.svg). Trece tarjetas, dos colaboraciones principales y consultas resumidas. Sin nubes, pergamino, lupa ni panel blanco de fondo.
- [Análisis, fuentes, cobertura y decisiones](Analisis-V10-V11.md).
- Generador vigente: `compactar_v10_v11.py` (reutiliza primitivas de `generar_v10_v11.py`). Produce únicamente artefactos en esta carpeta; no modifica ArchiMate. La versión 01 es un antecedente descartado de presentación, no la versión a revisar.
- Integración: `implementar_v10_v11.py`. Añade/regenera únicamente V10 y V11 en el modelo principal, conservando literalmente V2 y V8.
- Verificación: `verificar_v10_v11.py`, con resultados en `V10-V11-verificacion.json`. El modelo `modelo/V10-V11-qa.xml` es únicamente un ensayo semántico aislado; abrir normalmente `modelo/recaudo_tema4.archimate`.

Ambas vistas ya están implementadas con elementos y conexiones editables. La revisión semántica aislada pasó sin incidencias; no se atribuye una validación de entrevista inexistente en esta copia. Las imágenes `*-archi-mcp.png` son diagnósticos del renderizador MCP: no muestran fielmente todos los rótulos/figuras alternativas de la aplicación Archi.
