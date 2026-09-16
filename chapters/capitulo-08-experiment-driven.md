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

### 8.1.2. Raw Material: Assumptions, Knowledge Gaps, Ideas, Claims

**Assumptions (supuestos que damos por ciertos sin evidencia)**

| ID | Supuesto | Riesgo si es falso |
|---|---|---|
| A1 | La fricción del formulario es la principal barrera para reportar | La inversión en el flujo rápido no produce retorno |
| A2 | El operario está dispuesto a usar su celular personal para tareas de la empresa | La adopción no ocurre y el sistema queda vacío |
| A3 | El temor a represalias no es la barrera dominante | Reducir la fricción no cambia nada porque el problema es otro |
| A4 | Más reportes se traducen en más peligros corregidos | El sistema genera ruido en lugar de gestión |
| A5 | El supervisor tiene capacidad de atender el volumen adicional | Los hallazgos se acumulan y el MTTR empeora |

**Knowledge gaps (lo que no sabemos y necesitamos saber)**

| ID | Vacío de conocimiento |
|---|---|
| K1 | Cuántas veces reporta hoy un operario, en promedio, con el proceso en papel |
| K2 | Cuánto tiempo transcurre hoy entre la detección y la corrección de un peligro |
| K3 | Qué proporción de peligros detectados nunca llega a reportarse, y por qué |
| K4 | Si la foto obligatoria acelera o frena el reporte |
| K5 | Cuál es la capacidad real de cierre del equipo de SST por semana |

**Ideas (soluciones candidatas)**

| ID | Idea |
|---|---|
| I1 | Formulario tipo asistente de tres pasos con foto |
| I2 | Reporte anónimo opcional para eliminar el temor a represalias |
| I3 | Notificación al operario cuando su hallazgo se cierra |
| I4 | Reporte por voz para quien trabaja con guantes |
| I5 | Ranking de áreas por hallazgos cerrados, como incentivo colectivo |

**Claims (afirmaciones que el equipo sostiene y que deberían verificarse)**

| ID | Afirmación |
|---|---|
| C1 | "Un formulario de tres pasos duplicará la frecuencia de reporte" |
| C2 | "Sin operación offline, el sistema no sirve en obra ni en mina" |
| C3 | "La evidencia exportable es el argumento que cierra la venta" |

### 8.1.3. Experiment-Ready Questions

Una pregunta está lista para experimentar cuando es específica, medible y su respuesta cambia
una decisión.

| ID | Pregunta | ¿Qué decisión cambia? |
|---|---|---|
| Q1 | ¿Un formulario de tres pasos aumenta el número de reportes por usuario frente a uno de diez campos? | Si no, se simplifica el producto eliminando la variante y se invierte en otra barrera |
| Q2 | ¿Qué proporción de reportes se origina sin conexión? | Determina si la inversión en la cola local y la sincronización se justifica |
| Q3 | ¿La foto obligatoria reduce la tasa de finalización del reporte? | Decide si la foto se mantiene obligatoria u opcional |
| Q4 | ¿El aumento de reportes se traduce en más hallazgos cerrados o solo en más cola? | Decide si hay que trabajar sobre la capacidad de cierre antes de escalar la captura |
| Q5 | ¿La posibilidad de reportar de forma anónima aumenta los reportes de actos inseguros de terceros? | Decide si se implementa el reporte anónimo |

