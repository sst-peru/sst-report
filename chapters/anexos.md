# Anexos

## Anexo A. Videos de Exposiciones

| Entrega | Enlace del video | Duración |
|---|---|---|
| Trabajo Final (TF) | <!-- COMPLETAR --> | <!-- COMPLETAR --> |

## Anexo B. Enlaces del proyecto

| Recurso | Enlace |
|---|---|
| Organización GitHub | https://github.com/sst-peru |
| Repositorio del informe | https://github.com/sst-peru/sst-report |
| API (backend) | https://github.com/sst-peru/sst-api |
| Aplicación web | https://github.com/sst-peru/sst-web |
| Aplicación móvil Android | https://github.com/sst-peru/sst-mobile |
| Landing page desplegada | <!-- COMPLETAR --> |
| Aplicación web desplegada | <!-- COMPLETAR --> |
| Documentación del API (Swagger) | <!-- COMPLETAR: URL pública + `/api/docs/` --> |

## Anexo C. Credenciales de demostración

Usuarios generados por el comando `python manage.py seed_demo` del repositorio `sst-api`. Todos
comparten la contraseña `demo12345`.

| Usuario | Rol | Qué permite demostrar |
|---|---|---|
| `supervisor` | Supervisor de SST | Acceso completo: tablero, gestión de hallazgos, IPERC, inspecciones, EPP, comité, usuarios y exportaciones |
| `comite1`, `comite2` | Miembro del comité | Mismas capacidades que el supervisor |
| `operario1` … `operario6` | Operario | Menú reducido, visibilidad limitada a sus propios reportes, y las dos variantes del formulario del experimento |

> **Advertencia.** Los datos que genera `seed_demo` son simulados, incluida la diferencia entre
> variantes del experimento. Sirven para demostrar el funcionamiento del sistema y **no
> constituyen evidencia experimental**.

## Anexo D. Cálculo del tamaño de muestra

El cálculo de la sección 8.2.5 es reproducible ejecutando, en el repositorio del informe:

```bash
python tools/tamano-muestra.py
```

El script documenta los parámetros del diseño, el modelo estadístico empleado y sus supuestos, y
calcula tanto el tamaño de muestra requerido para distintos niveles de potencia como el efecto
mínimo detectable para muestras menores.

## Anexo E. Estructura del repositorio del informe

| Ruta | Contenido |
|---|---|
| `README.md` | Carátula, registro de versiones, índice y Student Outcome |
| `chapters/` | Un archivo por capítulo |
| `assets/img/` | Imágenes: capturas, diagramas exportados, fotografías |
| `assets/diagrams/` | Fuentes editables de los diagramas |
| `tools/build.py` | Genera el índice y compila `informe-completo.md` |
| `tools/tamano-muestra.py` | Cálculo del tamaño de muestra del experimento |
| `CONTRIBUTING.md` | GitFlow y Conventional Commits aplicados al informe |

