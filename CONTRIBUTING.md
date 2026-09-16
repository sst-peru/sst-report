# Cómo se trabaja este informe

El enunciado del curso exige que el informe evolucione en un repositorio de control de
versiones aplicando **GitFlow** y **Conventional Commits**, y que los commits evidencien los
aportes. Este documento fija esas reglas.

## Ramas

```
main                  ← solo versiones entregadas, una por entrega, con su tag
└── develop           ← informe en curso
    ├── docs/capitulo-01-introduccion
    ├── docs/capitulo-08-experimento
    └── fix/indice-desactualizado
```

| Prefijo | Para qué |
|---|---|
| `docs/` | Redactar o ampliar una sección del informe |
| `fix/` | Corregir errores, enlaces rotos, tablas mal formadas |
| `chore/` | Estructura del repositorio, scripts, plantillas |
| `release/` | Preparar una entrega: versión, índice, PDF |

Nunca se commitea directo a `main` ni a `develop`.

## Flujo de una sección

```bash
git checkout develop
git pull origin develop
git checkout -b docs/capitulo-02-competidores

# ... se redacta la sección ...
python tools/build.py toc          # el índice se regenera solo
git add chapters/capitulo-02-requirements-elicitation.md README.md
git commit -m "docs(cap02): agregar analisis competitivo con tres competidores"

git push -u origin docs/capitulo-02-competidores
# Pull Request hacia develop
```

## Conventional Commits

Formato: `tipo(alcance): descripción`

```
docs(cap01): redactar antecedentes y problematica con 5w2h
docs(cap04): agregar diagrama de contenedores c4
docs(cap08): documentar el calculo de tamano de muestra
fix(indice): corregir enlaces rotos del capitulo 6
chore(build): agregar script de compilacion del informe
```

Reglas:

- tipo en minúscula, de la lista: `docs` `fix` `chore` `style` `refactor` `feat` `revert`
- el alcance identifica el capítulo (`cap01` … `cap08`) o el área (`indice`, `build`, `assets`)
- descripción en minúscula y en modo imperativo, máximo 100 caracteres
- sin tildes ni eñes en el mensaje de commit, para evitar problemas de codificación en Windows

El hook `commit-msg` valida el formato localmente y el workflow de GitHub Actions lo valida en
cada Pull Request. **Actívalo después de clonar:**

```bash
bash scripts/setup-hooks.sh
```

## Entregas

Cada entrega se integra a `main` y se etiqueta:

```bash
git checkout main && git pull
git merge --no-ff develop -m "chore(release): informe trabajo final"
git tag -a tf -m "Trabajo Final"
git push origin main --tags
```

Antes de exportar el PDF:

```bash
python tools/build.py             # regenera índice y arma informe-completo.md
```

El script informa cuántas secciones siguen marcadas como **PENDIENTE** y cuántas marcas
`COMPLETAR` quedan. Ninguna de las dos debería aparecer en el documento que se entrega.
