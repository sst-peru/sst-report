# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

<!-- IMAGEN REQUERIDA: exportar el To-Be Scenario Map a assets/img/to-be-scenario-map.png -->

![To-Be Scenario Map](../assets/img/to-be-scenario-map.png)

| Fase | Detección | Reporte | Asignación | Corrección | Evidencia |
|---|---|---|---|---|---|
| **Acciones** | El trabajador identifica el peligro | Abre la app y reporta en tres toques con foto; si no hay señal, queda guardado y se envía solo | El supervisor ve el hallazgo en el panel y asigna responsable con un comentario | Se aplica la acción correctiva y se cierra el hallazgo describiéndola | El sistema exporta a Excel el registro completo con su trazabilidad |
| **Pensamientos** | "Esto es peligroso" | "Listo, quedó registrado" | "Esto es crítico, va primero" | "Queda documentado quién, qué y cuándo" | "Tengo cómo demostrarlo" |
| **Mejoras respecto del as-is** | — | Registro con hora exacta, foto y GPS; sin dependencia de la señal | Priorización por severidad en lugar de por quién insiste más | Responsable y plazo explícitos; bitácora automática | Expediente generado por la operación diaria, no reconstruido a mano |

## 3.2. User Stories

La columna **Plataforma** indica dónde está
implementada cada historia: `Web`, `Móvil` o `Ambas`. Esa columna es la evidencia de la paridad
exigida: para un mismo rol, ninguna capacidad existe en una plataforma y falta en la otra. Las
pocas historias marcadas con una sola plataforma lo están por una razón de dominio que se
explica en la propia fila, no por una funcionalidad faltante.

Las historias se agrupan en diez épicas. Los criterios de aceptación siguen el formato Gherkin
(Dado / Cuando / Entonces). Las historias técnicas (TS) corresponden a trabajo de infraestructura
sin valor directo para el usuario final pero necesario para sostener el producto.

### Épicas

| ID | Épica | Descripción |
|---|---|---|
| EP01 | Acceso y cuentas | Registro, autenticación y administración de usuarios y roles. |
| EP02 | Reporte de actos y condiciones inseguras | Captura del hallazgo en campo, con evidencia y operación sin conexión. |
| EP03 | Gestión del hallazgo | Seguimiento desde la recepción hasta el cierre verificado. |
| EP04 | Matriz IPERC | Identificación de peligros, evaluación de riesgos y controles. |
| EP05 | Control de EPP | Catálogo, entregas, vencimientos y conformidad del trabajador. |
| EP06 | Inspecciones periódicas | Programación, ejecución con checklist y cumplimiento. |
| EP07 | Comité de SST | Constitución, miembros, actas de reunión y acuerdos. |
| EP08 | Métricas y evidencia | Indicadores de gestión y exportación para auditorías. |
| EP09 | Experimento A/B | Asignación de variantes y medición de resultados. |
| EP10 | Calidad de uso y operación | Atributos transversales: consistencia visual, uso en campo, manejo de errores y respuesta ante fallos de red. |

### EP01 — Acceso y cuentas

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US01 | Registro de trabajador | **Como** trabajador **quiero** crear mi cuenta indicando el RUC de mi empresa **para** empezar a reportar sin depender de que alguien me la cree. | **Escenario: registro exitoso**<br>**Dado** que ingreso al formulario de registro<br>**Cuando** completo mis datos y el RUC de una empresa registrada<br>**Entonces** el sistema crea mi cuenta con rol operario y me deja dentro de la aplicación<br><br>**Escenario: RUC inexistente**<br>**Dado** que ingreso un RUC no registrado<br>**Cuando** envío el formulario<br>**Entonces** el sistema me indica que debo solicitar el RUC a mi supervisor y no crea la cuenta | Ambas | EP01 |
| US02 | Inicio de sesión | **Como** usuario **quiero** iniciar sesión con usuario y contraseña **para** acceder a la información de mi empresa. | **Escenario: credenciales válidas**<br>**Dado** que tengo una cuenta activa<br>**Cuando** ingreso mis credenciales correctas<br>**Entonces** el sistema me autentica y me lleva a la pantalla inicial de mi rol<br><br>**Escenario: credenciales inválidas**<br>**Cuando** ingreso credenciales incorrectas<br>**Entonces** el sistema muestra un mensaje de error sin revelar si el usuario existe | Ambas | EP01 |
| US03 | Sesión persistente en campo | **Como** operario **quiero** permanecer autenticado varios días **para** no tener que iniciar sesión cuando estoy en una zona sin señal. | **Escenario: renovación automática**<br>**Dado** que mi token de acceso expiró<br>**Cuando** la aplicación realiza una petición<br>**Entonces** el sistema renueva el token automáticamente y la petición se completa sin pedirme la contraseña | Ambas | EP01 |
| US04 | Administración de usuarios | **Como** supervisor de SST **quiero** crear usuarios y asignarles rol **para** incorporar al equipo de seguridad con los permisos correctos. | **Escenario: alta de supervisor**<br>**Dado** que tengo rol de supervisor<br>**Cuando** creo un usuario con rol supervisor<br>**Entonces** el usuario queda creado en mi empresa con ese rol<br><br>**Escenario: operario sin permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento listar los usuarios<br>**Entonces** el sistema deniega el acceso | Web | EP01 |
| US05 | Gestión de áreas | **Como** supervisor **quiero** registrar las áreas o frentes de trabajo **para** clasificar los hallazgos por ubicación organizativa. | **Escenario: alta de área**<br>**Cuando** registro un área con nombre y descripción<br>**Entonces** queda disponible para clasificar reportes, inspecciones y entradas IPERC | Web | EP01 |
| US41 | Cambio de rol de un usuario | **Como** supervisor **quiero** cambiar el rol de un usuario existente **para** incorporarlo al comité sin crearle una cuenta nueva. | **Cuando** cambio el rol desde la pantalla de usuarios<br>**Entonces** el usuario pasa a tener los permisos de ese rol en web y en móvil | Web | EP01 |
| US42 | Cierre de sesión | **Como** usuario **quiero** cerrar sesión **para** que nadie use mi cuenta en un equipo compartido. | **Cuando** cierro sesión<br>**Entonces** el sistema descarta mis credenciales y me devuelve a la pantalla de acceso | Ambas | EP01 |
| US43 | Menú según mi rol | **Como** operario **quiero** ver solo las opciones que me corresponden **para** no perderme entre funciones que no puedo usar. | **Dado** que tengo rol operario<br>**Entonces** el menú muestra únicamente reportar, mis reportes, mis EPP y las consultas, y no las opciones de gestión | Ambas | EP01 |

### EP02 — Reporte de actos y condiciones inseguras

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US06 | Reporte rápido desde el celular | **Como** operario **quiero** reportar un peligro en tres toques con una foto **para** no perder tiempo de trabajo. | **Escenario: reporte en tres pasos**<br>**Dado** que estoy en el frente de trabajo<br>**Cuando** elijo el tipo de hallazgo, la categoría y tomo la foto<br>**Entonces** el sistema registra el reporte y me confirma que quedó guardado<br><br>**Escenario: descripción opcional**<br>**Cuando** envío el reporte sin escribir descripción<br>**Entonces** el sistema lo acepta igualmente | Ambas | EP02 |
| US07 | Reporte sin conexión | **Como** operario en obra o mina **quiero** que mi reporte se guarde aunque no haya señal **para** no perderlo. | **Escenario: sin conectividad**<br>**Dado** que el dispositivo no tiene conexión<br>**Cuando** envío el reporte<br>**Entonces** se almacena localmente y se muestra como pendiente de envío<br><br>**Escenario: recuperación de señal**<br>**Cuando** el dispositivo recupera la conexión<br>**Entonces** el sistema sincroniza los reportes pendientes sin intervención del usuario | Móvil | EP02 |
| US08 | Sincronización sin duplicados | **Como** responsable de SST **quiero** que un reintento de envío no genere reportes repetidos **para** que las métricas sean confiables. | **Escenario: reintento del mismo reporte**<br>**Dado** un reporte con un identificador de cliente ya recibido<br>**Cuando** el dispositivo reintenta el envío<br>**Entonces** el sistema devuelve el reporte existente y no crea uno nuevo | Ambas | EP02 |
| US09 | Evidencia fotográfica | **Como** miembro del comité **quiero** ver la foto del hallazgo **para** entender el peligro sin desplazarme al lugar. | **Escenario: foto adjunta**<br>**Cuando** abro el detalle de un reporte con foto<br>**Entonces** veo la imagen y puedo ampliarla a pantalla completa | Ambas | EP02 |
| US10 | Geolocalización del hallazgo | **Como** supervisor **quiero** saber dónde ocurrió el hallazgo **para** ubicarlo dentro de la operación. | **Escenario: captura de coordenadas**<br>**Cuando** el operario autoriza la ubicación al tomar la foto<br>**Entonces** el reporte guarda latitud y longitud y el panel ofrece verlas en un mapa<br><br>**Escenario: permiso denegado**<br>**Cuando** el operario no autoriza la ubicación<br>**Entonces** el reporte se envía igualmente, sin coordenadas | Ambas | EP02 |
| US11 | Fecha real de ocurrencia | **Como** analista **quiero** que el reporte conserve la fecha en que ocurrió el hecho **para** que el indicador de tiempo de respuesta no se distorsione. | **Escenario: sincronización diferida**<br>**Dado** un reporte creado sin conexión el lunes<br>**Cuando** se sincroniza el miércoles<br>**Entonces** conserva la fecha de ocurrencia del lunes y registra además su fecha de recepción | Ambas | EP02 |
| US12 | Reporte desde la web | **Como** trabajador administrativo **quiero** reportar desde el navegador **para** no depender del celular. | **Escenario: paridad de canal**<br>**Cuando** reporto desde la web<br>**Entonces** el hallazgo se crea con los mismos campos y reglas que desde la aplicación móvil | Web | EP02 |
| US13 | Consulta de mis reportes | **Como** operario **quiero** ver los reportes que hice y su estado **para** saber si se atendieron. | **Escenario: alcance por rol**<br>**Dado** que tengo rol operario<br>**Cuando** consulto la lista de reportes<br>**Entonces** veo únicamente los míos | Ambas | EP02 |
| US44 | Vista previa de la evidencia | **Como** quien reporta **quiero** ver en pequeño la foto que elegí **para** confirmar que subí la correcta antes de enviar. | **Cuando** elijo una imagen<br>**Entonces** se muestra una miniatura con el nombre y el peso del archivo | Web | EP02 |
| US45 | Ampliar la evidencia | **Como** miembro del comité **quiero** ampliar la foto a pantalla completa **para** distinguir el detalle del peligro. | **Cuando** toco la imagen<br>**Entonces** se abre a pantalla completa y se cierra con Escape o tocando fuera | Web | EP02 |
| US46 | Reemplazar la foto elegida | **Como** quien reporta **quiero** quitar la foto y elegir otra **para** corregirme sin perder lo ya escrito. | **Cuando** quito la foto<br>**Entonces** el formulario conserva el resto de los datos y admite elegir una imagen nueva, incluso la misma | Web | EP02 |
| US47 | Categorías según el tipo de hallazgo | **Como** quien reporta **quiero** ver solo las categorías que aplican **para** no equivocarme entre actos y condiciones. | **Dado** que elegí condición insegura<br>**Entonces** solo se ofrecen categorías de condición | Ambas | EP02 |
| US48 | Estado de envío de mis reportes | **Como** operario **quiero** saber cuántos reportes tengo sin enviar **para** confiar en que no se perdieron. | **Dado** que hay reportes en la cola local<br>**Entonces** la pantalla muestra cuántos esperan señal, y cada uno indica si ya se envió | Móvil | EP02 |

### EP03 — Gestión del hallazgo

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US14 | Bandeja de hallazgos | **Como** supervisor **quiero** ver todos los hallazgos de la empresa filtrados por estado, tipo y área **para** priorizar mi trabajo. | **Escenario: filtro por estado**<br>**Cuando** filtro por estado abierto<br>**Entonces** la lista muestra solo los hallazgos sin atender | Ambas | EP03 |
| US15 | Asignación de responsable | **Como** supervisor **quiero** asignar un responsable al hallazgo **para** que alguien se haga cargo de la corrección. | **Escenario: asignación**<br>**Cuando** asigno un responsable<br>**Entonces** el hallazgo pasa a estado en proceso y queda registrado en la bitácora quién asignó, a quién y cuándo | Ambas | EP03 |
| US16 | Cierre con acción correctiva | **Como** supervisor **quiero** cerrar el hallazgo describiendo la acción aplicada **para** dejar evidencia de la corrección. | **Escenario: cierre**<br>**Cuando** cierro el hallazgo con la acción correctiva<br>**Entonces** el sistema registra la fecha de cierre y calcula el tiempo de resolución | Ambas | EP03 |
| US17 | Separación de responsabilidades | **Como** empresa **quiero** que quien reporta no sea quien valida el cierre **para** cumplir el control que exige la normativa. | **Escenario: operario intenta cerrar**<br>**Dado** que tengo rol operario<br>**Cuando** intento cerrar un hallazgo<br>**Entonces** el sistema deniega la operación | Ambas | EP03 |
| US18 | Bitácora del hallazgo | **Como** auditor interno **quiero** ver la secuencia completa de acciones sobre un hallazgo **para** verificar la trazabilidad. | **Escenario: historial**<br>**Cuando** abro el detalle de un hallazgo<br>**Entonces** veo en orden cronológico el reporte, las asignaciones, los comentarios y el cierre, cada uno con su autor y fecha | Ambas | EP03 |
| US49 | Descartar un reporte | **Como** supervisor **quiero** descartar un reporte que no corresponde a un hallazgo de SST **para** que no distorsione los indicadores. | **Cuando** descarto un reporte<br>**Entonces** pasa a estado descartado, queda registrado en la bitácora y deja de contarse como hallazgo abierto | Web | EP03 |
| US50 | Filtrar la bandeja | **Como** supervisor **quiero** filtrar por estado, tipo y área **para** trabajar por lotes en lugar de revisar todo. | **Cuando** aplico un filtro<br>**Entonces** la lista se reduce a los hallazgos que lo cumplen y el total se actualiza | Ambas | EP03 |
| US51 | Ubicar el hallazgo en el mapa | **Como** supervisor **quiero** abrir la ubicación del hallazgo en un mapa **para** llegar al punto exacto. | **Dado** que el reporte tiene coordenadas<br>**Entonces** el detalle ofrece un enlace que abre esa posición en un mapa | Web | EP03 |

### EP04 — Matriz IPERC

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US19 | Consulta de la matriz en campo | **Como** operario **quiero** consultar los peligros y controles de mi puesto desde el celular **para** saber cómo trabajar seguro. | **Escenario: consulta**<br>**Cuando** abro la matriz IPERC<br>**Entonces** veo los peligros con su nivel de riesgo y los controles existentes | Ambas | EP04 |
| US20 | Registro de peligros | **Como** supervisor **quiero** agregar y editar entradas de la matriz **para** mantenerla actualizada. | **Escenario: cálculo del nivel**<br>**Cuando** registro una entrada con probabilidad y consecuencia<br>**Entonces** el sistema calcula el puntaje y el nivel de riesgo resultante | Web | EP04 |
| US21 | Versionado de la matriz | **Como** responsable de SST **quiero** que la matriz se versione **para** mostrar su histórico ante una auditoría. | **Escenario: nueva versión**<br>**Cuando** creo una nueva matriz<br>**Entonces** el sistema le asigna el número de versión siguiente y conserva la anterior | Web | EP04 |
| US22 | Trazabilidad con el hallazgo de origen | **Como** miembro del comité **quiero** saber qué entradas de la matriz nacieron de un hallazgo real **para** demostrar que la matriz se alimenta del campo. | **Escenario: origen**<br>**Cuando** una entrada proviene de un reporte<br>**Entonces** el sistema muestra el número de ese reporte y permite abrirlo | Ambas | EP04 |
| US52 | Consultar versiones anteriores de la matriz | **Como** auditor interno **quiero** consultar versiones anteriores de la IPERC **para** verificar cómo evolucionaron los controles. | **Cuando** elijo una versión en el selector<br>**Entonces** la tabla muestra las entradas de esa versión y advierte que es histórica | Web | EP04 |
| US53 | Publicar una nueva versión de la matriz | **Como** responsable de SST **quiero** crear una versión nueva y ponerla vigente **para** actualizar la matriz sin borrar la anterior. | **Cuando** pongo vigente una versión<br>**Entonces** la anterior pasa a histórica y solo queda una vigente<br><br>**Escenario: versión histórica**<br>**Dado** que consulto una versión histórica<br>**Entonces** el sistema no permite editarla | Web | EP04 |
| US54 | Retirar un peligro de la matriz | **Como** responsable de SST **quiero** quitar una entrada que ya no aplica **para** que la matriz refleje la operación actual. | **Cuando** quito una entrada de la versión vigente<br>**Entonces** desaparece de la matriz y las versiones históricas la conservan | Web | EP04 |

### EP05 — Control de EPP

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US23 | Catálogo de EPP | **Como** supervisor **quiero** registrar los EPP con su vida útil **para** controlar reposiciones. | **Escenario: alta de EPP**<br>**Cuando** registro un EPP con su vida útil en días<br>**Entonces** queda disponible para registrar entregas | Web | EP05 |
| US24 | Registro de entrega | **Como** supervisor **quiero** registrar la entrega de un EPP a un trabajador **para** cumplir el registro obligatorio de la ley. | **Escenario: vencimiento automático**<br>**Cuando** registro una entrega<br>**Entonces** el sistema calcula la fecha de vencimiento a partir de la vida útil del EPP | Web | EP05 |
| US25 | Conformidad del trabajador | **Como** operario **quiero** dar conformidad de la entrega desde mi celular **para** que quede constancia sin firmar papeles. | **Escenario: conformidad**<br>**Dado** que soy el trabajador de la entrega<br>**Cuando** doy conformidad<br>**Entonces** la entrega queda marcada como conforme con la fecha | Ambas | EP05 |
| US26 | Alerta de EPP vencido | **Como** supervisor **quiero** identificar los EPP vencidos **para** reponerlos antes de que generen un riesgo. | **Escenario: marca de vencido**<br>**Cuando** la fecha de vencimiento es anterior a hoy<br>**Entonces** la entrega se muestra destacada como vencida | Ambas | EP05 |
| US55 | Control de stock del catálogo | **Como** supervisor **quiero** ver el stock y la vida útil de cada EPP **para** anticipar reposiciones. | **Cuando** abro el catálogo<br>**Entonces** veo por cada EPP su vida útil, su stock y cuántas entregas acumula | Web | EP05 |

### EP06 — Inspecciones periódicas

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US27 | Programa de inspecciones | **Como** supervisor **quiero** definir qué se inspecciona, cada cuánto y con qué checklist **para** sistematizar el programa anual. | **Escenario: alta de programa**<br>**Cuando** creo un programa con área, frecuencia y checklist<br>**Entonces** queda disponible para generar sus ocurrencias | Web | EP06 |
| US28 | Ejecución con checklist | **Como** inspector **quiero** realizar la inspección marcando el checklist desde el celular **para** registrarla en el lugar y no después. | **Escenario: ejecución**<br>**Cuando** marco los ítems y registro los hallazgos<br>**Entonces** la inspección queda como realizada con su fecha y responsable | Ambas | EP06 |
| US29 | Inspecciones vencidas | **Como** responsable de SST **quiero** ver las inspecciones que pasaron su fecha sin realizarse **para** actuar sobre el incumplimiento. | **Escenario: vencida**<br>**Dado** que la fecha programada ya pasó y la inspección sigue pendiente<br>**Entonces** el sistema la marca como vencida | Ambas | EP06 |
| US56 | Programar la siguiente inspección | **Como** supervisor **quiero** generar la siguiente ocurrencia según la frecuencia **para** no calcular fechas a mano. | **Cuando** genero la siguiente<br>**Entonces** el sistema crea la ocurrencia con la fecha que corresponde a la frecuencia del programa | Web | EP06 |
| US57 | Cumplimiento por área | **Como** responsable de SST **quiero** ver el cumplimiento desagregado por área **para** actuar sobre la que incumple. | **Cuando** consulto el indicador<br>**Entonces** veo programadas, realizadas y porcentaje por cada área | Web | EP06 |

### EP07 — Comité de SST

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US30 | Constitución del comité | **Como** responsable de SST **quiero** registrar el comité y su periodo **para** documentar su vigencia. | **Escenario: modo supervisor**<br>**Dado** que la empresa tiene menos de 20 trabajadores<br>**Cuando** registro el comité<br>**Entonces** el sistema lo marca como modo supervisor, conforme admite la ley | Web | EP07 |
| US31 | Miembros y paridad | **Como** responsable de SST **quiero** registrar los miembros con su cargo y representación **para** verificar que el comité sea paritario. | **Escenario: verificación de paridad**<br>**Cuando** el número de representantes del empleador difiere del de los trabajadores<br>**Entonces** el sistema advierte que el comité no es paritario | Web | EP07 |
| US32 | Acta de reunión | **Como** secretario del comité **quiero** registrar el acta con agenda, asistentes y desarrollo **para** cumplir con el registro obligatorio. | **Escenario: numeración correlativa**<br>**Cuando** registro una nueva acta<br>**Entonces** el sistema le asigna el número consecutivo siguiente, sin aceptarlo del cliente | Web | EP07 |
| US33 | Control de quórum | **Como** miembro del comité **quiero** saber si la reunión alcanzó quórum **para** conocer la validez del acta. | **Escenario: sin quórum**<br>**Dado** que asistieron menos de la mitad más uno de los titulares<br>**Entonces** el acta se muestra marcada como sin quórum | Ambas | EP07 |
| US34 | Acuerdos con responsable y plazo | **Como** presidente del comité **quiero** registrar los acuerdos con responsable y plazo **para** hacerles seguimiento. | **Escenario: seguimiento**<br>**Cuando** actualizo el estado de un acuerdo a cumplido<br>**Entonces** el indicador de cumplimiento de acuerdos se recalcula | Web | EP07 |
| US58 | Advertencia de comité no paritario | **Como** responsable de SST **quiero** que el sistema me advierta si el comité no es paritario **para** corregirlo antes de una fiscalización. | **Dado** que los representantes del empleador y de los trabajadores no son iguales en número<br>**Entonces** la pantalla muestra una advertencia explicando qué exige la ley | Web | EP07 |
| US59 | Seguimiento del estado de los acuerdos | **Como** presidente del comité **quiero** actualizar el estado de cada acuerdo **para** reflejar su avance real. | **Cuando** cambio el estado de un acuerdo<br>**Entonces** el indicador de cumplimiento del comité se recalcula | Web | EP07 |
| US60 | Consultar las actas desde el celular | **Como** trabajador **quiero** leer las actas y acuerdos del comité desde mi celular **para** enterarme de lo que se decidió. | **Cuando** abro la sección del comité<br>**Entonces** veo las actas con su fecha, quórum y acuerdos | Móvil | EP07 |

### EP08 — Métricas y evidencia

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US35 | Indicador MTTR | **Como** responsable de SST **quiero** conocer el tiempo promedio entre el reporte y el cierre **para** evaluar la capacidad de respuesta. | **Escenario: cálculo**<br>**Cuando** consulto el tablero<br>**Entonces** veo el MTTR del periodo, total y desagregado por severidad | Ambas | EP08 |
| US36 | Tasa de cumplimiento de inspecciones | **Como** responsable de SST **quiero** conocer qué proporción de inspecciones programadas se realizó **para** detectar áreas que incumplen. | **Escenario: desagregación**<br>**Cuando** consulto el indicador<br>**Entonces** veo el total y el detalle por área | Ambas | EP08 |
| US37 | Exportación de evidencia | **Como** responsable de SST **quiero** exportar a Excel los registros obligatorios **para** preparar el expediente de una inspección de SUNAFIL. | **Escenario: exportación**<br>**Cuando** exporto el registro de actos y condiciones inseguras<br>**Entonces** obtengo un archivo .xlsx con los campos del registro y su trazabilidad<br><br>**Escenario: permiso**<br>**Dado** que tengo rol operario<br>**Cuando** intento exportar<br>**Entonces** el sistema deniega la operación | Web | EP08 |
| US61 | MTTR por severidad | **Como** responsable de SST **quiero** ver el MTTR desagregado por severidad **para** distinguir si los críticos se atienden rápido. | **Cuando** consulto el tablero<br>**Entonces** veo el MTTR total y una fila por severidad con su promedio y cantidad de cerrados | Ambas | EP08 |
| US62 | Exportar cada registro obligatorio | **Como** responsable de SST **quiero** exportar por separado reportes, IPERC, EPP, inspecciones y actas **para** armar el expediente por tipo de registro. | **Cuando** exporto cualquiera de los cinco<br>**Entonces** obtengo un archivo .xlsx con la cabecera y los datos de ese registro | Web | EP08 |
| US63 | Resumen de hallazgos | **Como** responsable de SST **quiero** un resumen por estado, tipo, severidad y área **para** ver la distribución del riesgo de un vistazo. | **Cuando** consulto el resumen<br>**Entonces** obtengo los conteos por cada dimensión y el total de críticos sin atender | Ambas | EP08 |

### EP09 — Experimento A/B

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US38 | Asignación de variante | **Como** equipo de producto **quiero** que cada usuario quede asignado de forma estable a una variante **para** que la comparación sea válida. | **Escenario: estabilidad**<br>**Cuando** el mismo usuario consulta su variante en distintos momentos<br>**Entonces** obtiene siempre la misma | Ambas | EP09 |
| US39 | Registro de la variante en el reporte | **Como** analista **quiero** saber con qué formulario se creó cada reporte **para** atribuir correctamente los resultados. | **Escenario: atribución**<br>**Cuando** se crea un reporte<br>**Entonces** queda registrada la variante del formulario utilizado | Ambas | EP09 |
| US40 | Resultados del experimento | **Como** analista **quiero** comparar los reportes por usuario de cada variante **para** contrastar la hipótesis. | **Escenario: comparación**<br>**Cuando** consulto los resultados<br>**Entonces** veo, por variante, el número de usuarios, de reportes, el promedio por usuario y la diferencia porcentual | Web | EP09 |
| US64 | Variante disponible sin conexión | **Como** operario **quiero** que la aplicación sepa qué formulario mostrarme aunque no tenga señal **para** poder reportar igual. | **Dado** que la variante se guardó al iniciar sesión<br>**Cuando** abro el formulario sin conexión<br>**Entonces** se muestra la variante que me corresponde | Móvil | EP09 |

### EP10 — Calidad de uso y operación

| ID | Título | Descripción | Criterios de aceptación | Plataforma | Épica |
|---|---|---|---|---|---|
| US65 | Identidad visual consistente | **Como** usuario **quiero** una interfaz sobria y uniforme **para** confiar en que es un sistema de gestión formal y no un prototipo. | **Cuando** navego entre pantallas<br>**Entonces** encuentro la misma paleta, tipografía y tratamiento de estados en todas | Ambas | EP10 |
| US66 | Navegación siempre accesible | **Como** supervisor **quiero** que el menú permanezca visible al desplazarme **para** cambiar de sección sin volver arriba. | **Cuando** bajo por una tabla larga<br>**Entonces** la navegación sigue en pantalla | Ambas | EP10 |
| US67 | Uso desde pantallas pequeñas | **Como** supervisor en obra **quiero** usar el panel desde una pantalla angosta **para** no depender de la laptop. | **Cuando** reduzco el ancho de la ventana<br>**Entonces** la navegación pasa a barra superior y las tablas se desplazan sin romper el diseño | Web | EP10 |
| US68 | Errores comprensibles | **Como** usuario **quiero** entender qué salió mal **para** poder corregirlo yo mismo. | **Cuando** el servidor rechaza una operación<br>**Entonces** la pantalla muestra el motivo en lenguaje claro, indicando el campo cuando corresponde | Ambas | EP10 |
| US69 | Reintento ante fallo de red | **Como** operario **quiero** reintentar una consulta que falló **para** no tener que reiniciar la aplicación. | **Dado** que una pantalla no pudo cargar<br>**Entonces** muestra el motivo y un botón para reintentar | Móvil | EP10 |
| US70 | Sesión que no expira en campo | **Como** operario **quiero** seguir trabajando sin volver a iniciar sesión **para** no quedarme fuera en una zona sin señal. | **Cuando** mi token de acceso caduca<br>**Entonces** el sistema lo renueva automáticamente y la operación continúa | Ambas | EP10 |

### Historias técnicas

Trabajo de infraestructura sin valor directo para el usuario final, pero necesario para sostener
el producto y exigido por el curso. La columna indica el repositorio donde vive.

| ID | Título | Descripción | Criterios de aceptación | Repositorio | Épica |
|---|---|---|---|---|---|
| TS01 | Integración continua | **Como** equipo de desarrollo **quiero** que cada Pull Request ejecute pruebas y análisis estático **para** no integrar código roto. | **Escenario: PR con pruebas fallidas**<br>**Cuando** abro un PR cuyas pruebas fallan<br>**Entonces** el pipeline marca el PR en rojo y bloquea la integración | Los cuatro | — |
| TS02 | Convenciones de commits | **Como** equipo **quiero** que los mensajes de commit sigan Conventional Commits **para** mantener un historial legible y auditable. | **Escenario: mensaje inválido**<br>**Cuando** intento commitear con un mensaje fuera del formato<br>**Entonces** el hook local lo rechaza y el workflow de CI también | Los cuatro | — |
| TS03 | Documentación viva del API | **Como** desarrollador de los clientes **quiero** una especificación OpenAPI generada del código **para** que el contrato no se desactualice. | **Escenario: documentación**<br>**Cuando** accedo a la ruta de documentación<br>**Entonces** obtengo la especificación de todos los endpoints vigentes | sst-api | — |
| TS04 | Datos de demostración | **Como** equipo **quiero** un comando que genere datos realistas **para** poder demostrar y probar el sistema. | **Escenario: carga**<br>**Cuando** ejecuto el comando de carga<br>**Entonces** el sistema queda con empresa, usuarios, reportes, IPERC, EPP, inspecciones y actas de ejemplo, claramente identificados como datos de demostración | sst-api | — |
| TS05 | Flujo de ramas GitFlow | **Como** equipo **quiero** un flujo de ramas definido y protegido **para** que nada llegue a la línea principal sin revisión. | **Dado** que intento empujar directamente a main o develop<br>**Entonces** la protección de rama lo rechaza y obliga a pasar por Pull Request | Los cuatro | — |
| TS06 | Fin de línea normalizado | **Como** equipo que trabaja en Windows **quiero** que el repositorio guarde siempre LF **para** que no aparezcan diferencias falsas en cada archivo. | **Cuando** edito un archivo en Windows y lo commiteo<br>**Entonces** el repositorio lo guarda con LF y el diff muestra solo lo que cambié de verdad | Los cuatro | — |
| TS07 | Validación local del mensaje de commit | **Como** desarrollador **quiero** que el formato del commit se valide antes de crearlo **para** enterarme al momento y no en el Pull Request. | **Cuando** intento commitear con un mensaje fuera de formato<br>**Entonces** el hook lo rechaza mostrando los tipos válidos y un ejemplo | Los cuatro | — |
| TS08 | Configuración por variables de entorno | **Como** responsable del despliegue **quiero** que la configuración viva fuera del código **para** usar el mismo artefacto en desarrollo y en producción. | **Cuando** cambio la base de datos o el origen permitido<br>**Entonces** basta modificar el archivo de entorno, sin tocar ni reconstruir el código | sst-api | — |
| TS09 | Proxy de desarrollo | **Como** desarrollador de la web **quiero** que las peticiones al API pasen por el servidor de desarrollo **para** no lidiar con CORS en local. | **Cuando** levanto la web en desarrollo<br>**Entonces** las llamadas a /api llegan al backend sin error de origen cruzado | sst-web | — |
| TS10 | Renovación transparente del token | **Como** usuario **quiero** no perder lo que estoy haciendo cuando expira mi sesión **para** no repetir el trabajo. | **Dado** que varias peticiones fallan a la vez por token expirado<br>**Entonces** el cliente renueva una sola vez y reintenta todas, sin pedir la contraseña | sst-web, sst-mobile | — |
| TS11 | Aislamiento entre empresas | **Como** empresa cliente **quiero** que mis datos sean invisibles para otras empresas **para** poder usar un servicio compartido. | **Cuando** un usuario consulta cualquier recurso<br>**Entonces** la consulta se restringe a su empresa en el backend, no en la interfaz | sst-api | — |
| TS12 | Idempotencia en la creación de reportes | **Como** equipo de datos **quiero** que un reintento no genere un hallazgo duplicado **para** que las métricas sean confiables. | **Cuando** llega dos veces el mismo identificador de cliente<br>**Entonces** el API devuelve el reporte existente y no crea otro | sst-api | — |
| TS13 | Migraciones verificadas en integración | **Como** equipo **quiero** que un modelo cambiado sin migración rompa la construcción **para** no descubrirlo en el despliegue. | **Cuando** abro un Pull Request con un modelo modificado y sin migración<br>**Entonces** el pipeline falla indicando que faltan migraciones | sst-api | — |
| TS14 | APK publicado por el pipeline | **Como** equipo **quiero** que cada construcción publique el APK **para** poder instalarlo y probarlo sin compilar. | **Cuando** el pipeline móvil termina correctamente<br>**Entonces** el APK de depuración queda disponible como artefacto de la ejecución | sst-mobile | — |
| TS15 | Generación de evidencia en Excel | **Como** responsable de SST **quiero** que la evidencia se genere en el formato que la auditoría espera **para** entregarla sin retrabajo. | **Cuando** solicito una exportación<br>**Entonces** el sistema genera un .xlsx con cabecera formateada, anchos ajustados y los datos del registro | sst-api | — |
| TS16 | Informe compilable y con índice verificado | **Como** equipo **quiero** que el informe se arme solo y su índice no se desactualice **para** exportar el PDF sin revisiones manuales. | **Cuando** abro un Pull Request con el índice desfasado<br>**Entonces** el pipeline del informe falla e indica cómo regenerarlo | sst-report | — |

## 3.3. Product Backlog

Orden por prioridad de negocio: primero lo que hace que el sistema capture el hallazgo, después
lo que permite gestionarlo, y al final lo que sostiene la operación. La estimación usa Story
Points en escala de Fibonacci. La columna Plataforma se repite aquí para que la paridad sea
verificable sin volver a la sección anterior.

| # | ID | Historia | Épica | Plataforma | Story Points |
|---|---|---|---|---|---|
| 1 | US02 | Inicio de sesión | EP01 | Ambas | 3 |
| 2 | US06 | Reporte rápido desde el celular | EP02 | Ambas | 8 |
| 3 | US07 | Reporte sin conexión | EP02 | Móvil | 13 |
| 4 | US08 | Sincronización sin duplicados | EP02 | Ambas | 8 |
| 5 | US13 | Consulta de mis reportes | EP02 | Ambas | 3 |
| 6 | US43 | Menú según mi rol | EP01 | Ambas | 3 |
| 7 | US70 | Sesión que no expira en campo | EP10 | Ambas | 5 |
| 8 | US14 | Bandeja de hallazgos | EP03 | Ambas | 5 |
| 9 | US16 | Cierre con acción correctiva | EP03 | Ambas | 5 |
| 10 | US15 | Asignación de responsable | EP03 | Ambas | 5 |
| 11 | US17 | Separación de responsabilidades | EP03 | Ambas | 3 |
| 12 | US18 | Bitácora del hallazgo | EP03 | Ambas | 3 |
| 13 | US09 | Evidencia fotográfica | EP02 | Ambas | 5 |
| 14 | US35 | Indicador MTTR | EP08 | Ambas | 5 |
| 15 | US50 | Filtrar la bandeja | EP03 | Ambas | 3 |
| 16 | US49 | Descartar un reporte | EP03 | Web | 2 |
| 17 | US10 | Geolocalización del hallazgo | EP02 | Ambas | 5 |
| 18 | US11 | Fecha real de ocurrencia | EP02 | Ambas | 3 |
| 19 | US12 | Reporte desde la web | EP02 | Web | 5 |
| 20 | US44 | Vista previa de la evidencia | EP02 | Web | 3 |
| 21 | US45 | Ampliar la evidencia | EP02 | Web | 3 |
| 22 | US46 | Reemplazar la foto elegida | EP02 | Web | 2 |
| 23 | US47 | Categorías según el tipo de hallazgo | EP02 | Ambas | 2 |
| 24 | US48 | Estado de envío de mis reportes | EP02 | Móvil | 3 |
| 25 | US51 | Ubicar el hallazgo en el mapa | EP03 | Web | 1 |
| 26 | US38 | Asignación de variante | EP09 | Ambas | 5 |
| 27 | US39 | Registro de la variante en el reporte | EP09 | Ambas | 2 |
| 28 | US40 | Resultados del experimento | EP09 | Web | 5 |
| 29 | US64 | Variante disponible sin conexión | EP09 | Móvil | 3 |
| 30 | US01 | Registro de trabajador | EP01 | Ambas | 5 |
| 31 | US03 | Sesión persistente en campo | EP01 | Ambas | 3 |
| 32 | US05 | Gestión de áreas | EP01 | Web | 2 |
| 33 | US04 | Administración de usuarios | EP01 | Web | 5 |
| 34 | US41 | Cambio de rol de un usuario | EP01 | Web | 2 |
| 35 | US42 | Cierre de sesión | EP01 | Ambas | 1 |
| 36 | US19 | Consulta de la matriz en campo | EP04 | Ambas | 3 |
| 37 | US20 | Registro de peligros | EP04 | Web | 5 |
| 38 | US21 | Versionado de la matriz | EP04 | Web | 5 |
| 39 | US22 | Trazabilidad con el hallazgo de origen | EP04 | Ambas | 3 |
| 40 | US52 | Consultar versiones anteriores de la matriz | EP04 | Web | 5 |
| 41 | US53 | Publicar una nueva versión de la matriz | EP04 | Web | 5 |
| 42 | US54 | Retirar un peligro de la matriz | EP04 | Web | 2 |
| 43 | US23 | Catálogo de EPP | EP05 | Web | 3 |
| 44 | US24 | Registro de entrega | EP05 | Web | 3 |
| 45 | US25 | Conformidad del trabajador | EP05 | Ambas | 3 |
| 46 | US26 | Alerta de EPP vencido | EP05 | Ambas | 2 |
| 47 | US55 | Control de stock del catálogo | EP05 | Web | 2 |
| 48 | US27 | Programa de inspecciones | EP06 | Web | 5 |
| 49 | US28 | Ejecución con checklist | EP06 | Ambas | 5 |
| 50 | US29 | Inspecciones vencidas | EP06 | Ambas | 3 |
| 51 | US56 | Programar la siguiente inspección | EP06 | Web | 3 |
| 52 | US36 | Tasa de cumplimiento de inspecciones | EP08 | Ambas | 5 |
| 53 | US57 | Cumplimiento por área | EP06 | Web | 3 |
| 54 | US30 | Constitución del comité | EP07 | Web | 3 |
| 55 | US31 | Miembros y paridad | EP07 | Web | 5 |
| 56 | US32 | Acta de reunión | EP07 | Web | 5 |
| 57 | US33 | Control de quórum | EP07 | Ambas | 3 |
| 58 | US34 | Acuerdos con responsable y plazo | EP07 | Web | 3 |
| 59 | US58 | Advertencia de comité no paritario | EP07 | Web | 2 |
| 60 | US59 | Seguimiento del estado de los acuerdos | EP07 | Web | 2 |
| 61 | US60 | Consultar las actas desde el celular | EP07 | Móvil | 3 |
| 62 | US37 | Exportación de evidencia | EP08 | Web | 8 |
| 63 | US61 | MTTR por severidad | EP08 | Ambas | 3 |
| 64 | US62 | Exportar cada registro obligatorio | EP08 | Web | 3 |
| 65 | US63 | Resumen de hallazgos | EP08 | Ambas | 3 |
| 66 | US65 | Identidad visual consistente | EP10 | Ambas | 5 |
| 67 | US66 | Navegación siempre accesible | EP10 | Ambas | 2 |
| 68 | US67 | Uso desde pantallas pequeñas | EP10 | Web | 5 |
| 69 | US68 | Errores comprensibles | EP10 | Ambas | 3 |
| 70 | US69 | Reintento ante fallo de red | EP10 | Móvil | 3 |
| 71 | TS02 | Convenciones de commits | — | Los cuatro | 2 |
| 72 | TS07 | Validación local del mensaje de commit | — | Los cuatro | 2 |
| 73 | TS05 | Flujo de ramas GitFlow | — | Los cuatro | 3 |
| 74 | TS06 | Fin de línea normalizado | — | Los cuatro | 2 |
| 75 | TS01 | Integración continua | — | Los cuatro | 5 |
| 76 | TS13 | Migraciones verificadas en integración | — | sst-api | 2 |
| 77 | TS03 | Documentación viva del API | — | sst-api | 2 |
| 78 | TS08 | Configuración por variables de entorno | — | sst-api | 3 |
| 79 | TS09 | Proxy de desarrollo | — | sst-web | 2 |
| 80 | TS10 | Renovación transparente del token | — | sst-web, sst-mobile | 5 |
| 81 | TS11 | Aislamiento entre empresas | — | sst-api | 5 |
| 82 | TS12 | Idempotencia en la creación de reportes | — | sst-api | 5 |
| 83 | TS04 | Datos de demostración | — | sst-api | 5 |
| 84 | TS14 | APK publicado por el pipeline | — | sst-mobile | 3 |
| 85 | TS15 | Generación de evidencia en Excel | — | sst-api | 5 |
| 86 | TS16 | Informe compilable y con índice verificado | — | sst-report | 3 |

**Total:** 86 elementos (70 historias de
usuario y 16 historias técnicas), 319 Story Points.

## 3.4. Impact Mapping

<!-- IMAGEN REQUERIDA: exportar el Impact Map a assets/img/impact-map.png -->

![Impact Map](../assets/img/impact-map.png)

| Goal (¿Por qué?) | Actor (¿Quién?) | Impact (¿Cómo?) | Deliverable (¿Qué?) |
|---|---|---|---|
| **Reducir el tiempo entre la detección de un peligro y su corrección, evidenciando la gestión ante la autoridad** | Operario de campo | Reporta más seguido porque le cuesta poco | Formulario de tres pasos con foto (US06) |
| | | No pierde reportes por falta de señal | Cola local y sincronización automática (US07, US08) |
| | | Sostiene el hábito porque ve resultados | Consulta del estado de sus reportes (US13) |
| | Supervisor de SST | Se entera de inmediato y prioriza por severidad | Bandeja de hallazgos filtrable (US14) |
| | | Hace responsable a alguien con plazo | Asignación y cierre con acción correctiva (US15, US16) |
| | | Mide en lugar de suponer | Indicadores MTTR y cumplimiento (US35, US36) |
| | Comité de SST | Documenta sus decisiones y les da seguimiento | Actas con quórum y acuerdos (US32, US33, US34) |
| | | Mantiene viva la matriz IPERC | Entradas con origen en hallazgos reales (US20, US22) |
| | Empresa ante SUNAFIL | Demuestra gestión en lugar de solo documentación | Exportación de los registros obligatorios (US37) |
