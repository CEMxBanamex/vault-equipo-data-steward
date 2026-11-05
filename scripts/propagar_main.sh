#!/usr/bin/env bash
# Propaga main a la rama de cada integrante listada en .github/integrantes.txt.
# Si una fusión tiene conflicto, la cancela, abre un issue asignado a esa persona
# y sigue con las demás ramas. Requiere GH_TOKEN para crear issues.
set -uo pipefail

git fetch origin --prune
conflictos=0

while read -r rama usuario; do
  [[ -z "${rama:-}" || "$rama" == \#* ]] && continue

  if ! git ls-remote --exit-code --heads origin "$rama" > /dev/null; then
    echo "::notice::La rama '$rama' no existe en el remoto; se omite."
    continue
  fi

  git checkout -q -B "$rama" "origin/$rama"
  if git merge --no-edit origin/main > /dev/null 2>&1; then
    git push -q origin "$rama"
    echo "OK: main propagado a '$rama'."
  else
    archivos=$(git diff --name-only --diff-filter=U | sed 's/^/- /')
    git merge --abort
    conflictos=$((conflictos + 1))
    echo "::warning::Conflicto al propagar main a '$rama'."

    titulo="Conflicto al propagar main a la rama $rama"
    abiertos=$(gh issue list --state open --search "\"$titulo\" in:title" --json number --jq 'length')
    if [[ "$abiertos" == "0" ]]; then
      cuerpo=$(printf 'El Action no pudo llevar los cambios de `main` a la rama `%s` porque hay conflictos en:\n\n%s\n\n**Cómo resolverlo:** en tu rama, haz `git pull origin main`, resuelve los conflictos, haz commit y push. Cierra este issue cuando termines.' "$rama" "$archivos")
      gh issue create --title "$titulo" --body "$cuerpo" --assignee "$usuario" \
        || gh issue create --title "$titulo" --body "$cuerpo"
    fi
  fi
done < .github/integrantes.txt

git checkout -q main
if (( conflictos > 0 )); then
  echo "Ramas con conflicto: $conflictos. Revisa los issues abiertos."
  exit 1
fi
echo "Todas las ramas están al día con main."
