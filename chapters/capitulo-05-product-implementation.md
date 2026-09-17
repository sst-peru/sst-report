# Capítulo V: Product Implementation

## 5.1. Software Configuration Management

### 5.1.1. Software Development Environment Configuration

| Propósito | Herramienta | Versión | Justificación |
|---|---|---|---|
| Control de versiones | Git | 2.45 | Estándar del curso; requerido para GitFlow y Conventional Commits |
| Alojamiento y colaboración | GitHub (organización pública `sst-peru`) | — | Exigido por el enunciado: organización pública con evidencia de commits |
| Automatización | GitHub Actions | — | Integrado al repositorio, sin infraestructura adicional |
| Backend | Python | 3.13 | Soportado por Django 5.1 |
| Framework backend | Django + Django REST Framework | 5.1.4 / 3.15.2 | Django aporta ORM, migraciones, autenticación y panel de administración; DRF añade el API REST |
| Documentación del API | drf-spectacular | 0.28.0 | Genera OpenAPI desde el código, evitando que el contrato se desactualice |
| Autenticación | djangorestframework-simplejwt | 5.3.1 | JWT consumido igual por web y móvil |
| Exportación de evidencia | openpyxl | 3.1.5 | Generación de .xlsx sin dependencias externas |
| Base de datos | PostgreSQL / SQLite | 16 / 3 | PostgreSQL en despliegue; SQLite en desarrollo local |
| Frontend web | React + TypeScript + Vite | 18.3 / 5.7 / 6.0 | TypeScript da verificación estática del contrato del API; Vite acelera el ciclo de desarrollo |
| Estado del servidor en la web | TanStack Query | 5.62 | Manejo de caché e invalidación sin escribir un reducer por pantalla |
| Cliente HTTP web | Axios | 1.7 | Interceptores para JWT y renovación de token |
| Móvil | Kotlin + Jetpack Compose | 2.0.21 / BOM 2024.12 | Android nativo con interfaz declarativa |
| Persistencia local móvil | Room | 2.6.1 | Cola de reportes pendientes de envío |
| Sincronización móvil | WorkManager | 2.10.0 | Reintento con backoff al recuperar la conectividad |
| Red móvil | Retrofit + OkHttp | 2.11 / 4.12 | Cliente HTTP con interceptor de autenticación |
| Entorno de desarrollo | Visual Studio Code / Android Studio | — | Edición del backend y la web; compilación y emulación Android |
| Pruebas backend | pytest + pytest-django | 8.3 / 4.9 | Suite de pruebas del API |
| Análisis estático | ruff / ESLint / TypeScript | 0.8 / 9.17 / 5.7 | Verificación sin ejecutar el código |

### 5.1.2. Source Code Management

**Repositorios.** El producto se organiza en tres repositorios independientes más el del informe,
todos dentro de la organización pública `sst-peru`:

| Repositorio | Contenido |
|---|---|
| `sst-api` | API REST en Django; concentra el modelo de dominio y las reglas de negocio |
| `sst-web` | Panel web en React |
| `sst-mobile` | Aplicación Android nativa |
| `sst-report` | Este informe |

La separación responde a que cada uno tiene su propio ciclo de construcción, su propio pipeline
y su propio lenguaje; un monorepo habría obligado a ejecutar los tres pipelines ante cualquier
cambio.

**Modelo de ramas.**

| Rama | Propósito | Sale de | Vuelve a |
|---|---|---|---|
| `main` | Solo versiones entregables, etiquetadas | — | — |
| `develop` | Integración del trabajo en curso | main | — |
| `feature/*` | Nueva funcionalidad | develop | develop |
| `fix/*` | Corrección de defecto | develop | develop |
| `docs/*` | Redacción del informe | develop | develop |
| `chore/*` | Infraestructura y configuración | develop | develop |

Reglas de protección aplicadas en GitHub: `main` y `develop` no aceptan push directo ni
force push; la integración ocurre exclusivamente por Pull Request; `develop` es la rama por
defecto, de modo que los PR apuntan ahí sin intervención.

**Conventional Commits.** Todos los mensajes siguen `tipo(alcance): descripción`. Ejemplos
reales del historial del proyecto:

```
feat(auth): agregar empresa, areas, usuario con roles y endpoints de registro y login
feat(reports): agregar reportes de actos y condiciones inseguras con cierre y bitacora
feat(sync): subir reportes pendientes con workmanager cuando vuelve la red
fix(reports): redondear la latitud y longitud del gps antes de validar
fix(auth)!: impedir que el registro publico elija su propio rol y agregar endpoint de usuarios
test(reports): cubrir creacion offline, permisos por rol y calculo de mttr
ci: agregar workflows de tests, lint y validacion de conventional commits
```

El signo `!` marca un cambio que rompe el contrato del API, como ocurrió al retirar el campo
`role` del registro público.

La convención se verifica en dos momentos: un hook `commit-msg` local la rechaza antes de crear
el commit, y un workflow de GitHub Actions la valida sobre todos los commits del Pull Request.
Tener ambas capas importa porque el hook local puede no estar instalado en una máquina nueva.

### 5.1.3. Source Code Style Guide & Conventions

| Ámbito | Convención | Verificación |
|---|---|---|
| Python | PEP 8 con línea de 100 caracteres; `ruff` con las reglas E, F, I, UP, B y DJ | `ruff check .` en CI |
| Nombres en Python | `snake_case` para funciones y variables, `PascalCase` para clases, español para el vocabulario de dominio y inglés para los nombres del framework | Revisión en PR |
| TypeScript | ESLint con reglas recomendadas más `react-hooks`; modo estricto de TypeScript con `noUnusedLocals` y `noUnusedParameters` | `npm run lint` y `npm run typecheck` en CI |
| Nombres en TypeScript | `camelCase` para variables y funciones, `PascalCase` para componentes y tipos | Revisión en PR |
| Kotlin | Estilo oficial de Kotlin (`kotlin.code.style=official`); composables en `PascalCase` | Compilación en CI |
| CSS | Propiedades personalizadas para toda la paleta; sin valores de color literales fuera de `:root` | Revisión en PR |
| Comentarios | Se comenta el **porqué**, no el qué. Un comentario que repite el código se elimina en revisión | Revisión en PR |
| Fin de línea | LF en el repositorio, forzado por `.gitattributes`; CRLF solo en `.bat`, `.cmd` y `.ps1` | `.gitattributes` |
| Idioma | Código y mensajes de commit sin tildes ni eñes; interfaz y documentación en español correcto | Revisión en PR |

### 5.1.4. Software Deployment Configuration

| Componente | Configuración |
|---|---|
| API | Variables de entorno mediante archivo `.env` (`DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASE_URL`, `CORS_ALLOWED_ORIGINS`). `DATABASE_URL` vacío usa SQLite; con valor, PostgreSQL |
| Web | `VITE_API_URL` define el API consumido. En desarrollo, Vite hace proxy de `/api` al backend, evitando CORS |
| Móvil | `API_BASE_URL` se inyecta como `buildConfigField` en Gradle. En emulador, `http://10.0.2.2:8000/api/v1/`, que es la dirección con la que el emulador alcanza el `localhost` del anfitrión |
| Tráfico en claro | `network_security_config.xml` permite HTTP sin cifrar únicamente contra direcciones de desarrollo; en producción el API va por HTTPS |
| Secretos | Ningún secreto se versiona: `.env` está en `.gitignore` y se distribuye `.env.example` con los nombres de variable |

> **PENDIENTE — despliegue.** Documentar aquí el despliegue real cuando esté hecho: proveedor
> (Render, Railway, Fly.io o similar para el API; Vercel o Netlify para la web), URL pública de
> cada entorno, y procedimiento de migración de base de datos en el despliegue.

## 5.2. Product Implementation & Deployment

### 5.2.1. Sprint Backlogs

El desarrollo se organizó en seis bloques de trabajo, tratados aquí como sprints. El Product
Backlog del Capítulo III contiene los 162 elementos del producto, de los cuales 86
(319 Story Points) están implementados y 76 quedan
especificados como backlog pendiente. Los Sprint Backlogs que siguen cubren exactamente esos 86
elementos implementados: cada uno contiene únicamente aquello que ese sprint se comprometió a
completar, y la suma de los seis equivale al alcance efectivamente construido en este ciclo. Los
elementos marcados *Propuesta* en el Capítulo III no figuran en ningún sprint, precisamente
porque no se construyeron.

La columna *Story Points completados* coincide con los planificados en los seis sprints porque
todos los elementos comprometidos quedaron terminados; no hubo arrastre de un sprint al
siguiente.

**Sobre el periodo de ejecución.** Conviene decirlo con precisión, porque el historial de los
repositorios es público y cualquiera puede contrastarlo: los seis sprints de esta sección
**organizan el alcance, no ventanas de calendario**. El trabajo no se repartió en seis
iteraciones separadas por semanas; se ejecutó en sesiones intensivas de desarrollo entre el 12 y
el 16 de septiembre de 2026, que es lo que muestran las fechas de los commits en `sst-api`,
`sst-web`, `sst-mobile` y `sst-report`. Por eso las tablas que siguen no declaran fechas de
inicio y fin: declararlas repartidas en semanas sería contradecir un dato verificable en un clic.

Esa aclaración no vacía de contenido a los Sprint Backlogs. Lo que cada uno documenta —qué
objetivo perseguía ese bloque de trabajo, qué elementos se comprometieron en él, cuántos Story
Points suponía y en qué orden se construyó sobre lo anterior— sigue siendo la información que un
Sprint Backlog aporta, y es la que permite entender por qué el producto se levantó en ese orden
y no en otro: primero la captura del hallazgo, después su gestión, luego los registros
obligatorios y al final la evidencia exportable.

Lo que sí se sostuvo de la práctica iterativa es el criterio de incremento: cada bloque cierra
con el producto funcionando de extremo a extremo para lo que ese bloque prometía, no con piezas
sueltas a la espera de integrarse. El Sprint 1 termina con un operario capaz de registrar un
hallazgo sin señal; el Sprint 2, con ese hallazgo asignado y cerrado; y así sucesivamente.

> **Limitación reconocida.** Un ciclo de desarrollo comprimido impide observar lo que la práctica
> iterativa busca: retroalimentación del usuario entre iteraciones que reoriente el alcance de la
> siguiente. Los seis bloques se ejecutaron sobre un plan fijado de antemano. Se documenta como
> limitación del trabajo, no como práctica recomendable.

**Sprint 1**

| Campo | Valor |
|---|---|
| Objetivo | Que un operario pueda entrar y registrar un hallazgo, con o sin señal. |
| Elementos comprometidos | 11 |
| Story Points planificados | 52 |
| Story Points completados | 52 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US02 | Inicio de sesión | Ambas | 3 | Completado |
| US06 | Reporte rápido desde el celular | Ambas | 8 | Completado |
| US07 | Reporte sin conexión | Móvil | 13 | Completado |
| US08 | Sincronización sin duplicados | Ambas | 8 | Completado |
| US13 | Consulta de mis reportes | Ambas | 3 | Completado |
| US43 | Menú según mi rol | Ambas | 3 | Completado |
| US70 | Sesión que no expira en campo | Ambas | 5 | Completado |
| TS02 | Convenciones de commits | Los cuatro | 2 | Completado |
| TS07 | Validación local del mensaje de commit | Los cuatro | 2 | Completado |
| TS05 | Flujo de ramas GitFlow | Los cuatro | 3 | Completado |
| TS06 | Fin de línea normalizado | Los cuatro | 2 | Completado |

**Sprint 2**

| Campo | Valor |
|---|---|
| Objetivo | Cerrar el ciclo del hallazgo: recibirlo, asignarlo y cerrarlo con evidencia. |
| Elementos comprometidos | 12 |
| Story Points planificados | 48 |
| Story Points completados | 48 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US14 | Bandeja de hallazgos | Ambas | 5 | Completado |
| US16 | Cierre con acción correctiva | Ambas | 5 | Completado |
| US15 | Asignación de responsable | Ambas | 5 | Completado |
| US17 | Separación de responsabilidades | Ambas | 3 | Completado |
| US18 | Bitácora del hallazgo | Ambas | 3 | Completado |
| US09 | Evidencia fotográfica | Ambas | 5 | Completado |
| US35 | Indicador MTTR | Ambas | 5 | Completado |
| US50 | Filtrar la bandeja | Ambas | 3 | Completado |
| US49 | Descartar un reporte | Web | 2 | Completado |
| TS01 | Integración continua | Los cuatro | 5 | Completado |
| TS13 | Migraciones verificadas en integración | sst-api | 2 | Completado |
| TS11 | Aislamiento entre empresas | sst-api | 5 | Completado |

**Sprint 3**

| Campo | Valor |
|---|---|
| Objetivo | Completar la captura y dejar el experimento A/B corriendo. |
| Elementos comprometidos | 14 |
| Story Points planificados | 47 |
| Story Points completados | 47 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US10 | Geolocalización del hallazgo | Ambas | 5 | Completado |
| US11 | Fecha real de ocurrencia | Ambas | 3 | Completado |
| US12 | Reporte desde la web | Web | 5 | Completado |
| US44 | Vista previa de la evidencia | Web | 3 | Completado |
| US45 | Ampliar la evidencia | Web | 3 | Completado |
| US46 | Reemplazar la foto elegida | Web | 2 | Completado |
| US47 | Categorías según el tipo de hallazgo | Ambas | 2 | Completado |
| US48 | Estado de envío de mis reportes | Móvil | 3 | Completado |
| US51 | Ubicar el hallazgo en el mapa | Web | 1 | Completado |
| US38 | Asignación de variante | Ambas | 5 | Completado |
| US39 | Registro de la variante en el reporte | Ambas | 2 | Completado |
| US40 | Resultados del experimento | Web | 5 | Completado |
| US64 | Variante disponible sin conexión | Móvil | 3 | Completado |
| TS12 | Idempotencia en la creación de reportes | sst-api | 5 | Completado |

**Sprint 4**

| Campo | Valor |
|---|---|
| Objetivo | Cuentas, roles y estructura organizativa de la empresa. |
| Elementos comprometidos | 10 |
| Story Points planificados | 30 |
| Story Points completados | 30 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US01 | Registro de trabajador | Ambas | 5 | Completado |
| US03 | Sesión persistente en campo | Ambas | 3 | Completado |
| US05 | Gestión de áreas | Web | 2 | Completado |
| US04 | Administración de usuarios | Web | 5 | Completado |
| US41 | Cambio de rol de un usuario | Web | 2 | Completado |
| US42 | Cierre de sesión | Ambas | 1 | Completado |
| TS03 | Documentación viva del API | sst-api | 2 | Completado |
| TS08 | Configuración por variables de entorno | sst-api | 3 | Completado |
| TS09 | Proxy de desarrollo | sst-web | 2 | Completado |
| TS10 | Renovación transparente del token | sst-web, sst-mobile | 5 | Completado |

**Sprint 5**

| Campo | Valor |
|---|---|
| Objetivo | Los registros obligatorios del SGSST: IPERC, EPP e inspecciones. |
| Elementos comprometidos | 19 |
| Story Points planificados | 70 |
| Story Points completados | 70 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US19 | Consulta de la matriz en campo | Ambas | 3 | Completado |
| US20 | Registro de peligros | Web | 5 | Completado |
| US21 | Versionado de la matriz | Web | 5 | Completado |
| US22 | Trazabilidad con el hallazgo de origen | Ambas | 3 | Completado |
| US52 | Consultar versiones anteriores de la matriz | Web | 5 | Completado |
| US53 | Publicar una nueva versión de la matriz | Web | 5 | Completado |
| US54 | Retirar un peligro de la matriz | Web | 2 | Completado |
| US23 | Catálogo de EPP | Web | 3 | Completado |
| US24 | Registro de entrega | Web | 3 | Completado |
| US25 | Conformidad del trabajador | Ambas | 3 | Completado |
| US26 | Alerta de EPP vencido | Ambas | 2 | Completado |
| US55 | Control de stock del catálogo | Web | 2 | Completado |
| US27 | Programa de inspecciones | Web | 5 | Completado |
| US28 | Ejecución con checklist | Ambas | 5 | Completado |
| US29 | Inspecciones vencidas | Ambas | 3 | Completado |
| US56 | Programar la siguiente inspección | Web | 3 | Completado |
| US36 | Tasa de cumplimiento de inspecciones | Ambas | 5 | Completado |
| US57 | Cumplimiento por área | Web | 3 | Completado |
| TS04 | Datos de demostración | sst-api | 5 | Completado |

**Sprint 6**

| Campo | Valor |
|---|---|
| Objetivo | Comité de SST, evidencia exportable y calidad de uso. |
| Elementos comprometidos | 20 |
| Story Points planificados | 72 |
| Story Points completados | 72 |

| ID | Historia | Plataforma | SP | Estado |
|---|---|---|---|---|
| US30 | Constitución del comité | Web | 3 | Completado |
| US31 | Miembros y paridad | Web | 5 | Completado |
| US32 | Acta de reunión | Web | 5 | Completado |
| US33 | Control de quórum | Ambas | 3 | Completado |
| US34 | Acuerdos con responsable y plazo | Web | 3 | Completado |
| US58 | Advertencia de comité no paritario | Web | 2 | Completado |
| US59 | Seguimiento del estado de los acuerdos | Web | 2 | Completado |
| US60 | Consultar las actas desde el celular | Móvil | 3 | Completado |
| US37 | Exportación de evidencia | Web | 8 | Completado |
| US61 | MTTR por severidad | Ambas | 3 | Completado |
| US62 | Exportar cada registro obligatorio | Web | 3 | Completado |
| US63 | Resumen de hallazgos | Ambas | 3 | Completado |
| US65 | Identidad visual consistente | Ambas | 5 | Completado |
| US66 | Navegación siempre accesible | Ambas | 2 | Completado |
| US67 | Uso desde pantallas pequeñas | Web | 5 | Completado |
| US68 | Errores comprensibles | Ambas | 3 | Completado |
| US69 | Reintento ante fallo de red | Móvil | 3 | Completado |
| TS14 | APK publicado por el pipeline | sst-mobile | 3 | Completado |
| TS15 | Generación de evidencia en Excel | sst-api | 5 | Completado |
| TS16 | Informe compilable y con índice verificado | sst-report | 3 | Completado |

**Resumen de los seis sprints**

| Sprint | Elementos | Story Points | Objetivo |
|---|---|---|---|
| Sprint 1 | 11 | 52 | Que un operario pueda entrar y registrar un hallazgo, con o sin señal. |
| Sprint 2 | 12 | 48 | Cerrar el ciclo del hallazgo: recibirlo, asignarlo y cerrarlo con evidencia. |
| Sprint 3 | 14 | 47 | Completar la captura y dejar el experimento A/B corriendo. |
| Sprint 4 | 10 | 30 | Cuentas, roles y estructura organizativa de la empresa. |
| Sprint 5 | 19 | 70 | Los registros obligatorios del SGSST: IPERC, EPP e inspecciones. |
| Sprint 6 | 20 | 72 | Comité de SST, evidencia exportable y calidad de uso. |
| **Total** | **86** | **319** | |

### 5.2.2. Implemented Landing Page Evidence

> **PENDIENTE — fuera del alcance de este ciclo.** La landing page no forma parte de la
> aplicación web: se construye en un repositorio propio, por las razones expuestas en la sección
> 4.3. Al cierre de estos seis sprints todavía no está implementada, de modo que no hay evidencia
> que presentar aquí. La estructura prevista y las restricciones de contenido quedan
> especificadas en 4.3.1.

<!-- IMAGEN REQUERIDA: capturas de la landing page desplegada en
     assets/img/evidencia-landing-*.png, más su URL pública, una vez construida. -->

### 5.2.3. Implemented Frontend-Web Application Evidence

<!-- IMAGEN REQUERIDA: capturas del panel web en ejecución, una por pantalla, en
     assets/img/evidencia-web-<pantalla>.png. Lista sugerida:
     acceso, registro, tablero, bandeja de hallazgos, detalle con bitácora, matriz IPERC,
     inspecciones con checklist, EPP, comité con actas, usuarios, experimento A/B. -->

La aplicación web está implementada en React con TypeScript y cubre la totalidad de las
funcionalidades disponibles para los roles de supervisor y comité, además del reporte para
cualquier rol.

| Pantalla | Ruta | Funcionalidad implementada |
|---|---|---|
| Acceso | `/login` | Autenticación con JWT |
| Registro | `/registro` | Alta de trabajador por RUC de empresa |
| Tablero | `/` | MTTR, hallazgos abiertos, cumplimiento de inspecciones, vencidas, acuerdos y actas del comité |
| Reportes | `/reportes` | Bandeja filtrable por estado, tipo y área |
| Nuevo reporte | `/reportes/nuevo` | Formulario en sus dos variantes del experimento, con foto, vista previa ampliable y captura de ubicación |
| Detalle | `/reportes/:id` | Datos completos, bitácora, asignación de responsable y cierre con acción correctiva |
| Matriz IPERC | `/iperc` | Consulta y edición de entradas con cálculo del nivel de riesgo |
| Inspecciones | `/inspecciones` | Programas, generación de ocurrencias, ejecución con checklist e indicadores |
| EPP | `/epp` | Catálogo, registro de entregas y conformidad del trabajador |
| Comité | `/comite` | Constitución, miembros, paridad, actas con quórum y acuerdos |
| Usuarios y áreas | `/usuarios` | Alta de usuarios con rol y gestión de áreas |
| Experimento | `/experimento` | Resultados comparados por variante |

### 5.2.4. Acuerdo de Servicio - SaaS

> **PENDIENTE.** Redactar el acuerdo de nivel de servicio del producto como SaaS: disponibilidad
> comprometida, ventana de mantenimiento, tiempos de respuesta ante incidencias por severidad,
> política de respaldo y retención de datos, tratamiento de datos personales conforme a la Ley
> N° 29733 de Protección de Datos Personales —relevante porque el sistema almacena DNI,
> fotografías y geolocalización de trabajadores— y condiciones de terminación con devolución de
> la información del cliente.

### 5.2.5. Implemented Native-Mobile Application Evidence

<!-- IMAGEN REQUERIDA: capturas de la aplicación Android en ejecución en
     assets/img/evidencia-movil-<pantalla>.png. Lista sugerida: acceso, registro, formulario
     rápido en sus tres pasos, formulario largo, lista de reportes con pendientes de envío,
     detalle del hallazgo, IPERC, mis EPP, inspecciones con checklist, tablero. -->

| Pantalla | Funcionalidad implementada |
|---|---|
| Acceso y registro | Autenticación JWT y alta de trabajador por RUC |
| Reportar | Formulario rápido de tres pasos y formulario largo, según la variante asignada |
| Mis reportes | Cola local con estado de envío y listado del servidor con filtros |
| Detalle del hallazgo | Bitácora, foto, tiempo de resolución; asignación y cierre para supervisor y comité |
| Matriz IPERC | Consulta de peligros y controles por puesto |
| Mis EPP | Entregas, vencimientos y conformidad del trabajador |
| Inspecciones | Listado y ejecución con checklist |
| Tablero | MTTR, cumplimiento de inspecciones y acuerdos del comité |

> **PENDIENTE — compilación.** Adjuntar evidencia de la compilación exitosa y el APK de
> depuración generado por el pipeline, más capturas en dispositivo o emulador.

### 5.2.6. Implemented RESTful API and/or Serverless Backend Evidence

El API expone 8 módulos de dominio bajo el prefijo `/api/v1/`.

| Módulo | Endpoints principales |
|---|---|
| Autenticación | `POST auth/register/`, `POST auth/login/`, `POST auth/refresh/`, `GET auth/me/`, CRUD `auth/users/`, CRUD `auth/areas/` |
| Reportes | CRUD `reports/`, `POST reports/{id}/assign/`, `POST reports/{id}/close/`, `POST reports/{id}/change-status/`, CRUD `categories/` |
| IPERC | CRUD `iperc/matrices/`, CRUD `iperc/entries/` |
| EPP | CRUD `epp/items/`, CRUD `epp/deliveries/` |
| Inspecciones | CRUD `inspections/schedules/`, `POST inspections/schedules/{id}/generate-next/`, CRUD `inspections/`, `POST inspections/{id}/complete/` |
| Comité | CRUD `committee/`, `committee/members/`, `committee/meetings/`, `committee/agreements/`, `GET committee-compliance/` |
| Métricas | `GET metrics/mttr/`, `GET metrics/inspection-compliance/`, `GET metrics/reports-summary/` |
| Experimento | `GET experiments/my-variant/`, `GET experiments/{key}/results/` |
| Exportación | `GET exports/reports.xlsx`, `iperc.xlsx`, `epp.xlsx`, `inspections.xlsx`, `committee.xlsx` |

**Dos decisiones de implementación que conviene destacar en la sustentación:**

*Idempotencia en la creación de reportes.* `POST reports/` recibe un `client_uuid` generado por
el dispositivo antes del envío. Si el reporte con ese identificador ya existe, el API responde
`200` con el reporte existente en lugar de crear uno nuevo y responder `201`. Sin esta decisión,
un reintento tras una conexión interrumpida —el caso normal en obra— duplicaría el hallazgo y
distorsionaría todas las métricas.

*El rol no se acepta del cliente.* El registro público fuerza el rol `OPERARIO`. Si se aceptara
del cliente, cualquiera podría registrarse como supervisor y cerrar sus propios hallazgos,
rompiendo la separación de responsabilidades que la normativa exige. Los usuarios con otros
roles se crean desde `auth/users/`, que requiere ser supervisor o miembro del comité.

<!-- IMAGEN REQUERIDA: captura de la interfaz Swagger en /api/docs/ mostrando los módulos
     desplegados, en assets/img/evidencia-api-swagger.png -->

### 5.2.7. RESTful API documentation

La documentación se genera automáticamente desde el código con drf-spectacular, de modo que el
contrato publicado no puede divergir de la implementación.

| Recurso | Ruta |
|---|---|
| Interfaz interactiva (Swagger UI) | `/api/docs/` |
| Especificación OpenAPI 3 | `/api/schema/` |

Todos los endpoints requieren autenticación JWT mediante la cabecera `Authorization: Bearer
<token>`, con la excepción de `auth/register/`, `auth/login/` y `auth/refresh/`.

### 5.2.8. Team Collaboration Insights

<!-- IMAGEN REQUERIDA: capturas de GitHub → Insights → Contributors y Commits de cada uno de
     los cuatro repositorios, en assets/img/insights-<repo>.png -->

> **PENDIENTE.** Incluir, por cada repositorio, la captura de los analíticos de colaboración y
> una descripción de cómo se distribuyó el trabajo. El historial de commits debe ser coherente
> con lo declarado en el Registro de Versiones del Informe y en el Participant Performance
> Report.

## 5.3. Video About-the-Product

> **PENDIENTE.** <!-- COMPLETAR: enlace al video y descripción del contenido. El video debe
> mostrar el producto en operación cubriendo el escenario principal: el operario reporta un
> hallazgo desde el celular, el supervisor lo recibe en el panel, lo asigna y lo cierra, y el
> indicador MTTR se actualiza. Duración sugerida: entre 3 y 5 minutos. -->
