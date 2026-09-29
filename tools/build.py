#!/usr/bin/env python3
"""Actualiza el índice del informe único en README.md.

    python tools/build.py toc   -> regenera la tabla de contenidos
    python tools/build.py       -> actualiza el índice y resume las marcas pendientes

Para la entrega, exportar README.md directamente a PDF.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


INICIO = "<!-- TOC:inicio -->"
FIN = "<!-- TOC:fin -->"


def ancla(titulo: str) -> str:
    """Reproduce el identificador que GitHub genera para un encabezado."""
    texto = titulo.strip().lower()
    texto = texto.replace(" ", "-")
    # GitHub conserva letras (incluidas acentuadas), números, guiones y guiones bajos.
    permitidos = []
    for caracter in texto:
        if caracter in "-_" or caracter.isalnum():
            permitidos.append(caracter)
    return "".join(permitidos)


def encabezados(ruta: Path):
    """Devuelve (nivel, título) de cada encabezado, ignorando los bloques de código."""
    en_codigo = False
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        coincidencia = re.match(r"^(#{1,4})\s+(.*)$", linea)
        if coincidencia:
            yield len(coincidencia.group(1)), coincidencia.group(2).strip()


def construir_toc() -> str:
    lineas = []
    usados = set()
    en_informe = False
    for nivel, titulo in encabezados(RAIZ / "README.md"):
        base = ancla(titulo)
        identificador = base
        sufijo = 0
        while identificador in usados:
            sufijo += 1
            identificador = f"{base}-{sufijo}"
        usados.add(identificador)
        if nivel == 1 and titulo == "Capítulo I: Introducción":
            en_informe = True
        if en_informe:
            sangria = "  " * (nivel - 1)
            limpio = re.sub(r"[*`]", "", titulo)
            lineas.append(f"{sangria}- [{limpio}](#{identificador})")
    return "\n".join(lineas)


def escribir_toc() -> None:
    readme = RAIZ / "README.md"
    texto = readme.read_text(encoding="utf-8")
    if INICIO not in texto or FIN not in texto:
        sys.exit("No encuentro las marcas del índice en el README.")
    antes = texto.split(INICIO)[0]
    despues = texto.split(FIN)[1]
    readme.write_text(
        f"{antes}{INICIO}\n\n{construir_toc()}\n\n{FIN}{despues}",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Índice actualizado: {len(construir_toc().splitlines())} entradas.")


def resumir() -> None:
    contenido = (RAIZ / "README.md").read_text(encoding="utf-8")
    pendientes = contenido.count("**PENDIENTE.**")
    completar = contenido.count("COMPLETAR")
    print(f"README.md: {len(contenido.splitlines())} líneas.")
    print(f"  secciones pendientes: {pendientes}")
    print(f"  marcas COMPLETAR:     {completar}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "toc":
        escribir_toc()
    else:
        escribir_toc()
        resumir()
