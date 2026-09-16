#!/usr/bin/env bash
# Activa los hooks de git del repositorio. Correr una vez después de clonar.
set -e
git config core.hooksPath .githooks
chmod +x .githooks/* 2>/dev/null || true
echo "✓ Hooks activados: los mensajes de commit se validan contra Conventional Commits."
