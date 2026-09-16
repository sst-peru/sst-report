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

### 8.1.4. Question Backlog

Priorización por el criterio de mayor incertidumbre combinada con mayor costo de equivocarse.

| Prioridad | ID | Pregunta | Incertidumbre | Costo de equivocarse | Puntaje |
|---|---|---|---|---|---|
| 1 | Q1 | Fricción del formulario | Alta | Alto | 9 |
| 2 | Q4 | Captura frente a capacidad de cierre | Alta | Alto | 9 |
| 3 | Q2 | Peso real del uso sin conexión | Media | Alto | 6 |
| 4 | Q3 | Foto obligatoria | Media | Medio | 4 |
| 5 | Q5 | Reporte anónimo | Alta | Bajo | 3 |

La pregunta Q1 encabeza el backlog y es la que se somete a experimento en este ciclo.

### 8.1.5. Experiment Cards

**Experiment Card — EXP-01**

| Campo | Contenido |
|---|---|
| **Pregunta** | Q1: ¿Un formulario de tres pasos aumenta el número de reportes por usuario frente al formulario tradicional de diez o más campos? |
| **Hipótesis** | Creemos que el grupo expuesto al formulario rápido registrará al menos el doble de reportes por usuario que el grupo expuesto al formulario largo, durante la ventana de medición |
| **Método** | Experimento controlado A/B con asignación determinística por usuario |
| **Variable independiente** | Variante del formulario de reporte: `rapido` o `largo` |
| **Variable dependiente** | Número de reportes por usuario en la ventana de medición |
| **Variables controladas** | El resto de la aplicación es idéntico para ambos grupos: mismo acceso, misma lista, misma operación sin conexión, mismo API |
| **Participantes** | Operarios de campo con cuenta activa |
| **Duración** | 14 días |
| **Criterio de éxito** | Diferencia estadísticamente significativa (α = 0.05) a favor del grupo `rapido` |
| **Criterio de refutación** | Ausencia de diferencia significativa, o diferencia a favor del formulario largo |
| **Decisión asociada** | Si se confirma, el flujo rápido se convierte en el único formulario del producto. Si se refuta, se elimina la variante, se conserva el formulario simple por coherencia de diseño y la inversión se redirige hacia la barrera que las entrevistas señalen como dominante |

**Experiment Card — EXP-02 (siguiente ciclo)**

| Campo | Contenido |
|---|---|
| **Pregunta** | Q4: ¿El aumento de reportes se traduce en hallazgos cerrados o solo en cola acumulada? |
| **Hipótesis** | Creemos que un aumento del volumen de reportes sin cambios en el proceso de cierre incrementará el MTTR |
| **Método** | Análisis observacional de la serie temporal de MTTR frente al volumen de reportes |
| **Medida** | MTTR semanal y número de hallazgos abiertos al cierre de cada semana |
| **Decisión asociada** | Si el MTTR se deteriora, priorizar funcionalidades de capacidad de respuesta (notificaciones, asignación automática) antes que funcionalidades de captura |

## 8.2. Experiment Design

### 8.2.1. Hypotheses

**Hipótesis nula (H₀).** No existe diferencia en la media de reportes por usuario entre el grupo
expuesto al formulario rápido y el expuesto al formulario largo.

> H₀: μ_rápido = μ_largo

**Hipótesis alterna (H₁).** La media de reportes por usuario del grupo expuesto al formulario
rápido es distinta de la del grupo expuesto al formulario largo.

> H₁: μ_rápido ≠ μ_largo

Se plantea la prueba **a dos colas** aunque la hipótesis de negocio sea direccional. La razón es
metodológica: un formulario más corto podría, en principio, producir reportes de menor calidad y
desalentar su uso al percibirse como poco serio. Cerrar esa posibilidad por anticipado sería
diseñar el experimento para confirmar lo que ya se cree.

### 8.2.2. Domain Business Metrics

| Métrica de negocio | Definición | Por qué importa |
|---|---|---|
| **Frecuencia de reporte** | Reportes creados por usuario activo en el periodo | Mide si el sistema captura lo que ocurre en campo; es la entrada de todo el resto |
| **MTTR de hallazgos** | Horas promedio entre la creación del reporte y su cierre | Mide la capacidad de respuesta: cuánto tiempo permanece expuesto el peligro |
| **Tasa de cumplimiento de inspecciones** | Inspecciones realizadas sobre programadas | Mide la disciplina preventiva, no solo la reactiva |
| **Tasa de cierre** | Hallazgos cerrados sobre hallazgos creados en el periodo | Detecta si la captura crece más rápido que la capacidad de atención |
| **Cobertura de evidencia** | Proporción de hallazgos con foto y con acción correctiva registrada | Mide la calidad del expediente ante una fiscalización |

### 8.2.3. Measures

| Medida | Operacionalización | Origen del dato |
|---|---|---|
| Reportes por usuario | Conteo de `Report` por `reported_by`, dividido entre los usuarios de la variante | `experiments/report_form/results/` |
| Variante asignada | Campo `form_variant` almacenado en cada reporte y `Assignment` del usuario | Base de datos |
| Reportes con foto | Conteo de reportes con `photo` no nulo | `experiments/report_form/results/` |
| MTTR por variante | Promedio de `closed_at − created_at` de los reportes cerrados de cada grupo | `experiments/report_form/results/` |
| Serie diaria | Conteo de reportes por día y variante | `experiments/report_form/results/` (campo `daily`) |
| Reportes sincronizados offline | Conteo de reportes con `synced_offline` verdadero | Base de datos |

Todas las medidas se obtienen del propio sistema. No se emplea una herramienta de analítica
externa, decisión justificada en el Capítulo VII: los eventos de una herramienta externa se
pierden cuando no hay conectividad, que es exactamente la condición de uso del producto.

### 8.2.4. Conditions

| Condición | Definición |
|---|---|
| **Unidad de asignación** | El usuario. No la sesión ni el reporte: si un mismo operario viera formularios distintos, la comparación dejaría de medir el formulario |
| **Mecanismo de asignación** | Hash SHA-256 estable de `clave_del_experimento + id_de_usuario`, con módulo sobre el número de variantes |
| **Grupo de control** | Variante `largo`: formulario tradicional con todos los campos visibles y obligatorios |
| **Grupo de tratamiento** | Variante `rapido`: asistente de tres pasos con foto y descripción opcional |
| **Elementos controlados** | Acceso, navegación, lista de reportes, operación sin conexión, API y permisos son idénticos en ambos grupos |
| **Criterio de inclusión** | Usuarios con rol operario y cuenta activa durante toda la ventana |
| **Criterio de exclusión** | Usuarios creados para pruebas o demostración; usuarios con rol de gestión |
| **Ventana de medición** | 14 días corridos, iniciando el mismo día para ambos grupos |
| **Contaminación** | No hay comunicación entre variantes dentro de la aplicación; el riesgo residual es que dos operarios comparen sus pantallas entre sí, lo que se registra como amenaza a la validez |

**Por qué la asignación es determinística y no aleatoria.** Un `random()` produciría una
asignación distinta en cada consulta, de modo que un mismo usuario podría ver un formulario
distinto cada día. El hash estable garantiza tres propiedades necesarias: el usuario conserva su
variante durante todo el experimento, la aplicación puede recalcularla sin conexión, y la
asignación es reproducible por un tercero que quiera auditar los resultados.

### 8.2.5. Scale Calculations and Decisions

**Parámetros del diseño**

| Parámetro | Valor | Justificación |
|---|---|---|
| Nivel de significancia (α) | 0.05, dos colas | Estándar del curso: minimiza los errores atribuibles al azar (Tipo I) |
| Potencia estadística (1 − β) | 0.80 | Rango recomendado de 80 % a 95 %; con 80 % se acota la probabilidad de error Tipo II a 20 % |
| Efecto mínimo detectable (MDE) | +100 % | Es la magnitud que afirma la hipótesis de negocio ("el doble") |
| Ventana de medición | 14 días | Suficiente para cubrir dos ciclos semanales de trabajo, incluidos los turnos de fin de semana |
| Tasa base supuesta | 0.15 reportes por usuario y por día | **Supuesto a calibrar con el piloto.** Equivale a un reporte cada siete días por operario |

**Modelo estadístico.** Se compara la media de reportes por usuario entre dos grupos
independientes mediante la aproximación normal para diferencia de medias:

> n por grupo = 2 · (Z(α/2) + Z(β))² · σ² / Δ²

Se asume que el conteo de reportes por usuario sigue aproximadamente una distribución de
Poisson, por lo que la varianza se estima igual a la media. Es una aproximación declarada: si la
dispersión real resulta mayor —algo frecuente en conteos de comportamiento humano, donde unos
pocos usuarios concentran la mayoría de los reportes—, el tamaño requerido será mayor y debe
recalcularse con la varianza observada.

**Resultados del cálculo**

El cálculo es reproducible ejecutando `python tools/tamano-muestra.py` en el repositorio del
informe. Con una media esperada de 2.10 reportes por usuario en el control y 4.20 en el
tratamiento:

| Potencia | Usuarios por grupo | Total |
|---|---|---|
| 80 % | 12 | **24** |
| 90 % | 16 | 32 |
| 95 % | 19 | 38 |

**Efecto mínimo detectable según la muestra disponible**

Este es el análisis que determina si el experimento puede ejecutarse con los participantes que
realmente se consigan:

| Usuarios por grupo | Total | Solo se podrían detectar efectos de |
|---|---|---|
| 3 | 6 | +232 % o mayores |
| 5 | 10 | +166 % o mayores |
| 8 | 16 | +123 % o mayores |
| 12 | 24 | +97 % o mayores |
| 20 | 40 | +72 % o mayores |

**Decisión de escala y su consecuencia honesta.** El diseño requiere **24 participantes** para
detectar el efecto que la hipótesis afirma, con α = 0.05 y potencia del 80 %. Si el piloto se
ejecuta con menos participantes —por ejemplo, seis—, el experimento queda **subpotenciado**: solo
podría detectar un efecto superior al 232 %, muy por encima del que se busca. En ese escenario,
un resultado no significativo **no permite concluir que el formulario no funciona**, y debe
reportarse explícitamente como una limitación del estudio y no como una refutación de la
hipótesis. Esta distinción es la diferencia entre un experimento y una demostración.

> **PENDIENTE.** Consignar aquí el número real de participantes reclutados y recalcular el
> efecto mínimo detectable con esa cifra antes de interpretar cualquier resultado.

