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

## 5.2. Product Implementation & Deployment

### 5.2.1. Sprint Backlogs

El ciclo se organizó en dos sprints. El Capítulo III contiene el catálogo completo de las 128
historias de usuario y las 34 historias técnicas, con su Product Backlog priorizado; esta sección
toma de ese backlog únicamente lo que cada sprint se comprometió a entregar y lo **desglosa en
work-items**: la tarea concreta, su estimación en horas y el área responsable.

**Criterio de división.** El Sprint 1 cierra el **ciclo de vida de un hallazgo** de extremo a
extremo: que el operario lo registre con evidencia y que el supervisor lo reciba, lo asigne y lo
cierre. El Sprint 2 construye sobre ese cimiento **el resto del sistema de gestión**: la matriz
IPERC, el control de EPP, las inspecciones, el comité, las métricas y la evidencia exportable, más
las cuentas, los roles y la calidad de uso. Sin el ciclo del hallazgo funcionando, ninguno de los
registros del Sprint 2 tendría de dónde alimentarse.

**Cómo se desglosó cada historia.** Una historia de usuario no es una tarea: atraviesa el API, la
web y el móvil. El desglose sigue esa estructura, de modo que cada work-item cae en un único
repositorio y en una única área responsable:

| Plataforma de la historia | Work-items que genera |
|---|---|
| `Ambas` | Lógica y endpoint en el API · interfaz en el panel web · interfaz en Android · pruebas automatizadas |
| `Web` | Lógica y endpoint en el API · interfaz en el panel web · pruebas automatizadas |
| `Móvil` | Lógica y endpoint en el API · interfaz en Android · pruebas automatizadas |
| `—` (sin interfaz) | Lógica en el API · pruebas automatizadas |
| Historia técnica | Configuración · verificación en el pipeline |

**Cómo se estimaron las horas.** Cada Story Point equivale a **2 horas** de trabajo, y las horas
de la historia se reparten entre sus work-items según el peso de cada capa. La conversión es una
regla declarada, no una medición: sirve para dimensionar el esfuerzo relativo entre tareas, no para
afirmar cuánto tardó realmente cada una.

---

#### Sprint 1

| Campo | Valor |
|---|---|
| Objetivo | Cerrar el ciclo del hallazgo de extremo a extremo: registrarlo en campo con evidencia, recibirlo, asignarlo y cerrarlo con la acción correctiva aplicada. |
| Elementos del backlog comprometidos | 15 |
| Story Points | 60 |
| Work-items | 54 |
| Horas estimadas | 120 |
| Incremento entregable | Un operario registra un acto o condición insegura con foto, ubicación y fecha real desde el celular o la web; el supervisor lo ve en su bandeja, lo asigna y lo cierra; la bitácora queda con quién hizo qué y cuándo. |

Las doce historias de usuario de este sprint están marcadas `Ambas` en el Capítulo III: el
incremento es demostrable tanto desde el panel web como desde la aplicación Android, que es la
condición de paridad que el proyecto se impuso.

| Sprint | User Story | Título | Work-Item | Descripción de la tarea | Estimación (h) | Área responsable | Estado |
|---|---|---|---|---|---|---|---|
| Sprint 1 | US02 | Inicio de sesión | Sprint1-T01 | Implementar en el API la lógica y el endpoint de «Inicio de sesión» | 1 | Backend | Terminado |
| Sprint 1 | US02 | Inicio de sesión | Sprint1-T02 | Construir en el panel web la interfaz de «Inicio de sesión» | 2 | Web | Terminado |
| Sprint 1 | US02 | Inicio de sesión | Sprint1-T03 | Construir en la aplicación Android la interfaz de «Inicio de sesión» | 2 | Móvil | Terminado |
| Sprint 1 | US02 | Inicio de sesión | Sprint1-T04 | Cubrir «Inicio de sesión» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US06 | Reporte rápido desde el celular | Sprint1-T05 | Implementar en el API la lógica y el endpoint de «Reporte rápido desde el celular» | 4 | Backend | Terminado |
| Sprint 1 | US06 | Reporte rápido desde el celular | Sprint1-T06 | Construir en el panel web la interfaz de «Reporte rápido desde el celular» | 5 | Web | Terminado |
| Sprint 1 | US06 | Reporte rápido desde el celular | Sprint1-T07 | Construir en la aplicación Android la interfaz de «Reporte rápido desde el celular» | 5 | Móvil | Terminado |
| Sprint 1 | US06 | Reporte rápido desde el celular | Sprint1-T08 | Cubrir «Reporte rápido desde el celular» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 1 | US13 | Consulta de mis reportes | Sprint1-T09 | Implementar en el API la lógica y el endpoint de «Consulta de mis reportes» | 1 | Backend | Terminado |
| Sprint 1 | US13 | Consulta de mis reportes | Sprint1-T10 | Construir en el panel web la interfaz de «Consulta de mis reportes» | 2 | Web | Terminado |
| Sprint 1 | US13 | Consulta de mis reportes | Sprint1-T11 | Construir en la aplicación Android la interfaz de «Consulta de mis reportes» | 2 | Móvil | Terminado |
| Sprint 1 | US13 | Consulta de mis reportes | Sprint1-T12 | Cubrir «Consulta de mis reportes» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US43 | Menú según mi rol | Sprint1-T13 | Implementar en el API la lógica y el endpoint de «Menú según mi rol» | 1 | Backend | Terminado |
| Sprint 1 | US43 | Menú según mi rol | Sprint1-T14 | Construir en el panel web la interfaz de «Menú según mi rol» | 2 | Web | Terminado |
| Sprint 1 | US43 | Menú según mi rol | Sprint1-T15 | Construir en la aplicación Android la interfaz de «Menú según mi rol» | 2 | Móvil | Terminado |
| Sprint 1 | US43 | Menú según mi rol | Sprint1-T16 | Cubrir «Menú según mi rol» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US14 | Bandeja de hallazgos | Sprint1-T17 | Implementar en el API la lógica y el endpoint de «Bandeja de hallazgos» | 3 | Backend | Terminado |
| Sprint 1 | US14 | Bandeja de hallazgos | Sprint1-T18 | Construir en el panel web la interfaz de «Bandeja de hallazgos» | 3 | Web | Terminado |
| Sprint 1 | US14 | Bandeja de hallazgos | Sprint1-T19 | Construir en la aplicación Android la interfaz de «Bandeja de hallazgos» | 3 | Móvil | Terminado |
| Sprint 1 | US14 | Bandeja de hallazgos | Sprint1-T20 | Cubrir «Bandeja de hallazgos» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US16 | Cierre con acción correctiva | Sprint1-T21 | Implementar en el API la lógica y el endpoint de «Cierre con acción correctiva» | 3 | Backend | Terminado |
| Sprint 1 | US16 | Cierre con acción correctiva | Sprint1-T22 | Construir en el panel web la interfaz de «Cierre con acción correctiva» | 3 | Web | Terminado |
| Sprint 1 | US16 | Cierre con acción correctiva | Sprint1-T23 | Construir en la aplicación Android la interfaz de «Cierre con acción correctiva» | 3 | Móvil | Terminado |
| Sprint 1 | US16 | Cierre con acción correctiva | Sprint1-T24 | Cubrir «Cierre con acción correctiva» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US15 | Asignación de responsable | Sprint1-T25 | Implementar en el API la lógica y el endpoint de «Asignación de responsable» | 3 | Backend | Terminado |
| Sprint 1 | US15 | Asignación de responsable | Sprint1-T26 | Construir en el panel web la interfaz de «Asignación de responsable» | 3 | Web | Terminado |
| Sprint 1 | US15 | Asignación de responsable | Sprint1-T27 | Construir en la aplicación Android la interfaz de «Asignación de responsable» | 3 | Móvil | Terminado |
| Sprint 1 | US15 | Asignación de responsable | Sprint1-T28 | Cubrir «Asignación de responsable» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US18 | Bitácora del hallazgo | Sprint1-T29 | Implementar en el API la lógica y el endpoint de «Bitácora del hallazgo» | 1 | Backend | Terminado |
| Sprint 1 | US18 | Bitácora del hallazgo | Sprint1-T30 | Construir en el panel web la interfaz de «Bitácora del hallazgo» | 2 | Web | Terminado |
| Sprint 1 | US18 | Bitácora del hallazgo | Sprint1-T31 | Construir en la aplicación Android la interfaz de «Bitácora del hallazgo» | 2 | Móvil | Terminado |
| Sprint 1 | US18 | Bitácora del hallazgo | Sprint1-T32 | Cubrir «Bitácora del hallazgo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US09 | Evidencia fotográfica | Sprint1-T33 | Implementar en el API la lógica y el endpoint de «Evidencia fotográfica» | 3 | Backend | Terminado |
| Sprint 1 | US09 | Evidencia fotográfica | Sprint1-T34 | Construir en el panel web la interfaz de «Evidencia fotográfica» | 3 | Web | Terminado |
| Sprint 1 | US09 | Evidencia fotográfica | Sprint1-T35 | Construir en la aplicación Android la interfaz de «Evidencia fotográfica» | 3 | Móvil | Terminado |
| Sprint 1 | US09 | Evidencia fotográfica | Sprint1-T36 | Cubrir «Evidencia fotográfica» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US10 | Geolocalización del hallazgo | Sprint1-T37 | Implementar en el API la lógica y el endpoint de «Geolocalización del hallazgo» | 3 | Backend | Terminado |
| Sprint 1 | US10 | Geolocalización del hallazgo | Sprint1-T38 | Construir en el panel web la interfaz de «Geolocalización del hallazgo» | 3 | Web | Terminado |
| Sprint 1 | US10 | Geolocalización del hallazgo | Sprint1-T39 | Construir en la aplicación Android la interfaz de «Geolocalización del hallazgo» | 3 | Móvil | Terminado |
| Sprint 1 | US10 | Geolocalización del hallazgo | Sprint1-T40 | Cubrir «Geolocalización del hallazgo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US11 | Fecha real de ocurrencia | Sprint1-T41 | Implementar en el API la lógica y el endpoint de «Fecha real de ocurrencia» | 1 | Backend | Terminado |
| Sprint 1 | US11 | Fecha real de ocurrencia | Sprint1-T42 | Construir en el panel web la interfaz de «Fecha real de ocurrencia» | 2 | Web | Terminado |
| Sprint 1 | US11 | Fecha real de ocurrencia | Sprint1-T43 | Construir en la aplicación Android la interfaz de «Fecha real de ocurrencia» | 2 | Móvil | Terminado |
| Sprint 1 | US11 | Fecha real de ocurrencia | Sprint1-T44 | Cubrir «Fecha real de ocurrencia» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | US47 | Categorías según el tipo de hallazgo | Sprint1-T45 | Implementar en el API la lógica y el endpoint de «Categorías según el tipo de hallazgo» | 1 | Backend | Terminado |
| Sprint 1 | US47 | Categorías según el tipo de hallazgo | Sprint1-T46 | Construir en el panel web la interfaz de «Categorías según el tipo de hallazgo» | 1 | Web | Terminado |
| Sprint 1 | US47 | Categorías según el tipo de hallazgo | Sprint1-T47 | Construir en la aplicación Android la interfaz de «Categorías según el tipo de hallazgo» | 1 | Móvil | Terminado |
| Sprint 1 | US47 | Categorías según el tipo de hallazgo | Sprint1-T48 | Cubrir «Categorías según el tipo de hallazgo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 1 | TS02 | Convenciones de commits | Sprint1-T49 | Configurar «Convenciones de commits» | 3 | DevOps | Terminado |
| Sprint 1 | TS02 | Convenciones de commits | Sprint1-T50 | Verificar «Convenciones de commits» en el pipeline | 1 | DevOps | Terminado |
| Sprint 1 | TS05 | Flujo de ramas GitFlow | Sprint1-T51 | Configurar «Flujo de ramas GitFlow» | 4 | DevOps | Terminado |
| Sprint 1 | TS05 | Flujo de ramas GitFlow | Sprint1-T52 | Verificar «Flujo de ramas GitFlow» en el pipeline | 2 | DevOps | Terminado |
| Sprint 1 | TS01 | Integración continua | Sprint1-T53 | Configurar «Integración continua» | 7 | DevOps | Terminado |
| Sprint 1 | TS01 | Integración continua | Sprint1-T54 | Verificar «Integración continua» en el pipeline | 3 | DevOps | Terminado |

---

#### Sprint 2

| Campo | Valor |
|---|---|
| Objetivo | Completar el sistema de gestión sobre el ciclo del hallazgo ya funcionando: matriz IPERC, control de EPP, inspecciones, comité de SST, métricas, evidencia exportable, cuentas y calidad de uso. |
| Elementos del backlog comprometidos | 71 |
| Story Points | 259 |
| Work-items | 220 |
| Horas estimadas | 518 |
| Incremento entregable | El supervisor y el comité disponen de los registros obligatorios de la Ley N° 29783 en el sistema: peligros evaluados y versionados, entregas de EPP con conformidad, inspecciones programadas y ejecutadas con checklist, actas del comité con quórum y acuerdos, indicadores de gestión y exportación de la evidencia a Excel. |

| Sprint | User Story | Título | Work-Item | Descripción de la tarea | Estimación (h) | Área responsable | Estado |
|---|---|---|---|---|---|---|---|
| Sprint 2 | US07 | Reporte sin conexión | Sprint2-T01 | Implementar en el API la lógica y el endpoint de «Reporte sin conexión» | 9 | Backend | Terminado |
| Sprint 2 | US07 | Reporte sin conexión | Sprint2-T02 | Construir en la aplicación Android la interfaz de «Reporte sin conexión» | 12 | Móvil | Terminado |
| Sprint 2 | US07 | Reporte sin conexión | Sprint2-T03 | Cubrir «Reporte sin conexión» con pruebas automatizadas | 5 | QA | Terminado |
| Sprint 2 | US08 | Sincronización sin duplicados | Sprint2-T04 | Implementar en el API la lógica y el endpoint de «Sincronización sin duplicados» | 4 | Backend | Terminado |
| Sprint 2 | US08 | Sincronización sin duplicados | Sprint2-T05 | Construir en el panel web la interfaz de «Sincronización sin duplicados» | 5 | Web | Terminado |
| Sprint 2 | US08 | Sincronización sin duplicados | Sprint2-T06 | Construir en la aplicación Android la interfaz de «Sincronización sin duplicados» | 5 | Móvil | Terminado |
| Sprint 2 | US08 | Sincronización sin duplicados | Sprint2-T07 | Cubrir «Sincronización sin duplicados» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US70 | Sesión que no expira en campo | Sprint2-T08 | Implementar en el API la lógica y el endpoint de «Sesión que no expira en campo» | 3 | Backend | Terminado |
| Sprint 2 | US70 | Sesión que no expira en campo | Sprint2-T09 | Construir en el panel web la interfaz de «Sesión que no expira en campo» | 3 | Web | Terminado |
| Sprint 2 | US70 | Sesión que no expira en campo | Sprint2-T10 | Construir en la aplicación Android la interfaz de «Sesión que no expira en campo» | 3 | Móvil | Terminado |
| Sprint 2 | US70 | Sesión que no expira en campo | Sprint2-T11 | Cubrir «Sesión que no expira en campo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US17 | Separación de responsabilidades | Sprint2-T12 | Implementar en el API la lógica y el endpoint de «Separación de responsabilidades» | 1 | Backend | Terminado |
| Sprint 2 | US17 | Separación de responsabilidades | Sprint2-T13 | Construir en el panel web la interfaz de «Separación de responsabilidades» | 2 | Web | Terminado |
| Sprint 2 | US17 | Separación de responsabilidades | Sprint2-T14 | Construir en la aplicación Android la interfaz de «Separación de responsabilidades» | 2 | Móvil | Terminado |
| Sprint 2 | US17 | Separación de responsabilidades | Sprint2-T15 | Cubrir «Separación de responsabilidades» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US35 | Indicador MTTR | Sprint2-T16 | Implementar en el API la lógica y el endpoint de «Indicador MTTR» | 3 | Backend | Terminado |
| Sprint 2 | US35 | Indicador MTTR | Sprint2-T17 | Construir en el panel web la interfaz de «Indicador MTTR» | 3 | Web | Terminado |
| Sprint 2 | US35 | Indicador MTTR | Sprint2-T18 | Construir en la aplicación Android la interfaz de «Indicador MTTR» | 3 | Móvil | Terminado |
| Sprint 2 | US35 | Indicador MTTR | Sprint2-T19 | Cubrir «Indicador MTTR» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US50 | Filtrar la bandeja | Sprint2-T20 | Implementar en el API la lógica y el endpoint de «Filtrar la bandeja» | 1 | Backend | Terminado |
| Sprint 2 | US50 | Filtrar la bandeja | Sprint2-T21 | Construir en el panel web la interfaz de «Filtrar la bandeja» | 2 | Web | Terminado |
| Sprint 2 | US50 | Filtrar la bandeja | Sprint2-T22 | Construir en la aplicación Android la interfaz de «Filtrar la bandeja» | 2 | Móvil | Terminado |
| Sprint 2 | US50 | Filtrar la bandeja | Sprint2-T23 | Cubrir «Filtrar la bandeja» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US49 | Descartar un reporte | Sprint2-T24 | Implementar en el API la lógica y el endpoint de «Descartar un reporte» | 1 | Backend | Terminado |
| Sprint 2 | US49 | Descartar un reporte | Sprint2-T25 | Construir en el panel web la interfaz de «Descartar un reporte» | 2 | Web | Terminado |
| Sprint 2 | US49 | Descartar un reporte | Sprint2-T26 | Cubrir «Descartar un reporte» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US12 | Reporte desde la web | Sprint2-T27 | Implementar en el API la lógica y el endpoint de «Reporte desde la web» | 4 | Backend | Terminado |
| Sprint 2 | US12 | Reporte desde la web | Sprint2-T28 | Construir en el panel web la interfaz de «Reporte desde la web» | 4 | Web | Terminado |
| Sprint 2 | US12 | Reporte desde la web | Sprint2-T29 | Cubrir «Reporte desde la web» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US44 | Vista previa de la evidencia | Sprint2-T30 | Implementar en el API la lógica y el endpoint de «Vista previa de la evidencia» | 2 | Backend | Terminado |
| Sprint 2 | US44 | Vista previa de la evidencia | Sprint2-T31 | Construir en el panel web la interfaz de «Vista previa de la evidencia» | 3 | Web | Terminado |
| Sprint 2 | US44 | Vista previa de la evidencia | Sprint2-T32 | Cubrir «Vista previa de la evidencia» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US45 | Ampliar la evidencia | Sprint2-T33 | Implementar en el API la lógica y el endpoint de «Ampliar la evidencia» | 2 | Backend | Terminado |
| Sprint 2 | US45 | Ampliar la evidencia | Sprint2-T34 | Construir en el panel web la interfaz de «Ampliar la evidencia» | 3 | Web | Terminado |
| Sprint 2 | US45 | Ampliar la evidencia | Sprint2-T35 | Cubrir «Ampliar la evidencia» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US46 | Reemplazar la foto elegida | Sprint2-T36 | Implementar en el API la lógica y el endpoint de «Reemplazar la foto elegida» | 1 | Backend | Terminado |
| Sprint 2 | US46 | Reemplazar la foto elegida | Sprint2-T37 | Construir en el panel web la interfaz de «Reemplazar la foto elegida» | 2 | Web | Terminado |
| Sprint 2 | US46 | Reemplazar la foto elegida | Sprint2-T38 | Cubrir «Reemplazar la foto elegida» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US48 | Estado de envío de mis reportes | Sprint2-T39 | Implementar en el API la lógica y el endpoint de «Estado de envío de mis reportes» | 2 | Backend | Terminado |
| Sprint 2 | US48 | Estado de envío de mis reportes | Sprint2-T40 | Construir en la aplicación Android la interfaz de «Estado de envío de mis reportes» | 3 | Móvil | Terminado |
| Sprint 2 | US48 | Estado de envío de mis reportes | Sprint2-T41 | Cubrir «Estado de envío de mis reportes» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US51 | Ubicar el hallazgo en el mapa | Sprint2-T42 | Implementar en el API la lógica y el endpoint de «Ubicar el hallazgo en el mapa» | 1 | Backend | Terminado |
| Sprint 2 | US51 | Ubicar el hallazgo en el mapa | Sprint2-T43 | Construir en el panel web la interfaz de «Ubicar el hallazgo en el mapa» | 1 | Web | Terminado |
| Sprint 2 | US38 | Asignación de variante | Sprint2-T44 | Implementar en el API la lógica y el endpoint de «Asignación de variante» | 3 | Backend | Terminado |
| Sprint 2 | US38 | Asignación de variante | Sprint2-T45 | Construir en el panel web la interfaz de «Asignación de variante» | 3 | Web | Terminado |
| Sprint 2 | US38 | Asignación de variante | Sprint2-T46 | Construir en la aplicación Android la interfaz de «Asignación de variante» | 3 | Móvil | Terminado |
| Sprint 2 | US38 | Asignación de variante | Sprint2-T47 | Cubrir «Asignación de variante» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US39 | Registro de la variante en el reporte | Sprint2-T48 | Implementar en el API la lógica y el endpoint de «Registro de la variante en el reporte» | 1 | Backend | Terminado |
| Sprint 2 | US39 | Registro de la variante en el reporte | Sprint2-T49 | Construir en el panel web la interfaz de «Registro de la variante en el reporte» | 1 | Web | Terminado |
| Sprint 2 | US39 | Registro de la variante en el reporte | Sprint2-T50 | Construir en la aplicación Android la interfaz de «Registro de la variante en el reporte» | 1 | Móvil | Terminado |
| Sprint 2 | US39 | Registro de la variante en el reporte | Sprint2-T51 | Cubrir «Registro de la variante en el reporte» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US40 | Resultados del experimento | Sprint2-T52 | Implementar en el API la lógica y el endpoint de «Resultados del experimento» | 4 | Backend | Terminado |
| Sprint 2 | US40 | Resultados del experimento | Sprint2-T53 | Construir en el panel web la interfaz de «Resultados del experimento» | 4 | Web | Terminado |
| Sprint 2 | US40 | Resultados del experimento | Sprint2-T54 | Cubrir «Resultados del experimento» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US64 | Variante disponible sin conexión | Sprint2-T55 | Implementar en el API la lógica y el endpoint de «Variante disponible sin conexión» | 2 | Backend | Terminado |
| Sprint 2 | US64 | Variante disponible sin conexión | Sprint2-T56 | Construir en la aplicación Android la interfaz de «Variante disponible sin conexión» | 3 | Móvil | Terminado |
| Sprint 2 | US64 | Variante disponible sin conexión | Sprint2-T57 | Cubrir «Variante disponible sin conexión» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US01 | Registro de trabajador | Sprint2-T58 | Implementar en el API la lógica y el endpoint de «Registro de trabajador» | 3 | Backend | Terminado |
| Sprint 2 | US01 | Registro de trabajador | Sprint2-T59 | Construir en el panel web la interfaz de «Registro de trabajador» | 3 | Web | Terminado |
| Sprint 2 | US01 | Registro de trabajador | Sprint2-T60 | Construir en la aplicación Android la interfaz de «Registro de trabajador» | 3 | Móvil | Terminado |
| Sprint 2 | US01 | Registro de trabajador | Sprint2-T61 | Cubrir «Registro de trabajador» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US03 | Sesión persistente en campo | Sprint2-T62 | Implementar en el API la lógica y el endpoint de «Sesión persistente en campo» | 1 | Backend | Terminado |
| Sprint 2 | US03 | Sesión persistente en campo | Sprint2-T63 | Construir en el panel web la interfaz de «Sesión persistente en campo» | 2 | Web | Terminado |
| Sprint 2 | US03 | Sesión persistente en campo | Sprint2-T64 | Construir en la aplicación Android la interfaz de «Sesión persistente en campo» | 2 | Móvil | Terminado |
| Sprint 2 | US03 | Sesión persistente en campo | Sprint2-T65 | Cubrir «Sesión persistente en campo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US05 | Gestión de áreas | Sprint2-T66 | Implementar en el API la lógica y el endpoint de «Gestión de áreas» | 1 | Backend | Terminado |
| Sprint 2 | US05 | Gestión de áreas | Sprint2-T67 | Construir en el panel web la interfaz de «Gestión de áreas» | 2 | Web | Terminado |
| Sprint 2 | US05 | Gestión de áreas | Sprint2-T68 | Cubrir «Gestión de áreas» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US04 | Administración de usuarios | Sprint2-T69 | Implementar en el API la lógica y el endpoint de «Administración de usuarios» | 4 | Backend | Terminado |
| Sprint 2 | US04 | Administración de usuarios | Sprint2-T70 | Construir en el panel web la interfaz de «Administración de usuarios» | 4 | Web | Terminado |
| Sprint 2 | US04 | Administración de usuarios | Sprint2-T71 | Cubrir «Administración de usuarios» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US41 | Cambio de rol de un usuario | Sprint2-T72 | Implementar en el API la lógica y el endpoint de «Cambio de rol de un usuario» | 1 | Backend | Terminado |
| Sprint 2 | US41 | Cambio de rol de un usuario | Sprint2-T73 | Construir en el panel web la interfaz de «Cambio de rol de un usuario» | 2 | Web | Terminado |
| Sprint 2 | US41 | Cambio de rol de un usuario | Sprint2-T74 | Cubrir «Cambio de rol de un usuario» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US42 | Cierre de sesión | Sprint2-T75 | Implementar en el API la lógica y el endpoint de «Cierre de sesión» | 1 | Backend | Terminado |
| Sprint 2 | US42 | Cierre de sesión | Sprint2-T76 | Construir en el panel web la interfaz de «Cierre de sesión» | 1 | Web | Terminado |
| Sprint 2 | US19 | Consulta de la matriz en campo | Sprint2-T77 | Implementar en el API la lógica y el endpoint de «Consulta de la matriz en campo» | 1 | Backend | Terminado |
| Sprint 2 | US19 | Consulta de la matriz en campo | Sprint2-T78 | Construir en el panel web la interfaz de «Consulta de la matriz en campo» | 2 | Web | Terminado |
| Sprint 2 | US19 | Consulta de la matriz en campo | Sprint2-T79 | Construir en la aplicación Android la interfaz de «Consulta de la matriz en campo» | 2 | Móvil | Terminado |
| Sprint 2 | US19 | Consulta de la matriz en campo | Sprint2-T80 | Cubrir «Consulta de la matriz en campo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US20 | Registro de peligros | Sprint2-T81 | Implementar en el API la lógica y el endpoint de «Registro de peligros» | 4 | Backend | Terminado |
| Sprint 2 | US20 | Registro de peligros | Sprint2-T82 | Construir en el panel web la interfaz de «Registro de peligros» | 4 | Web | Terminado |
| Sprint 2 | US20 | Registro de peligros | Sprint2-T83 | Cubrir «Registro de peligros» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US21 | Versionado de la matriz | Sprint2-T84 | Implementar en el API la lógica y el endpoint de «Versionado de la matriz» | 4 | Backend | Terminado |
| Sprint 2 | US21 | Versionado de la matriz | Sprint2-T85 | Construir en el panel web la interfaz de «Versionado de la matriz» | 4 | Web | Terminado |
| Sprint 2 | US21 | Versionado de la matriz | Sprint2-T86 | Cubrir «Versionado de la matriz» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US22 | Trazabilidad con el hallazgo de origen | Sprint2-T87 | Implementar en el API la lógica y el endpoint de «Trazabilidad con el hallazgo de origen» | 1 | Backend | Terminado |
| Sprint 2 | US22 | Trazabilidad con el hallazgo de origen | Sprint2-T88 | Construir en el panel web la interfaz de «Trazabilidad con el hallazgo de origen» | 2 | Web | Terminado |
| Sprint 2 | US22 | Trazabilidad con el hallazgo de origen | Sprint2-T89 | Construir en la aplicación Android la interfaz de «Trazabilidad con el hallazgo de origen» | 2 | Móvil | Terminado |
| Sprint 2 | US22 | Trazabilidad con el hallazgo de origen | Sprint2-T90 | Cubrir «Trazabilidad con el hallazgo de origen» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US52 | Consultar versiones anteriores de la matriz | Sprint2-T91 | Implementar en el API la lógica y el endpoint de «Consultar versiones anteriores de la matriz» | 4 | Backend | Terminado |
| Sprint 2 | US52 | Consultar versiones anteriores de la matriz | Sprint2-T92 | Construir en el panel web la interfaz de «Consultar versiones anteriores de la matriz» | 4 | Web | Terminado |
| Sprint 2 | US52 | Consultar versiones anteriores de la matriz | Sprint2-T93 | Cubrir «Consultar versiones anteriores de la matriz» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US53 | Publicar una nueva versión de la matriz | Sprint2-T94 | Implementar en el API la lógica y el endpoint de «Publicar una nueva versión de la matriz» | 4 | Backend | Terminado |
| Sprint 2 | US53 | Publicar una nueva versión de la matriz | Sprint2-T95 | Construir en el panel web la interfaz de «Publicar una nueva versión de la matriz» | 4 | Web | Terminado |
| Sprint 2 | US53 | Publicar una nueva versión de la matriz | Sprint2-T96 | Cubrir «Publicar una nueva versión de la matriz» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US54 | Retirar un peligro de la matriz | Sprint2-T97 | Implementar en el API la lógica y el endpoint de «Retirar un peligro de la matriz» | 1 | Backend | Terminado |
| Sprint 2 | US54 | Retirar un peligro de la matriz | Sprint2-T98 | Construir en el panel web la interfaz de «Retirar un peligro de la matriz» | 2 | Web | Terminado |
| Sprint 2 | US54 | Retirar un peligro de la matriz | Sprint2-T99 | Cubrir «Retirar un peligro de la matriz» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US23 | Catálogo de EPP | Sprint2-T100 | Implementar en el API la lógica y el endpoint de «Catálogo de EPP» | 2 | Backend | Terminado |
| Sprint 2 | US23 | Catálogo de EPP | Sprint2-T101 | Construir en el panel web la interfaz de «Catálogo de EPP» | 3 | Web | Terminado |
| Sprint 2 | US23 | Catálogo de EPP | Sprint2-T102 | Cubrir «Catálogo de EPP» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US24 | Registro de entrega | Sprint2-T103 | Implementar en el API la lógica y el endpoint de «Registro de entrega» | 2 | Backend | Terminado |
| Sprint 2 | US24 | Registro de entrega | Sprint2-T104 | Construir en el panel web la interfaz de «Registro de entrega» | 3 | Web | Terminado |
| Sprint 2 | US24 | Registro de entrega | Sprint2-T105 | Cubrir «Registro de entrega» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US25 | Conformidad del trabajador | Sprint2-T106 | Implementar en el API la lógica y el endpoint de «Conformidad del trabajador» | 1 | Backend | Terminado |
| Sprint 2 | US25 | Conformidad del trabajador | Sprint2-T107 | Construir en el panel web la interfaz de «Conformidad del trabajador» | 2 | Web | Terminado |
| Sprint 2 | US25 | Conformidad del trabajador | Sprint2-T108 | Construir en la aplicación Android la interfaz de «Conformidad del trabajador» | 2 | Móvil | Terminado |
| Sprint 2 | US25 | Conformidad del trabajador | Sprint2-T109 | Cubrir «Conformidad del trabajador» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US26 | Alerta de EPP vencido | Sprint2-T110 | Implementar en el API la lógica y el endpoint de «Alerta de EPP vencido» | 1 | Backend | Terminado |
| Sprint 2 | US26 | Alerta de EPP vencido | Sprint2-T111 | Construir en el panel web la interfaz de «Alerta de EPP vencido» | 1 | Web | Terminado |
| Sprint 2 | US26 | Alerta de EPP vencido | Sprint2-T112 | Construir en la aplicación Android la interfaz de «Alerta de EPP vencido» | 1 | Móvil | Terminado |
| Sprint 2 | US26 | Alerta de EPP vencido | Sprint2-T113 | Cubrir «Alerta de EPP vencido» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US55 | Control de stock del catálogo | Sprint2-T114 | Implementar en el API la lógica y el endpoint de «Control de stock del catálogo» | 1 | Backend | Terminado |
| Sprint 2 | US55 | Control de stock del catálogo | Sprint2-T115 | Construir en el panel web la interfaz de «Control de stock del catálogo» | 2 | Web | Terminado |
| Sprint 2 | US55 | Control de stock del catálogo | Sprint2-T116 | Cubrir «Control de stock del catálogo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US27 | Programa de inspecciones | Sprint2-T117 | Implementar en el API la lógica y el endpoint de «Programa de inspecciones» | 4 | Backend | Terminado |
| Sprint 2 | US27 | Programa de inspecciones | Sprint2-T118 | Construir en el panel web la interfaz de «Programa de inspecciones» | 4 | Web | Terminado |
| Sprint 2 | US27 | Programa de inspecciones | Sprint2-T119 | Cubrir «Programa de inspecciones» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US28 | Ejecución con checklist | Sprint2-T120 | Implementar en el API la lógica y el endpoint de «Ejecución con checklist» | 3 | Backend | Terminado |
| Sprint 2 | US28 | Ejecución con checklist | Sprint2-T121 | Construir en el panel web la interfaz de «Ejecución con checklist» | 3 | Web | Terminado |
| Sprint 2 | US28 | Ejecución con checklist | Sprint2-T122 | Construir en la aplicación Android la interfaz de «Ejecución con checklist» | 3 | Móvil | Terminado |
| Sprint 2 | US28 | Ejecución con checklist | Sprint2-T123 | Cubrir «Ejecución con checklist» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US29 | Inspecciones vencidas | Sprint2-T124 | Implementar en el API la lógica y el endpoint de «Inspecciones vencidas» | 1 | Backend | Terminado |
| Sprint 2 | US29 | Inspecciones vencidas | Sprint2-T125 | Construir en el panel web la interfaz de «Inspecciones vencidas» | 2 | Web | Terminado |
| Sprint 2 | US29 | Inspecciones vencidas | Sprint2-T126 | Construir en la aplicación Android la interfaz de «Inspecciones vencidas» | 2 | Móvil | Terminado |
| Sprint 2 | US29 | Inspecciones vencidas | Sprint2-T127 | Cubrir «Inspecciones vencidas» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US56 | Programar la siguiente inspección | Sprint2-T128 | Implementar en el API la lógica y el endpoint de «Programar la siguiente inspección» | 2 | Backend | Terminado |
| Sprint 2 | US56 | Programar la siguiente inspección | Sprint2-T129 | Construir en el panel web la interfaz de «Programar la siguiente inspección» | 3 | Web | Terminado |
| Sprint 2 | US56 | Programar la siguiente inspección | Sprint2-T130 | Cubrir «Programar la siguiente inspección» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US36 | Tasa de cumplimiento de inspecciones | Sprint2-T131 | Implementar en el API la lógica y el endpoint de «Tasa de cumplimiento de inspecciones» | 3 | Backend | Terminado |
| Sprint 2 | US36 | Tasa de cumplimiento de inspecciones | Sprint2-T132 | Construir en el panel web la interfaz de «Tasa de cumplimiento de inspecciones» | 3 | Web | Terminado |
| Sprint 2 | US36 | Tasa de cumplimiento de inspecciones | Sprint2-T133 | Construir en la aplicación Android la interfaz de «Tasa de cumplimiento de inspecciones» | 3 | Móvil | Terminado |
| Sprint 2 | US36 | Tasa de cumplimiento de inspecciones | Sprint2-T134 | Cubrir «Tasa de cumplimiento de inspecciones» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US57 | Cumplimiento por área | Sprint2-T135 | Implementar en el API la lógica y el endpoint de «Cumplimiento por área» | 2 | Backend | Terminado |
| Sprint 2 | US57 | Cumplimiento por área | Sprint2-T136 | Construir en el panel web la interfaz de «Cumplimiento por área» | 3 | Web | Terminado |
| Sprint 2 | US57 | Cumplimiento por área | Sprint2-T137 | Cubrir «Cumplimiento por área» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US30 | Constitución del comité | Sprint2-T138 | Implementar en el API la lógica y el endpoint de «Constitución del comité» | 2 | Backend | Terminado |
| Sprint 2 | US30 | Constitución del comité | Sprint2-T139 | Construir en el panel web la interfaz de «Constitución del comité» | 3 | Web | Terminado |
| Sprint 2 | US30 | Constitución del comité | Sprint2-T140 | Cubrir «Constitución del comité» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US31 | Miembros y paridad | Sprint2-T141 | Implementar en el API la lógica y el endpoint de «Miembros y paridad» | 4 | Backend | Terminado |
| Sprint 2 | US31 | Miembros y paridad | Sprint2-T142 | Construir en el panel web la interfaz de «Miembros y paridad» | 4 | Web | Terminado |
| Sprint 2 | US31 | Miembros y paridad | Sprint2-T143 | Cubrir «Miembros y paridad» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US32 | Acta de reunión | Sprint2-T144 | Implementar en el API la lógica y el endpoint de «Acta de reunión» | 4 | Backend | Terminado |
| Sprint 2 | US32 | Acta de reunión | Sprint2-T145 | Construir en el panel web la interfaz de «Acta de reunión» | 4 | Web | Terminado |
| Sprint 2 | US32 | Acta de reunión | Sprint2-T146 | Cubrir «Acta de reunión» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US33 | Control de quórum | Sprint2-T147 | Implementar en el API la lógica y el endpoint de «Control de quórum» | 1 | Backend | Terminado |
| Sprint 2 | US33 | Control de quórum | Sprint2-T148 | Construir en el panel web la interfaz de «Control de quórum» | 2 | Web | Terminado |
| Sprint 2 | US33 | Control de quórum | Sprint2-T149 | Construir en la aplicación Android la interfaz de «Control de quórum» | 2 | Móvil | Terminado |
| Sprint 2 | US33 | Control de quórum | Sprint2-T150 | Cubrir «Control de quórum» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US34 | Acuerdos con responsable y plazo | Sprint2-T151 | Implementar en el API la lógica y el endpoint de «Acuerdos con responsable y plazo» | 2 | Backend | Terminado |
| Sprint 2 | US34 | Acuerdos con responsable y plazo | Sprint2-T152 | Construir en el panel web la interfaz de «Acuerdos con responsable y plazo» | 3 | Web | Terminado |
| Sprint 2 | US34 | Acuerdos con responsable y plazo | Sprint2-T153 | Cubrir «Acuerdos con responsable y plazo» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US58 | Advertencia de comité no paritario | Sprint2-T154 | Implementar en el API la lógica y el endpoint de «Advertencia de comité no paritario» | 1 | Backend | Terminado |
| Sprint 2 | US58 | Advertencia de comité no paritario | Sprint2-T155 | Construir en el panel web la interfaz de «Advertencia de comité no paritario» | 2 | Web | Terminado |
| Sprint 2 | US58 | Advertencia de comité no paritario | Sprint2-T156 | Cubrir «Advertencia de comité no paritario» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US59 | Seguimiento del estado de los acuerdos | Sprint2-T157 | Implementar en el API la lógica y el endpoint de «Seguimiento del estado de los acuerdos» | 1 | Backend | Terminado |
| Sprint 2 | US59 | Seguimiento del estado de los acuerdos | Sprint2-T158 | Construir en el panel web la interfaz de «Seguimiento del estado de los acuerdos» | 2 | Web | Terminado |
| Sprint 2 | US59 | Seguimiento del estado de los acuerdos | Sprint2-T159 | Cubrir «Seguimiento del estado de los acuerdos» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US60 | Consultar las actas desde el celular | Sprint2-T160 | Implementar en el API la lógica y el endpoint de «Consultar las actas desde el celular» | 2 | Backend | Terminado |
| Sprint 2 | US60 | Consultar las actas desde el celular | Sprint2-T161 | Construir en la aplicación Android la interfaz de «Consultar las actas desde el celular» | 3 | Móvil | Terminado |
| Sprint 2 | US60 | Consultar las actas desde el celular | Sprint2-T162 | Cubrir «Consultar las actas desde el celular» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US37 | Exportación de evidencia | Sprint2-T163 | Implementar en el API la lógica y el endpoint de «Exportación de evidencia» | 6 | Backend | Terminado |
| Sprint 2 | US37 | Exportación de evidencia | Sprint2-T164 | Construir en el panel web la interfaz de «Exportación de evidencia» | 7 | Web | Terminado |
| Sprint 2 | US37 | Exportación de evidencia | Sprint2-T165 | Cubrir «Exportación de evidencia» con pruebas automatizadas | 3 | QA | Terminado |
| Sprint 2 | US61 | MTTR por severidad | Sprint2-T166 | Implementar en el API la lógica y el endpoint de «MTTR por severidad» | 1 | Backend | Terminado |
| Sprint 2 | US61 | MTTR por severidad | Sprint2-T167 | Construir en el panel web la interfaz de «MTTR por severidad» | 2 | Web | Terminado |
| Sprint 2 | US61 | MTTR por severidad | Sprint2-T168 | Construir en la aplicación Android la interfaz de «MTTR por severidad» | 2 | Móvil | Terminado |
| Sprint 2 | US61 | MTTR por severidad | Sprint2-T169 | Cubrir «MTTR por severidad» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US62 | Exportar cada registro obligatorio | Sprint2-T170 | Implementar en el API la lógica y el endpoint de «Exportar cada registro obligatorio» | 2 | Backend | Terminado |
| Sprint 2 | US62 | Exportar cada registro obligatorio | Sprint2-T171 | Construir en el panel web la interfaz de «Exportar cada registro obligatorio» | 3 | Web | Terminado |
| Sprint 2 | US62 | Exportar cada registro obligatorio | Sprint2-T172 | Cubrir «Exportar cada registro obligatorio» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US63 | Resumen de hallazgos | Sprint2-T173 | Implementar en el API la lógica y el endpoint de «Resumen de hallazgos» | 1 | Backend | Terminado |
| Sprint 2 | US63 | Resumen de hallazgos | Sprint2-T174 | Construir en el panel web la interfaz de «Resumen de hallazgos» | 2 | Web | Terminado |
| Sprint 2 | US63 | Resumen de hallazgos | Sprint2-T175 | Construir en la aplicación Android la interfaz de «Resumen de hallazgos» | 2 | Móvil | Terminado |
| Sprint 2 | US63 | Resumen de hallazgos | Sprint2-T176 | Cubrir «Resumen de hallazgos» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US65 | Identidad visual consistente | Sprint2-T177 | Implementar en el API la lógica y el endpoint de «Identidad visual consistente» | 3 | Backend | Terminado |
| Sprint 2 | US65 | Identidad visual consistente | Sprint2-T178 | Construir en el panel web la interfaz de «Identidad visual consistente» | 3 | Web | Terminado |
| Sprint 2 | US65 | Identidad visual consistente | Sprint2-T179 | Construir en la aplicación Android la interfaz de «Identidad visual consistente» | 3 | Móvil | Terminado |
| Sprint 2 | US65 | Identidad visual consistente | Sprint2-T180 | Cubrir «Identidad visual consistente» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US66 | Navegación siempre accesible | Sprint2-T181 | Implementar en el API la lógica y el endpoint de «Navegación siempre accesible» | 1 | Backend | Terminado |
| Sprint 2 | US66 | Navegación siempre accesible | Sprint2-T182 | Construir en el panel web la interfaz de «Navegación siempre accesible» | 1 | Web | Terminado |
| Sprint 2 | US66 | Navegación siempre accesible | Sprint2-T183 | Construir en la aplicación Android la interfaz de «Navegación siempre accesible» | 1 | Móvil | Terminado |
| Sprint 2 | US66 | Navegación siempre accesible | Sprint2-T184 | Cubrir «Navegación siempre accesible» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US67 | Uso desde pantallas pequeñas | Sprint2-T185 | Implementar en el API la lógica y el endpoint de «Uso desde pantallas pequeñas» | 4 | Backend | Terminado |
| Sprint 2 | US67 | Uso desde pantallas pequeñas | Sprint2-T186 | Construir en el panel web la interfaz de «Uso desde pantallas pequeñas» | 4 | Web | Terminado |
| Sprint 2 | US67 | Uso desde pantallas pequeñas | Sprint2-T187 | Cubrir «Uso desde pantallas pequeñas» con pruebas automatizadas | 2 | QA | Terminado |
| Sprint 2 | US68 | Errores comprensibles | Sprint2-T188 | Implementar en el API la lógica y el endpoint de «Errores comprensibles» | 1 | Backend | Terminado |
| Sprint 2 | US68 | Errores comprensibles | Sprint2-T189 | Construir en el panel web la interfaz de «Errores comprensibles» | 2 | Web | Terminado |
| Sprint 2 | US68 | Errores comprensibles | Sprint2-T190 | Construir en la aplicación Android la interfaz de «Errores comprensibles» | 2 | Móvil | Terminado |
| Sprint 2 | US68 | Errores comprensibles | Sprint2-T191 | Cubrir «Errores comprensibles» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | US69 | Reintento ante fallo de red | Sprint2-T192 | Implementar en el API la lógica y el endpoint de «Reintento ante fallo de red» | 2 | Backend | Terminado |
| Sprint 2 | US69 | Reintento ante fallo de red | Sprint2-T193 | Construir en la aplicación Android la interfaz de «Reintento ante fallo de red» | 3 | Móvil | Terminado |
| Sprint 2 | US69 | Reintento ante fallo de red | Sprint2-T194 | Cubrir «Reintento ante fallo de red» con pruebas automatizadas | 1 | QA | Terminado |
| Sprint 2 | TS07 | Validación local del mensaje de commit | Sprint2-T195 | Configurar «Validación local del mensaje de commit» | 3 | DevOps | Terminado |
| Sprint 2 | TS07 | Validación local del mensaje de commit | Sprint2-T196 | Verificar «Validación local del mensaje de commit» en el pipeline | 1 | DevOps | Terminado |
| Sprint 2 | TS06 | Fin de línea normalizado | Sprint2-T197 | Configurar «Fin de línea normalizado» | 3 | DevOps | Terminado |
| Sprint 2 | TS06 | Fin de línea normalizado | Sprint2-T198 | Verificar «Fin de línea normalizado» en el pipeline | 1 | DevOps | Terminado |
| Sprint 2 | TS13 | Migraciones verificadas en integración | Sprint2-T199 | Configurar «Migraciones verificadas en integración» | 3 | DevOps | Terminado |
| Sprint 2 | TS13 | Migraciones verificadas en integración | Sprint2-T200 | Verificar «Migraciones verificadas en integración» en el pipeline | 1 | DevOps | Terminado |
| Sprint 2 | TS03 | Documentación viva del API | Sprint2-T201 | Configurar «Documentación viva del API» | 3 | DevOps | Terminado |
| Sprint 2 | TS03 | Documentación viva del API | Sprint2-T202 | Verificar «Documentación viva del API» en el pipeline | 1 | DevOps | Terminado |
| Sprint 2 | TS08 | Configuración por variables de entorno | Sprint2-T203 | Configurar «Configuración por variables de entorno» | 4 | DevOps | Terminado |
| Sprint 2 | TS08 | Configuración por variables de entorno | Sprint2-T204 | Verificar «Configuración por variables de entorno» en el pipeline | 2 | DevOps | Terminado |
| Sprint 2 | TS09 | Proxy de desarrollo | Sprint2-T205 | Configurar «Proxy de desarrollo» | 3 | DevOps | Terminado |
| Sprint 2 | TS09 | Proxy de desarrollo | Sprint2-T206 | Verificar «Proxy de desarrollo» en el pipeline | 1 | DevOps | Terminado |
| Sprint 2 | TS10 | Renovación transparente del token | Sprint2-T207 | Configurar «Renovación transparente del token» | 7 | DevOps | Terminado |
| Sprint 2 | TS10 | Renovación transparente del token | Sprint2-T208 | Verificar «Renovación transparente del token» en el pipeline | 3 | DevOps | Terminado |
| Sprint 2 | TS11 | Aislamiento entre empresas | Sprint2-T209 | Configurar «Aislamiento entre empresas» | 7 | DevOps | Terminado |
| Sprint 2 | TS11 | Aislamiento entre empresas | Sprint2-T210 | Verificar «Aislamiento entre empresas» en el pipeline | 3 | DevOps | Terminado |
| Sprint 2 | TS12 | Idempotencia en la creación de reportes | Sprint2-T211 | Configurar «Idempotencia en la creación de reportes» | 7 | DevOps | Terminado |
| Sprint 2 | TS12 | Idempotencia en la creación de reportes | Sprint2-T212 | Verificar «Idempotencia en la creación de reportes» en el pipeline | 3 | DevOps | Terminado |
| Sprint 2 | TS04 | Datos de demostración | Sprint2-T213 | Configurar «Datos de demostración» | 7 | DevOps | Terminado |
| Sprint 2 | TS04 | Datos de demostración | Sprint2-T214 | Verificar «Datos de demostración» en el pipeline | 3 | DevOps | Terminado |
| Sprint 2 | TS14 | APK publicado por el pipeline | Sprint2-T215 | Configurar «APK publicado por el pipeline» | 4 | DevOps | Terminado |
| Sprint 2 | TS14 | APK publicado por el pipeline | Sprint2-T216 | Verificar «APK publicado por el pipeline» en el pipeline | 2 | DevOps | Terminado |
| Sprint 2 | TS15 | Generación de evidencia en Excel | Sprint2-T217 | Configurar «Generación de evidencia en Excel» | 7 | DevOps | Terminado |
| Sprint 2 | TS15 | Generación de evidencia en Excel | Sprint2-T218 | Verificar «Generación de evidencia en Excel» en el pipeline | 3 | DevOps | Terminado |
| Sprint 2 | TS16 | Informe compilable y con índice verificado | Sprint2-T219 | Configurar «Informe compilable y con índice verificado» | 4 | DevOps | Terminado |
| Sprint 2 | TS16 | Informe compilable y con índice verificado | Sprint2-T220 | Verificar «Informe compilable y con índice verificado» en el pipeline | 2 | DevOps | Terminado |

---

#### Resumen de los dos sprints

| Sprint | Elementos | Story Points | Work-items | Horas | Objetivo |
|---|---|---|---|---|---|
| Sprint 1 | 15 | 60 | 54 | 120 | Cerrar el ciclo del hallazgo de extremo a extremo. |
| Sprint 2 | 71 | 259 | 220 | 518 | Completar los registros del SGSST sobre ese ciclo. |
| **Total** | **86** | **319** | **274** | **638** | |

**Velocidad.** Los dos sprints completaron la totalidad de lo comprometido; no hubo arrastre de uno
al siguiente. Conviene señalar, sin embargo, que los sprints son marcadamente desiguales: el
Sprint 2 cuadruplica en Story Points al Sprint 1. Eso no es una buena práctica de planificación
—un sprint debe caber en una capacidad estable— y refleja que el alcance se agrupó por afinidad
funcional antes que por capacidad del equipo. Se documenta como lo que es: una decisión de
organización del trabajo, no una velocidad sostenible sobre la cual planificar.

**Sobre el periodo de ejecución.** Conviene decirlo con precisión, porque el historial de los
repositorios es público y cualquiera puede contrastarlo: los sprints **organizan el alcance, no
ventanas de calendario**. El trabajo se ejecutó en sesiones intensivas de desarrollo entre el 12 y
el 16 de septiembre de 2026, que es lo que muestran las fechas de los commits en `sst-api`,
`sst-web`, `sst-mobile` y `sst-report`. Por eso las tablas no declaran fechas de inicio y fin:
declararlas repartidas en semanas sería contradecir un dato verificable en un clic. Por la misma
razón las horas estimadas son una conversión declarada de los Story Points y no un registro de
tiempo real.

> **Limitación reconocida.** Un ciclo de desarrollo comprimido impide observar lo que la práctica
> iterativa busca: retroalimentación del usuario entre iteraciones que reoriente el alcance de la
> siguiente. Los dos sprints se ejecutaron sobre un plan fijado de antemano. Se documenta como
> limitación del trabajo, no como práctica recomendable.

### 5.2.2. Implemented Landing Page Evidence

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

Resguardo se ofrece como servicio en la nube: la empresa cliente no instala ni administra
servidores. Eso traslada al proveedor obligaciones que conviene fijar por escrito, sobre todo
tratándose de información que la empresa debe poder exhibir ante una fiscalización de SUNAFIL y
que incluye datos personales de sus trabajadores.

El acuerdo siguiente es el **nivel de servicio propuesto** para el producto. No está en vigor
—el sistema todavía no opera en producción con clientes reales— y se documenta aquí como parte
del diseño del servicio, no como un contrato suscrito.

**1. Alcance del servicio**

| Componente | Qué cubre |
|---|---|
| API y base de datos | Disponibilidad, respaldo y conservación de todos los registros del SGSST |
| Panel web | Acceso desde navegador para supervisor, comité y administrador |
| Aplicación Android | Distribución de la aplicación y compatibilidad con las dos últimas versiones mayores de Android |
| Evidencia documental | Generación de las exportaciones de los registros obligatorios |

**2. Disponibilidad**

| Parámetro | Compromiso |
|---|---|
| Disponibilidad mensual del API y del panel web | 99,5 % |
| Equivalente en indisponibilidad | Hasta 3 h 39 min por mes |
| Medición | Sobre el total de minutos del mes calendario, excluyendo la ventana de mantenimiento programada |
| Ventana de mantenimiento | Domingos de 02:00 a 05:00 (hora de Perú), avisada con 72 horas de anticipación |

La aplicación móvil queda fuera de este cómputo por diseño: opera sin conexión y sincroniza
cuando hay red, de modo que una caída del servicio no impide que el trabajador registre un
hallazgo. Ese es precisamente el motivo de la arquitectura sin conexión.

**3. Atención de incidencias**

| Severidad | Definición | Primera respuesta | Objetivo de solución |
|---|---|---|---|
| **Crítica** | El servicio no está disponible o no se pueden registrar hallazgos | 1 hora | 4 horas |
| **Alta** | Una funcionalidad de un registro obligatorio no opera y no hay forma de sortearla | 4 horas | 1 día hábil |
| **Media** | Funcionalidad degradada con alternativa disponible | 1 día hábil | 5 días hábiles |
| **Baja** | Consulta, mejora o defecto cosmético | 2 días hábiles | Según planificación |

Horario de atención: lunes a viernes de 08:00 a 18:00 (hora de Perú) para severidades media y
baja; veinticuatro horas para severidad crítica.

**4. Respaldo, retención y continuidad**

| Parámetro | Compromiso |
|---|---|
| Frecuencia de respaldo | Diaria, con copia cifrada fuera del servidor principal |
| Retención de respaldos | 30 días de copias diarias y 12 copias mensuales |
| RPO (pérdida máxima de datos) | 24 horas |
| RTO (tiempo máximo de restablecimiento) | 8 horas |
| Prueba de restauración | Trimestral, en entorno separado, con constancia del resultado |
| Conservación de registros del SGSST | Mientras dure el contrato y por el plazo que exige la normativa peruana de conservación de registros de seguridad y salud en el trabajo |

**5. Tratamiento de datos personales**

El sistema almacena DNI, teléfono, fotografías tomadas en campo y coordenadas de geolocalización
de trabajadores. Todo ello es dato personal bajo la **Ley N° 29733, Ley de Protección de Datos
Personales**, y su tratamiento se sujeta a las siguientes condiciones:

| Condición | Compromiso |
|---|---|
| Titularidad | Los datos son de la empresa cliente; el proveedor actúa como encargado del tratamiento, nunca como titular |
| Finalidad | Exclusivamente la gestión del sistema de seguridad y salud en el trabajo; no se usan para ningún otro fin ni se ceden a terceros |
| Aislamiento | Cada empresa accede únicamente a sus propios datos, restricción aplicada en el backend y no en la interfaz |
| Geolocalización | Es opcional y revocable por el trabajador; negarla no impide reportar |
| Subencargados | Se informa a la empresa cliente qué proveedores de infraestructura intervienen y dónde se alojan los datos |
| Incidentes de seguridad | Notificación a la empresa cliente dentro de las 48 horas de detectado un acceso no autorizado a datos personales |

**6. Terminación y devolución de la información**

| Situación | Compromiso |
|---|---|
| Terminación por cualquier causa | La empresa dispone de 60 días para descargar la totalidad de su información |
| Formato de devolución | Formatos abiertos y legibles sin el sistema: hojas de cálculo para los registros y archivos originales para las fotografías |
| Eliminación posterior | Cumplido el plazo, los datos se eliminan de los sistemas activos y de los respaldos en el siguiente ciclo de rotación |
| Sin retención como palanca comercial | La devolución no se condiciona al pago de conceptos distintos de los ya vencidos por el servicio prestado |

**7. Exclusiones**

No quedan cubiertos por los compromisos de disponibilidad: las interrupciones causadas por fallas
de la conexión a internet de la empresa cliente, los eventos de fuerza mayor, las suspensiones por
falta de pago previamente notificadas, y el uso del servicio fuera de las condiciones acordadas.

**8. Reporte de cumplimiento**

El proveedor publica mensualmente la disponibilidad alcanzada y el detalle de las incidencias de
severidad crítica y alta del periodo, con su tiempo de respuesta y de solución. Sin esa
publicación, el compromiso del punto 2 no sería verificable por el cliente y, por tanto, no sería
un compromiso.

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

## 5.3. Video About-the-Product

