# Capítulo VIII: Experiment-Driven Development

## 8.1. Experiment Planning

### 8.1.1. As-Is Summary

El producto implementado cubre el ciclo completo de gestión del SGSST: captura del hallazgo en
campo, seguimiento hasta el cierre, matriz IPERC, control de EPP, inspecciones periódicas,
comité con actas y acuerdos, indicadores y exportación de evidencia. Web y móvil consumen el
mismo API y ofrecen, para un mismo rol, las mismas capacidades.

Lo que el producto **todavía no sabe** es si su decisión de diseño más distintiva funciona. Todo
el planteamiento se apoya en una creencia: que la fricción del formulario es lo que determina
cuántas veces reporta un operario. Esa creencia gobierna la inversión de desarrollo más costosa
del proyecto —el flujo de tres pasos con operación sin conexión— y hasta ahora nadie la ha
puesto a prueba. Ese es el punto de partida del experimento.

