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

<!-- IMAGEN REQUERIDA: foto del integrante en assets/img/perfil-<apellido>.jpg (formato
     cuadrado, aproximadamente 400x400 px) -->

| | |
|---|---|
| <img src="../assets/img/perfil-integrante.jpg" width="130"> | **<!-- COMPLETAR: Apellidos y Nombres -->**<br>Código: <!-- COMPLETAR --><br>Carrera: Ingeniería de Software<br><br><!-- COMPLETAR: párrafo de resumen con los principales conocimientos técnicos y habilidades que aportas al equipo. Sé concreto: lenguajes, frameworks, herramientas y experiencias previas relevantes. --> |

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

> **PENDIENTE — cifra oficial.** Incorporar aquí la cifra de notificaciones de accidentes de
> trabajo del último boletín del MTPE, con su año y fuente citada. Se descarga en
> https://www.gob.pe/institucion/mtpe/informes-publicaciones/292368-boletin-estadistico-notificaciones-de-accidentes-de-trabajo
> y el dataset abierto está en
> https://www.datosabiertos.gob.pe/dataset/notificaciones-de-accidentes-de-trabajo-mortales-fuente-registro-%C3%BAnico-de-accidentes-de
> Buscar: total de notificaciones del año, accidentes mortales y los dos o tres sectores de
> mayor incidencia. No usar cifras aproximadas ni de memoria: el dato tiene que ser verificable.

**Objetivos del proyecto**

| # | Objetivo |
|---|---|
| O1 | Reducir el tiempo entre la detección de un peligro y su registro formal a menos de un minuto de trabajo del operario. |
| O2 | Garantizar que ningún reporte se pierda por falta de conectividad en obra, mina o planta. |
| O3 | Dar al comité de SST trazabilidad completa del hallazgo: quién reportó, quién fue asignado, qué se hizo y cuándo se cerró. |
| O4 | Mantener la matriz IPERC alimentada por hallazgos reales de campo y no solo por revisiones periódicas. |
| O5 | Producir, en un clic, la evidencia documental que una inspección de SUNAFIL requiere. |

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

