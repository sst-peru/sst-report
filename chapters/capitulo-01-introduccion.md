# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

<!-- COMPLETAR: nombre del startup. Reemplazar [NOMBRE DEL STARTUP] en todo el documento. -->

**[NOMBRE DEL STARTUP]** es una startup de software peruana dedicada a llevar la gestión de
la seguridad y salud en el trabajo del papel al dato en tiempo real. Nace de una observación
concreta: en la mayoría de empresas medianas y pequeñas del país el sistema de gestión de SST
existe formalmente —hay matriz IPERC, hay comité, hay registros— pero funciona con semanas de
retraso respecto de lo que realmente ocurre en el frente de trabajo.

**Misión.** Reducir el tiempo entre que un trabajador detecta un peligro y la persona que puede
corregirlo se entera, entregando a las empresas peruanas herramientas que hagan del cumplimiento
de la Ley N° 29783 una consecuencia de operar bien, y no un trámite que se resuelve el día antes
de una inspección.

**Visión.** Ser la plataforma de referencia para la gestión operativa de SST en la mediana
empresa peruana, en los sectores donde el riesgo es alto y la digitalización es baja:
construcción, manufactura, minería de menor escala y logística.

**Producto.** *Resguardo*, un sistema de gestión de SST compuesto por una aplicación móvil
Android para el trabajador de campo, un panel web para el supervisor y el comité de SST, y una
API REST que ambos consumen.

### 1.1.2. Perfiles de integrantes del equipo

<!-- IMAGEN REQUERIDA: una foto por integrante, cuadrada y de aproximadamente 400x400 px, en
     assets/img/perfil-1.jpg, perfil-2.jpg y perfil-3.jpg -->

**Integrante 1**

| | |
|---|---|
| <img src="../assets/img/perfil-1.jpg" width="130"> | **<!-- COMPLETAR: Apellidos y Nombres -->**<br>**Código:** <!-- COMPLETAR --><br>**Carrera:** <!-- COMPLETAR --><br><br><!-- COMPLETAR: párrafo de resumen. Indicar los principales conocimientos técnicos y habilidades que aporta al equipo, siendo concreto: lenguajes, frameworks, herramientas y experiencias previas relevantes. --> |

**Integrante 2**

| | |
|---|---|
| <img src="../assets/img/perfil-2.jpg" width="130"> | **<!-- COMPLETAR: Apellidos y Nombres -->**<br>**Código:** <!-- COMPLETAR --><br>**Carrera:** <!-- COMPLETAR --><br><br><!-- COMPLETAR: párrafo de resumen con los conocimientos técnicos y habilidades que aporta al equipo. --> |

**Integrante 3**

| | |
|---|---|
| <img src="../assets/img/perfil-3.jpg" width="130"> | **<!-- COMPLETAR: Apellidos y Nombres -->**<br>**Código:** <!-- COMPLETAR --><br>**Carrera:** <!-- COMPLETAR --><br><br><!-- COMPLETAR: párrafo de resumen con los conocimientos técnicos y habilidades que aporta al equipo. --> |

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática

La Ley N° 29783, Ley de Seguridad y Salud en el Trabajo, y su reglamento, el D.S. N° 005-2012-TR,
obligan a toda empresa peruana a implementar un Sistema de Gestión de Seguridad y Salud en el
Trabajo. Ese sistema incluye, como mínimo, un comité de SST —o un supervisor cuando la empresa
tiene menos de veinte trabajadores—, una matriz IPERC de identificación de peligros y evaluación
de riesgos, el registro de actos y condiciones inseguras, el control de entrega de equipos de
protección personal y un programa de inspecciones periódicas.

En la práctica, en la mediana y pequeña empresa ese sistema opera así:

1. Un trabajador detecta una condición peligrosa —una escalera rota, un cable expuesto, un piso
   mojado sin señalizar— pero **no tiene una forma simple de reportarla**. Debe llenar un
   formato en papel, o avisar verbalmente a su jefe inmediato, que puede olvidarlo.
2. Cuando el reporte sí se registra, **queda en una hoja de cálculo o en un cuaderno físico**,
   sin hora exacta, sin fotografía y sin ubicación.
3. La matriz IPERC, que debería alimentarse de lo que ocurre en campo, **se actualiza en
   revisiones esporádicas**, a veces con meses de diferencia respecto de los hechos.
4. Ante una inspección de SUNAFIL, la empresa **no puede evidenciar** que gestiona sus riesgos:
   tiene los documentos, pero no la trazabilidad entre el hallazgo, la acción correctiva y su
   verificación.
5. Cuando ocurre un accidente grave, se descubre que el peligro **ya había sido advertido** y
   que nadie le hizo seguimiento.

El problema, resumido: **el dato de seguridad existe en la cabeza de los trabajadores o en
papel, pero no fluye a tiempo hacia quien puede actuar.**

**Objetivos del proyecto**

| # | Objetivo |
|---|---|
| O1 | Reducir a menos de un minuto de trabajo del operario el tiempo entre la detección de un peligro y su registro formal, incluso sin conectividad en obra, mina o planta. |
| O2 | Dar al comité de SST trazabilidad completa del hallazgo: quién reportó, quién fue asignado, qué se hizo y cuándo se cerró. |
| O3 | Mantener la matriz IPERC alimentada por hallazgos reales de campo y no solo por revisiones periódicas. |
| O4 | Producir, en un clic, la evidencia documental que una inspección de SUNAFIL requiere. |

**Restricciones y alcance**

| # | Restricción |
|---|---|
| R1 | La aplicación móvil se desarrolla para Android nativo. iOS queda fuera del alcance por la distribución de dispositivos del segmento objetivo. |
| R2 | El producto cubre la gestión operativa del SGSST; no incluye vigilancia médica ocupacional ni exámenes médicos ocupacionales (EMO). |
| R3 | El experimento del curso se limita a una hipótesis sobre el formulario de reporte; el resto de funcionalidades no forma parte del diseño experimental. |
| R4 | El desarrollo lo ejecuta un equipo de un integrante en un ciclo académico, lo que acota el alcance a un producto mínimo funcional y verificable. |

#### 1.2.1.1. The 5 'W's and 2 'H's

| Pregunta | Respuesta |
|---|---|
| **Who** (¿Quién?) | Trabajadores de campo (operarios) que detectan peligros; supervisores de SST y miembros del comité de SST que deben gestionarlos; la empresa, como sujeto obligado ante SUNAFIL. |
| **What** (¿Qué?) | El dato de seguridad —actos y condiciones inseguras, inspecciones, entregas de EPP, acuerdos del comité— no llega a tiempo ni de forma verificable a quien puede actuar sobre él. |
| **Where** (¿Dónde?) | En frentes de trabajo de empresas medianas y pequeñas peruanas: obras de construcción, plantas, almacenes y unidades mineras, donde además la conectividad es intermitente. |
| **When** (¿Cuándo?) | Desde la entrada en vigor de la Ley N° 29783 (2011) la obligación existe, pero el problema se manifiesta en el día a día: en cada turno en que se detecta un peligro y no se registra. |
| **Why** (¿Por qué?) | Porque el canal de reporte disponible —papel o aviso verbal— impone un costo de tiempo y fricción mayor que el beneficio percibido por el trabajador, y porque el registro resultante no es trazable ni auditable. |
| **How** (¿Cómo?) | Con una aplicación móvil que permite reportar en segundos con foto y geolocalización, funcionando sin conexión y sincronizando después, y un panel web donde el comité asigna, cierra y evidencia. |
| **How much** (¿Cuánto?) | El costo del problema se mide en dos dimensiones: el tiempo de exposición al riesgo mientras el peligro no se corrige (MTTR), y la exposición económica ante multas de SUNAFIL por no evidenciar la gestión del riesgo. <!-- COMPLETAR: rango de multas vigente según la escala de infracciones de SUNAFIL, citando la norma --> |

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

**Dominio.** Gestión operativa de la seguridad y salud en el trabajo en empresas peruanas
obligadas por la Ley N° 29783.

**Segmentos de clientes.**
- Trabajadores de campo (operarios) de empresas medianas y pequeñas de alto riesgo.
- Supervisores de SST y miembros del comité de SST de esas mismas empresas.

**Pain points.**
- Reportar un peligro cuesta más esfuerzo del que el trabajador está dispuesto a invertir.
- El registro en papel o en hoja de cálculo carece de fecha exacta, evidencia fotográfica y
  ubicación, por lo que no sirve como prueba ante una inspección.
- El comité de SST descubre los peligros tarde y no tiene forma de demostrar el seguimiento.
- La matriz IPERC envejece y deja de reflejar los riesgos reales de la operación.

**Gap.** Las soluciones disponibles en el mercado están construidas alrededor del profesional de
SST y de sus obligaciones documentales, no alrededor del operario que detecta el peligro. El
formulario de reporte típico exige más de diez campos y presupone conectividad permanente.

**Visión / estrategia.** Convertir al trabajador de campo en el sensor principal del sistema de
gestión, bajando la fricción del reporte hasta que reportar sea más barato que no reportar, y
usando ese flujo de datos para mantener vivo el resto del sistema.

**Segmento inicial.** Empresas constructoras medianas de Lima Metropolitana, de entre 20 y 200
trabajadores, con comité de SST constituido y operaciones en obra.

#### 1.2.2.2. Lean UX Assumptions

**Business assumptions**

1. Creemos que nuestros clientes son empresas medianas obligadas por la Ley N° 29783 que ya
   tienen un comité de SST constituido.
2. Estos clientes pueden ser atendidos con una solución SaaS por suscripción mensual según
   número de trabajadores.
3. El valor principal que el cliente quiere de nuestro producto es reducir su exposición a
   sanciones y accidentes, evidenciando gestión real y no solo documentación.
4. El cliente también obtiene reducción del tiempo administrativo que hoy consume consolidar
   registros dispersos.
5. Conseguiremos la mayoría de clientes a través de consultoras de SST y de referencias en el
   sector construcción.
6. Haremos dinero mediante suscripción mensual por empresa, escalonada por número de
   trabajadores activos.
7. Nuestra competencia principal en el mercado son plataformas SST orientadas al profesional de
   salud ocupacional, como SELERIA y GISSAT.
8. Los venceremos por la experiencia del operario en campo: reporte en segundos y operación sin
   conexión.
9. El mayor riesgo del producto es que los trabajadores no adopten la aplicación y el sistema
   quede tan vacío como el cuaderno que reemplaza.
10. Resolveremos esto midiendo la adopción como métrica de producto desde el primer día, y
    experimentando sobre la fricción del formulario de reporte.

**User assumptions**

| Pregunta | Supuesto |
|---|---|
| ¿Quién es el usuario? | El operario de campo, con casco y guantes, que usa su propio celular de gama media o baja. |
| ¿Dónde encaja el producto en su trabajo? | En el momento exacto en que ve el peligro, sin interrumpir su tarea más de un minuto. |
| ¿Qué problemas tiene? | Reportar le cuesta tiempo, no ve resultado de haber reportado antes, y a veces teme la reacción del supervisor. |
| ¿Cuándo y cómo lo usa? | De pie, con una mano, en exteriores, con conectividad intermitente. |
| ¿Qué funcionalidades son importantes? | Tomar foto, elegir el tipo de peligro y enviar. Todo lo demás es opcional. |
| ¿Cómo debe verse y comportarse? | Objetivos táctiles grandes, texto corto, confirmación inmediata de que el reporte quedó guardado. |

**Feature assumptions**

1. Creemos que un formulario de tres pasos aumentará la frecuencia de reportes de los operarios.
2. Creemos que guardar el reporte localmente antes de enviarlo evitará la pérdida de reportes en
   zonas sin cobertura.
3. Creemos que la fotografía obligatoria mejorará la capacidad del comité de priorizar sin ir al
   lugar.
4. Creemos que mostrar al operario el estado de sus reportes anteriores sostendrá la adopción en
   el tiempo.
5. Creemos que exportar la evidencia a Excel reducirá el tiempo de preparación ante una
   inspección de SUNAFIL.

#### 1.2.2.3. Lean UX Hypothesis Statements

**H1 — Fricción del reporte (hipótesis central del experimento)**

> **Creemos que** un aumento en la frecuencia de reportes de actos y condiciones inseguras
> **se logrará si** el operario de campo **obtiene** un flujo de reporte de tres a cuatro toques
> con fotografía **con** un formulario tipo asistente en lugar del formulario tradicional de
> diez o más campos.
> **Sabremos que** hemos tenido éxito **cuando** el grupo expuesto al formulario rápido registre
> una cantidad de reportes por usuario significativamente mayor que el grupo expuesto al
> formulario largo, durante el periodo de medición.

**H2 — Operación sin conexión**

> **Creemos que** la reducción de reportes perdidos **se logrará si** el operario **obtiene**
> la certeza de que su reporte quedó guardado **con** un almacenamiento local que sincroniza
> automáticamente al recuperar la señal.
> **Sabremos que** hemos tenido éxito **cuando** la proporción de reportes creados sin conexión
> que llegan al servidor sea cercana al total, sin duplicados.

**H3 — Trazabilidad del hallazgo**

> **Creemos que** una reducción del tiempo de cierre de hallazgos **se logrará si** el supervisor
> de SST **obtiene** visibilidad inmediata y asignación de responsable **con** un panel web que
> concentra los reportes en tiempo real.
> **Sabremos que** hemos tenido éxito **cuando** el MTTR de hallazgos disminuya respecto de la
> línea base del proceso en papel.

**H4 — Evidencia ante la autoridad**

> **Creemos que** una reducción del tiempo de preparación ante inspecciones **se logrará si**
> el responsable de SST **obtiene** los registros consolidados **con** exportaciones a Excel de
> reportes, IPERC, EPP, inspecciones y actas del comité.
> **Sabremos que** hemos tenido éxito **cuando** el tiempo declarado para armar el expediente se
> reduzca respecto del procedimiento manual actual.

#### 1.2.2.4. Lean UX Canvas

<!-- IMAGEN REQUERIDA: exportar el Lean UX Canvas desde UXPressia, Miro o Figma a
     assets/img/lean-ux-canvas.png -->

![Lean UX Canvas](../assets/img/lean-ux-canvas.png)

| Bloque | Contenido |
|---|---|
| **1. Business Problem** | Las empresas peruanas obligadas por la Ley N° 29783 no logran que el dato de seguridad fluya desde el frente de trabajo hasta quien puede actuar, lo que las expone a accidentes evitables y a sanciones por no evidenciar gestión del riesgo. |
| **2. Business Outcomes** | Aumento de reportes por trabajador activo; reducción del MTTR de hallazgos; aumento de la tasa de cumplimiento de inspecciones programadas; reducción del tiempo de preparación de evidencia. |
| **3. Users** | Operario de campo; supervisor de SST; miembro del comité de SST. |
| **4. User Outcomes & Benefits** | El operario reporta sin perder tiempo y ve que su reporte tuvo consecuencia. El supervisor deja de perseguir papeles y prioriza por severidad. El comité sustenta su gestión con evidencia trazable. |
| **5. Solutions** | App Android con reporte en tres pasos y operación sin conexión; panel web de seguimiento; matriz IPERC alimentada por hallazgos; control de EPP; programa de inspecciones; actas del comité; exportación de evidencia. |
| **6. Hypotheses** | Las hipótesis H1 a H4 de la sección anterior. |
| **7. What's the most important thing we need to learn first?** | Si la fricción del formulario es realmente el factor que determina la frecuencia de reporte del operario. |
| **8. What's the least amount of work to learn the next most important thing?** | Implementar las dos variantes del formulario tras una asignación determinística por usuario y comparar reportes por usuario entre ambos grupos. |

## 1.3. Segmentos objetivo

**Segmento 1 — Trabajador de campo (operario)**

Hombres y mujeres de entre 20 y 55 años que desempeñan labores operativas en obra, planta,
almacén o unidad minera. Usan teléfonos Android de gama media o baja como principal —y con
frecuencia único— dispositivo digital. Su jornada transcurre de pie, con equipos de protección
puestos, y su interacción con sistemas de la empresa se limita a marcar asistencia y firmar
formatos. Son quienes primero ven el peligro y, hoy, quienes menos herramientas tienen para
comunicarlo.

**Segmento 2 — Supervisor de SST y miembro del comité**

Profesionales o técnicos en seguridad, entre 25 y 50 años, responsables de que el sistema de
gestión funcione y de responder ante la autoridad. Trabajan con computadora y celular, manejan
hojas de cálculo y formatos, y dedican una parte sustancial de su tiempo a consolidar
información dispersa en lugar de a intervenir sobre el riesgo. Son el usuario que decide la
compra o la recomienda.
