#!/usr/bin/env python3
import sys
import subprocess
import re
import argparse
import os
import csv
from openpyxl import Workbook

def remover_ansi(texto: str):
    # Remove códigos ANSI de cores
    ansi_escape = re.compile(r'\x1B\[[0-9;]*[mK]')
    return ansi_escape.sub('', texto)

def down_single(repo: str, output: str | None = None):
    print(f"📦 Processando {repo}...")

    # Obtém o ID da última execução
    try:
        result = subprocess.run(
            ["gh", "run", "list", "--repo", repo, "--limit", "1", "--json", "databaseId", "--jq", ".[0].databaseId"],
            capture_output=True,
            text=True,
            check=True
        )
        run_id = result.stdout.strip()
    except subprocess.CalledProcessError:
        print(f"⚠️  Erro ao tentar obter execução para {repo}")
        sys.exit(1)

    if not run_id:
        print(f"⚠️  Nenhuma execução encontrada para {repo}")
        sys.exit(1)

    # Define o nome do arquivo de saída
    if output:
        outfile = output
    else:
        outfile = repo.replace('/', '-') + ".txt"

    try:
        # Pega o log da execução
        log_result = subprocess.run(
            ["gh", "run", "view", run_id, "--repo", repo, "--log"],
            capture_output=True,
            text=True,
            check=True
        )
        log = log_result.stdout
    except subprocess.CalledProcessError:
        print(f"⚠️  Não foi possível obter o log de execução para {repo}")
        sys.exit(1)

    # Remove cores ANSI
    log = remover_ansi(log)

    # Filtra linhas contendo [TKO
    linhas_filtradas = [
        linha[64:]  # remove os primeiros 44 caracteres
        for linha in log.splitlines()
        if "[TKO" in linha
    ]

    # Salva no arquivo de saída
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas_filtradas))

    print(f"✅ Log salvo em {outfile}")

def down_task(org: str, task: str):
    cmd_list = ["gh", "repo", "list", org, "--limit", "1000", "--json", "name,url", "--jq", r'.[] | "\(.name) \(.url)"']
    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True, check=True)
        name_repos = result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        print(f"⚠️  Erro ao tentar listar repositórios para a tarefa {task} na organização {org}")
        sys.exit(1)

    os.makedirs(task, exist_ok=True)
    students: dict[str, dict[str, str]] = {}

    for name_repo in name_repos:
        parts = name_repo.split()
        name = parts[0]
        url = parts[1]
        cut_begin = len(task) + 1
        if name.startswith(task):
            single_name = name[cut_begin:]
            output_file = os.path.join(task, single_name + ".txt")
            # down_single(url, output_file)
            grading = load_info(output_file)
            students[single_name] = grading
            # print(f"📊 {single_name}:", end="")
            # print(", ".join(f"{label}" for label, value in grading.items()))

    return students

def load_info(file: str) -> dict[str, str]:
    grading: dict[str, str] = {}
    lines: list[str] = []
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        tko_running = "[TKO RUNNING] @"
        if line.startswith(tko_running):
            line = line[len(tko_running):]
            parts = line.split(" ")
            label = parts[0]
            parts = line.split("] ")
            extra = parts[-1]
            grading[label] = extra.strip().replace(", ", " ")
        tko_grading = "[TKO GRADING] "
        if line.startswith(tko_grading) and line[-1] == "%":
            line = line[len(tko_grading):]
            parts = line.split(" ")
            label = parts[0]
            if not label in grading:
                grading[label] = "0%"
    grading["Total"] = lines[-1].split(" ")[-1].strip()
    return grading

def format_sheet(sheet: list[list[str]]) -> list[list[str]]:
    nl = len(sheet)
    nc = len(sheet[0])

    for c in range(nc):
        for l in range(nl):
            sheet[l][c] = sheet[l][c].strip()

    for c in range(nc):
        max_len = 0
        for l in range(nl):
            max_len = max(max_len, len(sheet[l][c]))
        for l in range(nl):
            if c == 0:
                sheet[l][c] = sheet[l][c].ljust(max_len)
            else:
                sheet[l][c] = sheet[l][c].rjust(max_len)
    return sheet

def main():
    parser = argparse.ArgumentParser(description="Baixa logs de execução do GitHub Actions")
    parser.add_argument("--repo", type=str, nargs="*", help="Links dos repositórios a serem baixados")
    parser.add_argument("--task", type=str, nargs=2, required=False, metavar=("ORG", "TASK"), help="Baixar todos os logs dessa tarefa da organização")
    args = parser.parse_args()

    if not args.repo and not args.task:
        print("⚠️  Nenhum repositório ou tarefa fornecido. Use --repo <repo1> <repo2> ... ou --task <org> <task>")
        sys.exit(1)
    if args.repo:
        for repo in args.repo:
            down_single(repo)
    if args.task:
        org = args.task[0]
        task = args.task[1]
        students = down_task(org, task)
        labels: list[str] = list(next(iter(students.values())).keys())
        # print(labels)
        sheet: list[list[str]] = []

        header = ["Student"] + labels
        sheet.append(header)
        for student, grading in students.items():
            row = [student]
            row.extend(grading[label] for label in labels)
            sheet.append(row)

        sheet = format_sheet(sheet)

        with open(f"{task}.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for line in sheet:
                writer.writerow(line)

if __name__ == "__main__":
    main()
