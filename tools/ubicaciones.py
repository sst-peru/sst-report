"""Donde encontrar cada historia implementada en el panel web y en la app Android.

Las rutas salen de la navegacion real de los dos clientes: la barra lateral y las rutas
de sst-web, y la barra inferior mas la pantalla "Mas" de sst-mobile.
"""

# id: (ubicacion en el panel web, ubicacion en la app Android)
# Cadena vacia = la historia no tiene interfaz en esa plataforma.
UBICACIONES = {
    # --- Acceso y cuentas ---
    "US01": ("Registro (`/registro`)", "Pantalla de acceso → «Crear cuenta»"),
    "US02": ("Pantalla de acceso (`/login`)", "Pantalla de acceso al abrir la aplicación"),
    "US03": ("Transversal: la sesión se restaura al volver a abrir", "Transversal: la sesión se restaura al volver a abrir"),
    "US04": ("Usuarios y áreas (`/usuarios`)", ""),
    "US05": ("Usuarios y áreas (`/usuarios`) → pestaña Áreas", ""),
    "US41": ("Usuarios y áreas (`/usuarios`) → columna Rol", ""),
    "US42": ("Pie de la barra lateral → «Cerrar sesión»", "«Más» → «Cerrar sesión»"),
    "US43": ("Barra lateral: las opciones cambian según el rol", "Barra inferior y pantalla «Más»: cambian según el rol"),

    # --- Reporte de actos y condiciones inseguras ---
    "US06": ("Reportar (`/reportes/nuevo`)", "Pestaña «Reportar»"),
    "US07": ("", "Pestaña «Reportar» sin señal; la cola se ve en «Más» → «Reportes guardados en el celular»"),
    "US08": ("Reportar: un reintento no duplica el hallazgo", "La cola se envía sola al recuperar la señal, sin duplicar"),
    "US09": ("Reportar → paso 2, «Evidencia»", "Pestaña «Reportar» → paso 2, «Evidencia»"),
    "US10": ("Reportar → paso 2, «Ubicación»", "Pestaña «Reportar» → paso 2, «Ubicación»"),
    "US11": ("Reportar → paso 3, «Fecha de ocurrencia»", "Pestaña «Reportar» → paso 3, «Fecha de ocurrencia»"),
    "US12": ("Reportar (`/reportes/nuevo`)", ""),
    "US13": ("Reportes (`/reportes`)", "Pestaña «Mis reportes»"),
    "US44": ("Reportar → paso 2: miniatura de la foto elegida", ""),
    "US45": ("Reportar → paso 2 y detalle del hallazgo: tocar la foto la amplía", ""),
    "US46": ("Reportar → paso 2 → «Quitar»", ""),
    "US47": ("Reportar → paso 1, «Tipo de hallazgo»", "Pestaña «Reportar» → paso 1, «Tipo de hallazgo»"),
    "US48": ("", "«Más» → «Reportes guardados en el celular»: estado Enviado o Pendiente"),

    # --- Gestion del hallazgo ---
    "US14": ("Reportes (`/reportes`)", "Pestaña «Reportes»"),
    "US15": ("Reportes → detalle del hallazgo → «Asignar»", "Pestaña «Reportes» → detalle → «Asignar»"),
    "US16": ("Reportes → detalle del hallazgo → «Cerrar»", "Pestaña «Reportes» → detalle → «Cerrar»"),
    "US17": ("Reportes → detalle: las acciones solo aparecen para supervisor y comité", "Pestaña «Reportes» → detalle: las acciones dependen del rol"),
    "US18": ("Reportes → detalle → sección «Bitácora»", "Pestaña «Reportes» → detalle → «Bitácora»"),
    "US49": ("Reportes → detalle → «Descartar»", ""),
    "US50": ("Reportes → filtros de estado, tipo y área", "Pestaña «Reportes» → filtros"),
    "US51": ("Reportes → detalle → enlace de ubicación", ""),

    # --- Matriz IPERC ---
    "US19": ("Matriz IPERC (`/iperc`)", "«Más» → «Matriz IPERC»"),
    "US20": ("Matriz IPERC → «Agregar peligro»", ""),
    "US21": ("Matriz IPERC → selector de versión", ""),
    "US22": ("Matriz IPERC → columna «Hallazgo de origen»", "«Más» → «Matriz IPERC»"),
    "US52": ("Matriz IPERC → selector de versión → versiones históricas", ""),
    "US53": ("Matriz IPERC → «Nueva versión»", ""),
    "US54": ("Matriz IPERC → «Retirar» en la fila del peligro", ""),

    # --- Control de EPP ---
    "US23": ("Equipos de protección (`/epp`) → pestaña Catálogo", ""),
    "US24": ("Equipos de protección → «Registrar entrega»", ""),
    "US25": ("Equipos de protección → columna «Conformidad»", "Pestaña «Mis EPP» → «Dar conformidad»"),
    "US26": ("Equipos de protección → aviso de vencimiento en la entrega", "Pestaña «Mis EPP» → aviso de vencimiento"),
    "US55": ("Equipos de protección → pestaña Catálogo, columna Stock", ""),

    # --- Inspecciones periodicas ---
    "US27": ("Inspecciones (`/inspecciones`) → «Nuevo programa»", ""),
    "US28": ("Inspecciones → «Realizar» con checklist", "Pestaña «Inspecciones» → «Realizar» con checklist"),
    "US29": ("Inspecciones → listado, marca de vencida", "Pestaña «Inspecciones» → marca de vencida"),
    "US56": ("Inspecciones → «Generar siguiente»", ""),
    "US57": ("Inspecciones → indicadores por área", ""),

    # --- Comite de SST ---
    "US30": ("Comité de SST (`/comite`) → «Constituir comité»", ""),
    "US31": ("Comité de SST → pestaña Miembros", ""),
    "US32": ("Comité de SST → pestaña Actas → «Nueva acta»", ""),
    "US33": ("Comité de SST → Actas: verificación de quórum", "«Más» → «Comité de SST» → Actas"),
    "US34": ("Comité de SST → Actas → «Agregar acuerdo»", ""),
    "US58": ("Comité de SST → Miembros: aviso de comité no paritario", ""),
    "US59": ("Comité de SST → Acuerdos: estado y plazo", ""),
    "US60": ("", "«Más» → «Comité de SST» → Actas"),

    # --- Metricas y evidencia ---
    "US35": ("Tablero (`/`) → indicador MTTR", "Pestaña «Tablero» → indicador MTTR"),
    "US36": ("Tablero → cumplimiento de inspecciones", "Pestaña «Tablero» → cumplimiento de inspecciones"),
    "US37": ("Botón «Exportar» en reportes, IPERC, EPP, inspecciones y comité", ""),
    "US61": ("Tablero → MTTR desglosado por severidad", "Pestaña «Tablero» → MTTR por severidad"),
    "US62": ("Botón «Exportar» en cada módulo del panel", ""),
    "US63": ("Tablero → resumen de hallazgos por estado", "Pestaña «Tablero» → resumen de hallazgos"),

    # --- Experimento A/B ---
    "US38": ("Reportar: la variante se asigna al abrir el formulario", "Pestaña «Reportar»: la variante se asigna al abrir el formulario"),
    "US39": ("Reportes → detalle: la variante aparece en el subtítulo del hallazgo", "Pestaña «Reportes» → detalle → «Variante»"),
    "US40": ("Experimento A/B (`/experimento`)", ""),
    "US64": ("", "Pestaña «Reportar»: la variante se conserva sin conexión"),

    # --- Calidad de uso y operacion ---
    "US65": ("Transversal: misma identidad visual en todo el panel", "Transversal: misma identidad visual en toda la aplicación"),
    "US66": ("Barra lateral fija, visible en todas las pantallas", "Barra inferior fija, visible en todas las pantallas"),
    "US67": ("Transversal: el panel se adapta a pantallas pequeñas", ""),
    "US68": ("Transversal: mensajes de error con la acción a seguir", "Transversal: mensajes de error con la acción a seguir"),
    "US69": ("", "Pestaña «Reportar»: reintento automático al fallar la red"),
    "US70": ("Transversal: la sesión se renueva sin pedir la contraseña", "Transversal: la sesión se renueva sin pedir la contraseña"),

    # --- Registro de accidentes, incidentes y enfermedades ocupacionales ---
    "US71": ("Accidentes e incidentes (`/accidentes`) → «Registrar accidente» → tipo «Accidente de trabajo»", ""),
    "US72": ("Accidentes e incidentes → «Registrar accidente» → tipo «Incidente peligroso»", ""),
    "US74": ("Accidentes e incidentes → seleccionar el accidente → «Registrar investigación»", ""),
    "US75": ("Accidentes e incidentes → expediente del accidente → «Agregar medida»", ""),
    "US76": ("Accidentes e incidentes → aviso «Avisos al Ministerio de Trabajo pendientes», y en el expediente → «Registrar aviso»", ""),
    "US77": ("Accidentes e incidentes → «Índices de accidentabilidad · últimos 90 días»", ""),
    "US78": ("Accidentes e incidentes → «Enfermedades ocupacionales» → «Registrar enfermedad»", ""),

    # --- Privacidad y datos personales ---
    "US111": ("Pantalla de política de privacidad al iniciar sesión; después en Privacidad (`/privacidad`) → «Tu consentimiento»", ""),
    "US112": ("Privacidad (`/privacidad`) → «Ubicación de los hallazgos»", ""),
    "US116": ("Reportar (`/reportes/nuevo`) → casilla «Reportar de forma anónima»", ""),

    # --- Experimento A/B: lectura de los resultados ---
    "US125": ("Experimento A/B (`/experimento`) → aviso de datos de demostración sobre los resultados", ""),
    "US126": ("Experimento A/B (`/experimento`) → bloque «Diferencia en reportes por usuario»", ""),
}


# Historias tecnicas: no viven en una pantalla, asi que se describe donde se comprueban.
NOTAS_TECNICAS = {
    "TS01": "Sin interfaz: workflows de GitHub Actions en `.github/workflows/` de cada repositorio; se comprueban en la pestaña Actions de cada Pull Request",
    "TS02": "Sin interfaz: hook `commit-msg` en `.githooks/` y workflow «Conventional Commits», que rechazan el mensaje que no cumple el formato",
    "TS05": "Sin interfaz: ramas `main` y `develop` en los cuatro repositorios, con una rama de feature por historia",
    "TS09": "Sin interfaz: `server.proxy` de `/api` en `vite.config.ts` del panel web",
    "TS10": "Transversal en los dos clientes: la sesión se renueva sin volver a pedir la contraseña",
    "TS12": "Sin interfaz: `POST /api/v1/reports/` es idempotente por `client_uuid`; un reintento responde 200 con la cabecera `X-Idempotent-Replay`",
    "TS31": "Sin interfaz: al editar un reporte, `base_updated_at` desactualizado devuelve 409 con la versión del servidor",
}


def ubicacion(identificador):
    """Devuelve la celda de la columna «Dónde encontrarlo» para una historia.

    Un guion significa que la historia todavia no se puede verificar sobre el producto en
    ejecucion, sea porque no tiene interfaz propia o porque falta construirla en ese
    cliente. Nunca se escribe una ruta de algo que no existe: la columna sirve para
    comprobar el producto, y una ruta falsa la vuelve inutil.
    """
    if identificador in NOTAS_TECNICAS:
        return NOTAS_TECNICAS[identificador]
    web, android = UBICACIONES.get(identificador, ("", ""))
    partes = []
    if web:
        partes.append("**Web:** %s" % web)
    if android:
        partes.append("**Android:** %s" % android)
    return "<br>".join(partes) if partes else "—"
