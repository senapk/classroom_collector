#!/bin/bash

if [ -z "$1" ]; then
    echo "Uso: $0 usuario/repositorio"
    exit 1
fi

REPO="$1"
OUTDIR="resultado-${REPO//\//-}" # transforma usuario/repositorio em usuario-repositorio

echo "📦 Processando $REPO..."

# Pega o ID da última execução
run_id=$(gh run list --repo "$REPO" --limit 1 --json databaseId --jq '.[0].databaseId' 2>/dev/null)

if [ -z "$run_id" ]; then
    echo "⚠️  Nenhuma execução encontrada para $REPO"
    exit 1
fi

# outfile is REPO with .txt in the end
repo_clean="${REPO#https://github.com/}"
outfile="${repo_clean//\//-}.txt"

gh run view "$run_id" --repo "$REPO" --log > "$outfile" 2>/dev/null

# filter $outfile keeping only lines with text "Run setup script" and remove the first 3 cols using \t separator, depois cortar mais 10 caracteres
grep "Run setup script" "$outfile" | cut -f 3- | cut -c 11- > "$OUTDIR/$outfile"
