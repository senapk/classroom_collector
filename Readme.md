# Avaliação

```bash
# ==================================================================
# ===================  CODESPACE SETUP  ============================
# ==================================================================
# tko
sudo apt-get update && pipx install tko
# se for utilizar go
go install golang.org/x/tools/gopls@latest
# se for utilizar typescript
npm install typescript typescript-language-server esbuild readline-sync ts-node
# ==================================================================
# =====================  LOCAL SETUP  ==============================
# ==================================================================
# Se estiver no seu computador e já tiver o setup para fazer o clone
# local com as ferramentas de desenvolvimento e compiladores, lembre
# de atualizar o tko antes de começar a avaliação. 
pipx upgrade tko
# ==================================================================
# ==================  FAZENDO A AVALIAÇÃO  =========================
# ==================================================================
# abra o tko na raiz do repositório que você acabou de clonar
tko open .

# Baixe as atividades e rode os testes.
# Se quiser marcar a autoavalição para acompanhar a sua nota
# marque que fez sozinho, mas isso não é obrigatório ou muda a nota.

# ==================================================================
# =================  ENVIANDO A AVALIAÇÃO  =========================
# ==================================================================
git add .
git commit -m "Avaliação"
git push
```

## Acompanhamento

### Exercícios

- [ ] `@data       *1 :leet`[Formatando data](https://github.com/qxcodefup/arcade/blob/master/base/data/Readme.md)
- [ ] `@bonzinho   *2 :leet`[Professor](https://github.com/qxcodefup/arcade/blob/master/base/bonzinho/Readme.md)
- [ ] `@lotado     *2 :leet`[Ônibus dos alunos](https://github.com/qxcodefup/arcade/blob/master/base/lotado/Readme.md)
- [ ] `@casais     *3 :leet`[Quantos casais na arca](https://github.com/qxcodefup/arcade/blob/master/base/casais/Readme.md)
- [ ] `@parkour    *3 :leet`[Analisando vetores](https://github.com/qxcodefup/arcade/blob/master/base/parkour/Readme.md)
