# Capítulo IV: Product Design

## 4.1. Style Guidelines

### 4.1.1. General Style Guidelines

**Marca.** El producto se llama **Resguardo**. El nombre se eligió porque reúne los dos sentidos
que definen al sistema: proteger y dejar constancia. Se escribe en versalitas en la barra lateral
y acompañado siempre del descriptor "Sistema de Gestión de Seguridad y Salud en el Trabajo".

**Principio rector.** La interfaz es institucional, no comercial. El usuario que la abre está
gestionando riesgos laborales y respondiendo ante una autoridad fiscalizadora; el producto debe
transmitir formalidad y precisión, no entusiasmo. De ahí tres reglas que atraviesan todo el
diseño:

1. **El color solo aparece cuando significa algo.** El azul es la institución; el gris, la
   estructura. Verde, ámbar y rojo se reservan para estados: cerrado, en proceso, vencido o
   crítico. No hay color decorativo.
2. **Sin gradientes, sin sombras de color y con esquinas de 4 píxeles.** Es lo que separa
   visualmente una herramienta corporativa de una aplicación de consumo.
3. **La densidad es una función, no un defecto.** El supervisor revisa decenas de hallazgos por
   sesión; las tablas son compactas a propósito.

**Paleta cromática**

| Token | Valor | Uso |
|---|---|---|
| `--navy-900` | `#0c1d33` | Títulos y textos de mayor jerarquía |
| `--navy-800` | `#12304f` | Barra lateral, fondo de la pantalla de acceso |
| `--navy-700` | `#1b4570` | Acciones primarias, filetes superiores de tarjetas |
| `--navy-600` | `#24578a` | Estados hover, enlaces |
| `--blue-500` | `#2f6db0` | Indicador de la opción de menú activa |
| `--blue-100` | `#e7eff7` | Realce de fila de tabla, halo de foco |
| `--blue-050` | `#f2f6fa` | Filas alternadas de tabla |
| `--gray-900` | `#1c2530` | Texto base |
| `--gray-500` | `#5e6a78` | Texto secundario |
| `--gray-200` | `#dce1e7` | Bordes |
| `--gray-100` | `#eaeef2` | Cabeceras de tabla, separadores |
| `--gray-050` | `#f4f6f8` | Fondo de trabajo |
| `--ok-700` | `#1f6b47` | Estado cerrado / conforme |
| `--warn-700` | `#8a6100` | Estado en proceso |
| `--danger-700` | `#a02a2a` | Vencido, crítico, acciones destructivas |

**Tipografía**

| Rol | Familia | Justificación |
|---|---|---|
| Títulos y cifras de indicadores | Serif del sistema (`ui-serif`, Georgia, Palatino) | Aporta el peso de documento formal, sin cargar una fuente externa que retrase la carga en conexiones lentas |
| Texto de interfaz | Sans del sistema (Segoe UI, system-ui) | Legibilidad en pantalla y cero descarga adicional |
| Etiquetas y cabeceras de tabla | Sans en versalitas, 11 px, `letter-spacing` 0.06em | Jerarquía sin recurrir al color |

**Espaciado e iconografía.** Radio de esquina uniforme de 4 px; bordes de 1 px; separación base
de 8 px con múltiplos de 4. No se usan emojis ni iconos decorativos en la web; en la aplicación
móvil los iconos provienen de Material Icons, limitados a la navegación inferior.

**Tono de voz.** Español peruano formal pero directo. Se prefiere el vocabulario del dominio
("hallazgo", "acción correctiva", "quórum") sobre el vocabulario genérico de software
("ítem", "elemento"). Los mensajes de error explican qué hacer, no solo qué falló.

<!-- IMAGEN REQUERIDA: captura de la paleta y la tipografía aplicadas, o tabla de color
     exportada desde Figma, en assets/img/style-guide-paleta.png -->

