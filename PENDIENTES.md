# Pendientes del informe

Este archivo **no forma parte del informe**: no se compila ni se incluye en el índice.
Recoge las tareas que antes aparecían como bloques PENDIENTE dentro de los capítulos,
para que el documento entregable quede limpio sin perder la lista de lo que falta.

## bibliografia.md

**PENDIENTE.** Agregar las fuentes estadísticas que se citen finalmente en los apartados 1.2.1
y 1.3 (INEI, OSIPTEL), y toda referencia que se incorpore al completar las secciones
pendientes. Verificar que cada obra listada esté efectivamente citada en el cuerpo del informe.

---

## capitulo-01-introduccion.md

**PENDIENTE — cifra oficial.** Incorporar aquí la cifra de notificaciones de accidentes de
trabajo del último boletín del MTPE, con su año y fuente citada. Se descarga en
https://www.gob.pe/institucion/mtpe/informes-publicaciones/292368-boletin-estadistico-notificaciones-de-accidentes-de-trabajo
y el dataset abierto está en
https://www.datosabiertos.gob.pe/dataset/notificaciones-de-accidentes-de-trabajo-mortales-fuente-registro-%C3%BAnico-de-accidentes-de
Buscar: total de notificaciones del año, accidentes mortales y los dos o tres sectores de
mayor incidencia. No usar cifras aproximadas ni de memoria: el dato tiene que ser verificable.

---

## capitulo-02-requirements-elicitation.md

**PENDIENTE — trabajo de campo.** Esta sección debe contener entrevistas reales, grabadas en
video y editadas en el video de evidencia. Por cada entrevistado se registra: nombre y
apellidos, edad, distrito de residencia, cargo, fecha de la entrevista, duración, enlace al
video con el minuto de inicio, y un resumen de entre 150 y 250 palabras de lo que respondió.

Mínimo recomendado: cuatro entrevistas por segmento. **Este contenido no puede redactarse sin
haber realizado las entrevistas**; inventarlo invalidaría todo el needfinding que se construye
encima, y es exactamente lo que el jurado verifica preguntando por los entrevistados.

Plantilla por entrevistado:

| Campo | Contenido |
|---|---|
| Nombre y apellidos | |
| Edad / Distrito | |
| Cargo y empresa | |
| Fecha y duración | |
| Enlace al video (con minuto) | |
| Resumen de la entrevista | |

---
**PENDIENTE.** Se completa después del registro. Estructura esperada: hallazgos por segmento,
cada uno con el porcentaje de entrevistados que lo manifestó, citas textuales breves que lo
respalden, y la conexión explícita con los supuestos del Lean UX que confirma o refuta. Los
supuestos refutados deben marcarse como tales: un needfinding que confirma todo lo que se
asumió antes de entrevistar suele significar que se preguntó mal.

---

## capitulo-04-product-design.md

**PENDIENTE — fuera del alcance de este ciclo.** La landing page se construye en un repositorio
aparte. Esta sección documenta su diseño previsto; las capturas se incorporan cuando esté
publicada.

---
**PENDIENTE.** Incorporar el mock-up cuando la landing page esté construida, junto con la URL
de su despliegue.

---

## capitulo-05-product-implementation.md

**PENDIENTE — despliegue.** Documentar aquí el despliegue real cuando esté hecho: proveedor
(Render, Railway, Fly.io o similar para el API; Vercel o Netlify para la web), URL pública de
cada entorno, y procedimiento de migración de base de datos en el despliegue.

---
**PENDIENTE — fuera del alcance de este ciclo.** La landing page no forma parte de la
aplicación web: se construye en un repositorio propio, por las razones expuestas en la sección
4.3. Al cierre de este sprint todavía no está implementada, de modo que no hay evidencia
que presentar aquí. La estructura prevista y las restricciones de contenido quedan
especificadas en 4.3.1.

---
**PENDIENTE — compilación.** Adjuntar evidencia de la compilación exitosa y el APK de
depuración generado por el pipeline, más capturas en dispositivo o emulador.

---
**PENDIENTE.** Incluir, por cada repositorio, la captura de los analíticos de colaboración y
una descripción de cómo se distribuyó el trabajo. El historial de commits debe ser coherente
con lo declarado en el Registro de Versiones del Informe y en el Participant Performance
Report.

---
**PENDIENTE.** <!-- COMPLETAR: enlace al video y descripción del contenido. El video debe
mostrar el producto en operación cubriendo el escenario principal: el operario reporta un
hallazgo desde el celular, el supervisor lo recibe en el panel, lo asigna y lo cierra, y el
indicador MTTR se actualiza. Duración sugerida: entre 3 y 5 minutos. -->

---

## capitulo-06-verification-validation.md

**PENDIENTE.** Actualizar el número total de pruebas y adjuntar la captura de la ejecución
después de la última corrida.

---
**PENDIENTE — opcional.** Si se desea evidencia formal de BDD, migrar estos escenarios a
`pytest-bdd` con archivos `.feature`. La cobertura de comportamiento ya existe; lo que
añadiría es la trazabilidad literal entre el archivo Gherkin y la prueba.

---
**PENDIENTE.** Ejecutar y registrar el resultado de cada escenario con fecha, entorno y
evidencia en imagen o video.

---
**PENDIENTE — herramientas externas.** Ejecutar un análisis con SonarQube o SonarCloud sobre
los tres repositorios y adjuntar el reporte de *code smells*, duplicación, cobertura y
*security hotspots*. <!-- IMAGEN REQUERIDA: captura del panel de SonarCloud en
assets/img/evidencia-sonar.png -->

---
**PENDIENTE — trabajo de campo.** Registro por entrevistado: nombre, edad, distrito, cargo,
fecha, duración, enlace al video con minuto de inicio, tareas completadas con sus tiempos y
resumen de los hallazgos. **Requiere realizar las entrevistas; no puede redactarse antes.**

---
**PENDIENTE.** Evaluación del producto contra las diez heurísticas de Nielsen, siguiendo el
formato que indique el docente: por cada problema detectado, la heurística incumplida, la
severidad de 0 a 4, la evidencia en imagen y la recomendación de mejora.

Puntos del producto que conviene revisar con honestidad en esta evaluación:

- *Visibilidad del estado del sistema:* el indicador de reportes pendientes de envío cumple
  esta heurística; conviene verificar si es igual de visible en todas las pantallas.
- *Prevención de errores:* el cierre de un hallazgo es irreversible y hoy no pide confirmación.
- *Reconocimiento antes que recuerdo:* la matriz IPERC muestra probabilidad y consecuencia como
  números, no como etiquetas, en la tabla principal.
- *Ayuda y documentación:* el producto no tiene ayuda en línea.

---
**PENDIENTE.** Nombre del startup auditado, producto, integrantes y enlace a su repositorio.

---
**PENDIENTE.** Fechas y actividades de la auditoría ejecutada.

---
**PENDIENTE.** Hallazgos organizados por heurística o criterio, con severidad, evidencia y
recomendación.

---
**PENDIENTE.**

---
**PENDIENTE.**

---
**PENDIENTE.**

---
**PENDIENTE.** Por cada hallazgo recibido: descripción, decisión tomada, cambio realizado y
commit o Pull Request que lo implementa. Esta trazabilidad entre la observación y el commit
que la resuelve es lo que demuestra que la auditoría tuvo efecto real.

---

## capitulo-07-devops-practices.md

**PENDIENTE — implementación.** Los pipelines de construcción existen y publican artefactos;
el despliegue automatizado a un entorno de pruebas está diseñado pero **no implementado
todavía**. Debe documentarse honestamente como tal hasta que se ejecute, indicando después el
proveedor elegido y adjuntando la evidencia del despliegue.

---
**PENDIENTE — implementación.** Documentar el despliegue real cuando se ejecute: URL de
producción, proveedor, procedimiento de rollback probado y evidencia de al menos un despliegue
completo. <!-- IMAGEN REQUERIDA: captura del despliegue exitoso en
assets/img/pipeline-deploy.png -->

---
**PENDIENTE — implementación.** Hoy el sistema **calcula** estas condiciones y las muestra en
el tablero (hallazgos críticos abiertos, inspecciones vencidas, acuerdos pendientes), pero
**no emite notificaciones**. Documentarlo así; implementar las notificaciones es el siguiente
incremento natural del producto.

---
**PENDIENTE — implementación.** Canal de notificación previsto: Firebase Cloud Messaging para
la aplicación Android y correo electrónico para el resumen diario. No implementado en esta
entrega.

---

## capitulo-08-experiment-driven.md

**PENDIENTE.** Consignar aquí el número real de participantes reclutados y recalcular el
efecto mínimo detectable con esa cifra antes de interpretar cualquier resultado.

---
**PENDIENTE.** Completar con el sprint de implementación de las historias To-Be, siguiendo el
mismo formato del Capítulo V.

---
**PENDIENTE.** <!-- IMAGEN REQUERIDA -->

---
**PENDIENTE.** <!-- IMAGEN REQUERIDA: captura del panel del experimento con el aviso de datos
de demostración y el intervalo de confianza, en assets/img/evidencia-tobe-web.png -->

---
**PENDIENTE.** <!-- IMAGEN REQUERIDA -->

---
**PENDIENTE.** Documentar los endpoints añadidos para las historias To-Be.

---
**PENDIENTE.** <!-- IMAGEN REQUERIDA: analíticos de GitHub del periodo de experimentación -->

---
**PENDIENTE — trabajo de campo.** Mismo formato de registro del Capítulo VI: datos del
entrevistado, fecha, enlace al video con minuto de inicio y resumen.

---
**PENDIENTE — datos reales.** Esta sección se completa únicamente con los datos de la corrida
real del experimento.

**Advertencia de integridad.** El comando `seed_demo` del repositorio `sst-api` genera 60 días
de historia **simulada**, en la que el grupo del formulario rápido reporta aproximadamente el
doble por construcción del generador. Esos datos sirven para demostrar el funcionamiento del
sistema, **no como evidencia experimental**. Si se muestran en la sustentación, deben
declararse como datos de demostración. Presentarlos como resultados sería fabricar evidencia.

Estructura que debe seguir el análisis cuando existan datos reales:

| Elemento | Contenido |
|---|---|
| Participantes | Usuarios por grupo, composición por área, bajas durante el periodo |
| Estadística descriptiva | Media, mediana, desviación estándar y rango de reportes por usuario en cada grupo |
| Serie temporal | Reportes diarios por variante, para detectar efecto de novedad |
| Prueba de hipótesis | Estadístico, grados de libertad, valor p y decisión sobre H₀ |
| Tamaño del efecto | Diferencia de medias, *lift* porcentual e intervalo de confianza al 95 % |
| Potencia alcanzada | Recalculada con el n real y la varianza observada |
| Interpretación | Qué significa el resultado para la decisión de producto |
| Limitaciones | Tamaño de muestra, población, duración, amenazas a la validez identificadas en 8.2.6 |

**Los tres desenlaces posibles y qué hacer con cada uno:**

1. *Diferencia significativa a favor del formulario rápido:* se adopta como formulario único y
   se elimina la variante larga del producto.
2. *Sin diferencia significativa con potencia suficiente:* la hipótesis se refuta; el supuesto
   A1 era falso y la inversión debe redirigirse a la barrera que señalen las entrevistas.
3. *Sin diferencia significativa con potencia insuficiente:* el experimento no concluye. Se
   reporta como no concluyente y se replantea con más participantes. **Este desenlace no debe
   presentarse como refutación.**

---
**PENDIENTE.** Repriorizar el backlog de preguntas a la luz del resultado. La pregunta Q1 sale
del backlog una vez respondida; las preguntas que las entrevistas revelen como más relevantes
—por ejemplo, el peso del temor a represalias— ingresan con su puntuación de incertidumbre y
costo de equivocarse.

---
**PENDIENTE.** Realizar la sesión y adjuntar los artefactos con su fecha.

---
**PENDIENTE.** <!-- COMPLETAR: enlace al video de presentación del producto. -->

---
**PENDIENTE.** Aplicar el framework Gees (Go to market, Engage, Expand, Sustain) según el
formato que indique el docente. Contenido sugerido con base en lo desarrollado:

| Etapa | Contenido propuesto |
|---|---|
| **Go to market** | Entrada por el canal de consultoras de SST, que atienden a varias empresas medianas y sufren la consolidación manual de registros. Producto mínimo: captura en campo más evidencia exportable |
| **Engage** | Adopción medida desde el primer día como métrica de producto; el circuito de retroalimentación al operario (aviso de cierre) como mecanismo de retención |
| **Expand** | Ampliación hacia vigilancia médica ocupacional y gestión de contratistas, los dos módulos que la competencia sí cubre |
| **Sustain** | Suscripción escalonada por número de trabajadores; el cumplimiento normativo recurrente sostiene la renovación |

---

## conclusiones.md

**PENDIENTE.** Incorporar aquí las conclusiones derivadas del resultado real del experimento y
de las entrevistas de validación, una vez ejecutados.

---
**PENDIENTE.** <!-- COMPLETAR: enlace al video de validación de la aplicación con usuarios
reales ejecutando las tareas definidas en la sección 6.3.1. -->

---
**PENDIENTE.** <!-- COMPLETAR: enlace al video del equipo, incluyendo los testimonios sobre
las dimensiones del Student Outcome 4 exigidos por el enunciado. -->

---
