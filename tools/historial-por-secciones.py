#!/usr/bin/env python3
"""Reconstruye el historial del informe con un commit por cada sección.

    python tools/historial-por-secciones.py                 # simulación, no toca nada
    python tools/historial-por-secciones.py --ejecutar      # crea los commits
    python tools/historial-por-secciones.py --ejecutar --push

Toma el contenido actual de README.md como versión final y reconstruye sus capítulos
sección por sección, confirmando cada una con su propio commit en
formato Conventional Commits. El resultado es el mismo contenido con un historial
detallado, sección por sección.

Advertencia: todos los commits llevarán la fecha y hora en que se ejecute el script.
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

INFORME = RAIZ / "README.md"

ALCANCES = {
    "Capítulo I: Introducción": "cap01",
    "Capítulo II: Requirements Elicitation & Analysis": "cap02",
    "Capítulo III: Requirements Specification": "cap03",
    "Capítulo IV: Product Design": "cap04",
    "Capítulo V: Product Implementation": "cap05",
    "Capítulo VI: Product Verification & Validation": "cap06",
    "Capítulo VII: DevOps Practices": "cap07",
    "Capítulo VIII: Experiment-Driven Development": "cap08",
    "Conclusiones": "cierre",
    "Bibliografía": "biblio",
    "Anexos": "anexos",
}
CAPITULOS = list(ALCANCES)


def git(*args, capturar=False):
    resultado = subprocess.run(
        ["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8"
    )
    if resultado.returncode != 0:
        raise SystemExit(
            f"git {' '.join(args)} falló:\n{resultado.stdout}\n{resultado.stderr}"
        )
    return resultado.stdout.strip() if capturar else None


def sin_tildes(texto: str) -> str:
    """El convenio de commits del repositorio pide mensajes sin tildes ni eñes."""
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn").replace("ñ", "n")


def mensaje(alcance: str, titulo: str) -> str:
    """Construye el mensaje de commit a partir del título de la sección."""
    limpio = re.sub(r"^[\d.]+\s*", "", titulo)          # quita la numeración
    limpio = re.sub(r"[*`_]", "", limpio).strip(" .")    # quita marcas de markdown
    limpio = sin_tildes(limpio).lower()
    limpio = re.sub(r"\s+", " ", limpio)
    texto = f"docs({alcance}): agregar {limpio}"
    return texto[:100]


def trocear(contenido: str, nivel_maximo: int):
    """Parte el capítulo en bloques: el encabezado del capítulo y luego cada sección.

    Devuelve una lista de (titulo, texto_del_bloque). Las líneas dentro de bloques de
    código se ignoran para no confundir un comentario '## ' de un ejemplo con un título.
    """
    lineas = contenido.splitlines(keepends=True)
    bloques = []
    titulo_actual = None
    actual = []
    en_codigo = False

    for linea in lineas:
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            actual.append(linea)
            continue

        encabezado = None if en_codigo else re.match(r"^(#{2,4})\s+(.*)$", linea)
        if encabezado and len(encabezado.group(1)) <= nivel_maximo:
            if actual:
                bloques.append((titulo_actual, "".join(actual)))
            titulo_actual = encabezado.group(2).strip()
            actual = [linea]
        else:
            actual.append(linea)

    if actual:
        bloques.append((titulo_actual, "".join(actual)))
    return bloques


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ejecutar", action="store_true", help="crea los commits de verdad")
    parser.add_argument("--push", action="store_true", help="empuja la rama al final")
    parser.add_argument("--rama", default="docs/informe-por-secciones")
    parser.add_argument(
        "--nivel",
        type=int,
        default=3,
        choices=(2, 3, 4),
        help="profundidad de corte: 2 agrupa por sección mayor, 3 es el detalle recomendado",
    )
    args = parser.parse_args()

    # 1. El contenido actual de los capítulos es la versión final.
    contenido = INFORME.read_text(encoding="utf-8")
    posiciones = [contenido.index(f"\n# {titulo}\n") + 1 for titulo in CAPITULOS]
    cabecera = contenido[:posiciones[0]]
    limites = posiciones[1:] + [len(contenido)]
    finales = {
        titulo: contenido[inicio:fin]
        for titulo, inicio, fin in zip(CAPITULOS, posiciones, limites)
    }

    plan = []
    for nombre in CAPITULOS:
        alcance = ALCANCES[nombre]
        bloques = trocear(finales[nombre], args.nivel)
        for i, (titulo, texto) in enumerate(bloques):
            etiqueta = titulo if titulo else f"estructura de {nombre}"
            plan.append((nombre, alcance, etiqueta, texto, i == 0))

    print(f"Capítulos: {len(CAPITULOS)}")
    print(f"Commits que se crearán: {len(plan) + 2} (incluye el de reinicio y el del índice)\n")

    if not args.ejecutar:
        print("SIMULACIÓN — no se modificó nada. Primeros y últimos mensajes:\n")
        for nombre, alcance, etiqueta, _, _ in plan[:5]:
            print(f"  {mensaje(alcance, etiqueta)}")
        print("  ...")
        for nombre, alcance, etiqueta, _, _ in plan[-3:]:
            print(f"  {mensaje(alcance, etiqueta)}")
        print("\nPara crearlos de verdad:  python tools/historial-por-secciones.py --ejecutar")
        return

    # 2. Rama de trabajo.
    rama_actual = git("rev-parse", "--abbrev-ref", "HEAD", capturar=True)
    if rama_actual != args.rama:
        git("checkout", "-B", args.rama)
    print(f"Rama: {args.rama}\n")

    # 3. Vaciar los capítulos y confirmarlo como un paso explícito del historial.
    INFORME.write_text(cabecera, encoding="utf-8", newline="")
    git("add", "README.md")
    creados = 0
    if git("status", "--porcelain", capturar=True):
        git("commit", "-m", "chore(informe): reiniciar capitulos para reconstruir el historial")
        creados = 1
        print("  [  1] chore(informe): reiniciar capitulos para reconstruir el historial")

    acumulado = cabecera

    for nombre, alcance, etiqueta, texto, es_primero in plan:
        acumulado += texto
        INFORME.write_text(acumulado, encoding="utf-8", newline="")
        git("add", "README.md")

        if es_primero:
            texto_commit = f"docs({alcance}): crear el capitulo y su encabezado"
        else:
            texto_commit = mensaje(alcance, etiqueta)

        if not git("status", "--porcelain", capturar=True):
            print(f"  [ -- ] sin cambios, se omite: {texto_commit}")
            continue

        git("commit", "-m", texto_commit)
        creados += 1
        print(f"  [{creados:>3}] {texto_commit}")

    # 4. Índice regenerado como último commit.
    subprocess.run([sys.executable, str(RAIZ / "tools" / "build.py"), "toc"], cwd=RAIZ, check=False)
    git("add", "README.md")
    estado = git("status", "--porcelain", capturar=True)
    if estado:
        git("commit", "-m", "docs(indice): regenerar la tabla de contenidos del informe")
        creados += 1
        print(f"  [{creados:>3}] docs(indice): regenerar la tabla de contenidos del informe")

    print(f"\n{creados} commits creados en {args.rama}.")

    if args.push:
        git("push", "-u", "origin", args.rama)
        print(f"Rama {args.rama} enviada a origin.")
    else:
        print(f"Para subirla:  git push -u origin {args.rama}")


if __name__ == "__main__":
    main()
