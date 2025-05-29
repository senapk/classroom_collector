# 🌟 Ambiente produtivo para desenvolvimento TypeScript | Node.js

Este conteúdo foca no ambiente de desenvolvimento — terminal e configurações do VS Code — para projetos em TypeScript, fundamentado nos seguintes pilares:

-   Ambiente estruturado
-   Terminal bem configurado
-   Visual Studio Code com extensões

Este repositório já está pronto para criar um ambiente ideal utilizando:

-   **GitHub Codespaces** como ambiente de desenvolvimento
-   **VS Code** como editor
-   **Dev Container** para configurar um contêiner Docker no Codespaces
-   **Docker** para conteinerização

Você não precisa conhecer todas essas ferramentas de antemão; confira as descrições abaixo quando quiser se aprofundar. Vamos começar pelo básico para você já poder codar.

## 🖥️ Onde fica o código?

Grande parte dos arquivos neste repositório é de configuração:  
`.gitignore`, a pasta `.devcontainer/` (com `Dockerfile` e `devcontainer.json`), `eslint.config.js` etc. Eles determinam seu ambiente e geralmente não precisam ser alterados.

O código do projeto fica na pasta `src` e o arquivo principal é o `src/main.ts`.

Para executar o projeto, rode:

```bash
npm run build
```

Ou execute diretamente com o tsx:

```bash
npx tsx src/main.ts
```

O script npm run build (definido em `package.json`) compila o TypeScript sem emitir arquivos JavaScript. Se quiser ver o .js gerado, use:

```bash
npx tsc src/main.ts
```

# 📋 Conceitos

## JavaScript

JavaScript (JS) é uma linguagem de programação versátil e popular, amplamente utilizada para adicionar interatividade a páginas web e, mais recentemente, para o desenvolvimento de aplicações do lado do servidor (back-end). É uma linguagem de alto nível, interpretada e baseada em objetos, com funções de primeira classe.

Algumas referências importantes sobre JavaScript:

-   [MDN Web Docs - JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
-   [W3Schools - JavaScript](https://www.w3schools.com/js/)
-   [Importação de Módulos](https://www.alura.com.br/artigos/guia-importacao-exportacao-modulos-javascript)

## TypeScript

TypeScript é um superset de JavaScript com tipagem estática opcional, que amplia o editor com detecção de erros e autocompletar mais precisos.

Algumas referências importantes sobre TypeScript:

-   [Documentação oficial do TypeScript](https://www.typescriptlang.org/docs/)
-   [MDN Web Docs - TypeScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Using_type_annotations)
-   [Alura - O que é TypeScript?](https://www.alura.com.br/artigos/o-que-e-typescript)
-   [Playground do TypeScript](https://www.typescriptlang.org/play)
-   [Diferenças entre JavaScript e TypeScript](https://www.alura.com.br/artigos/diferencas-entre-javascript-e-typescript)

## ⚙️ Node.js

O **Node.js** é um ambiente de execução de JavaScript multiplataforma, de código-aberto e gratuita, baseado no motor V8 do Chrome. Ele permite executar código JavaScript no servidor, fora do navegador.

Criado com foco em desempenho e escalabilidade, o Node.js é especialmente útil para aplicações web em tempo real, APIs RESTful e serviços que exigem alta taxa de I/O (entrada e saída), como chats e sistemas de streaming.

### 🚀 Principais características

-   **Event-driven** e **non-blocking**: usa um modelo assíncrono baseado em eventos, o que o torna altamente eficiente.
-   **Leve e rápido**: ideal para aplicações escaláveis.
-   **NPM**: possui o maior ecossistema de bibliotecas open source do mundo.
-   **Cross-platform**: funciona em Windows, Linux e macOS.

### ▶️ Principais comandos

**Executar um arquivo JavaScript**

```bash
node arquivo.js
```

Executa um script Node.js diretamente no terminal.

**Inicializar um projeto Node**

```bash
npm init
npm init -y   # pula perguntas e cria um package.json com padrão
```

Cria o package.json, que organiza as dependências e scripts do projeto.

## 📦 NPM (Node Package Manager)

O **NPM** é o gerenciador de pacotes oficial do Node.js. Ele permite instalar bibliotecas, frameworks e ferramentas de forma simples, além de gerenciar scripts e dependências de um projeto JavaScript ou TypeScript.

### 🧰 Comandos essenciais

```bash
npm init -y                   # Cria um package.json com configurações padrão
npm install <pacote>          # Instala um pacote como dependência
npm install --save-dev <pacote>  # Instala como dependência de desenvolvimento
npm run <script>              # Executa um script definido no package.json
npm outdated                  # Verifica pacotes desatualizados
npm update                    # Atualiza pacotes
```

### 📁 Estrutura após instalação

-   package.json: define as dependências e scripts do projeto.
-   package-lock.json: registra a árvore de dependências exata.
-   node_modules/: pasta onde os pacotes instalados ficam armazenados. Essa pasta não precisa ser versionada ou estar no repositório online. Além de possuir um tamanho enorme, com o package.json é possível reconstruí-la em qualquer máquina.

### 💡 Dica

Use scripts personalizados no package.json para tarefas recorrentes, como:

```json
"scripts": {
  "dev": "node index.js",
  "lint": "eslint .",
  "format": "prettier --write ."
}
```

### ⚡ npx: executar sem instalar

O comando npx permite executar um pacote diretamente do repositório NPM, sem precisar instalá-lo globalmente. Exemplo: `npx eslint . `.

## 🐳 Docker

Docker é uma plataforma que permite empacotar, distribuir e executar aplicações em ambientes isolados chamados de _containers_. Um container é uma unidade leve, portátil e consistente, que inclui tudo o que a aplicação precisa para funcionar — bibliotecas, dependências, código e configuração — garantindo que ela funcione da mesma forma em qualquer ambiente, seja na máquina local, em um servidor ou na nuvem.

Diferente da virtualização de máquinas, em que os recursos eram mais rígidos e há uma dependência do sistema operacional, a solução do Docker é leve e fácil de implantar. Os arquivos de imagens de container são semelhantes aos pacotes de instalação de software. No entanto, eles só precisam de um runtime de container e um kernel compatível para executar a aplicação, não importando o sistema operacional usado para criar o container nem a origem das bibliotecas dentro dele.

## Dev Container

Dev Containers são ambientes de desenvolvimento prontos e reprodutíveis configurados com base em arquivos como `.devcontainer/devcontainer.json`. Eles são usados em conjunto com o VS Code (ou GitHub Codespaces) para garantir que todos os desenvolvedores de um projeto usem a mesma versão de configurações, ferramentas, extensões e dependências.

**Benefícios:**

-   Reduz problemas de "na minha máquina funciona".
-   Permite configuração padronizada do ambiente com Node, TypeScript, linters, etc.
-   Integração nativa com o VS Code e GitHub CodeSpaces.

As features aplicadas neste repositório no DevContainer são:

-   Common Utilities: usado para instalar o terminal Zsh
-   Zsh Plugins: para instalar plugins do OhMyZsh, como o zsh-autosuggestions
-   GitHub CLI: para lidar com fluxos do GitHub

Se realizar alguma atualização no arquivo `devcontainer.json`, pressione "Ctrl+Shift+P" para exibir a "Paleta de Comandos" e comece a digitar "codespaces: rebuild container" para ver o resultado das alterações.

## JSON

JSON (**JavaScript** Object Notation) é um formato leve de troca de dados, fácil de ler e escrever. É usado extensivamente para configurar ambientes (como no `devcontainer.json`), transferir dados entre front-end e back-end, e configurar serviços em nuvem.

#### 🧩 Elementos básicos do JSON

JSON (JavaScript Object Notation) é composto por **pares chave-valor** e pode conter diferentes tipos de dados. Seus dois principais blocos estruturais são **objetos** e **arrays**, além dos valores literais.

**🔹 Objeto (`Object`)**

Um **objeto** é uma estrutura de dados composta por pares `chave: valor`, delimitados por `{}`. Cada chave deve ser uma **string** entre aspas duplas, e os valores podem ser de qualquer tipo JSON válido. Veja o exemplo abaixo:

```json
{
    "nome": "Lana",
    "idade": 30,
    "ativo": true
}
```

**🔹 Array (Array)**

Um array é uma lista ordenada de valores, delimitada por [ ]. Os elementos podem ser de tipos diferentes, inclusive outros objetos ou arrays. Veja o exemplo abaixo:

```json
["JavaScript", "TypeScript", "Python"]
```

Um exemplo com uma lista de objetos:

```json
[
    { "nome": "João", "idade": 25 },
    { "nome": "Maria", "idade": 28 }
]
```

## 💻 Zsh (Z Shell)

Zsh é um interpretador de comandos (shell) para sistemas Unix/Linux, compatível com o Bash, mas com **funcionalidades mais avançadas**, como:

-   **Autocompletar inteligente** com sugestões e correções automáticas.
-   **Suporte a plugins e temas** via frameworks como [Oh My Zsh](https://ohmyz.sh/).
-   **Histórico compartilhado entre abas/terminais**.
-   **Prompt personalizável** com informações de Git, status de comando anterior, entre outros.

Zsh é especialmente útil para desenvolvedores, pois acelera a produtividade no terminal com recursos como:

```bash
# Autocompleta comandos e nomes de arquivos
cd D<tab>   # completa para 'Documents' ou diretório equivalente

# Sugestão de comandos do histórico
git status     # ao digitar `git`, ele sugere o uso anterior
```

## ✨ [oh my zsh](https://ohmyz.sh/)

Oh My Zsh é uma estrutura open source para personalizar o shell Zsh, amplamente usada em Linux e macOS. Zsh é um shell projetado para uso interativo, semelhante ao Bash, usado em sistemas Unix/Linux e macOS.

Com WSL, pode ser instalado no Ubuntu do Windows Terminal. Oferece temas, plugins e atalhos para melhorar a produtividade e a aparência do terminal. Fácil de instalar, é popular entre desenvolvedores por sua flexibilidade e vasta comunidade. Suas funcionalidades são:

-   Autocompletar e correção de comandos
-   Temas e cores
-   Gerência avançada do histórico de comandos
-   Variedade enorme de plugins, comunidade ativa.

### 🔌 Plugins e complementos:

Coleção de complementos adicionais ao ohmyzsh: O [zsh-completions](https://github.com/zsh-users/zsh-completions) é uma coleção de complementos adicionais para o Zsh (Z Shell), projetada para melhorar a experiência de autocompletar comandos e opções no terminal.

[Fast Syntax Highlighting](https://github.com/zdharma/fast-syntax-highlighting) é um plugin para o shell Zsh que fornece realce de sintaxe (syntax highlighting) em tempo real para comandos digitados no terminal. Ele ajuda os usuários a identificar erros, comandos válidos e argumentos enquanto escrevem.

## 📝 Spell-checker

O _spell-checker_ é um verificador ortográfico que ajuda a identificar erros de escrita em códigos e comentários. No VS Code, use o plugin **Code Spell Checker**, disponível na extensão `streetsidesoftware.code-spell-checker`, com suporte a múltiplos idiomas como inglês e português (pt-BR). É necessário instalar tanto o plugin quanto o dicionário da língua.

## 🐙 GitHub CLI (gh)

Use o GitHub CLI para interagir com repositórios remotos:

```bash
gh auth login                   # Faz login na sua conta do GitHub
gh repo create                  # Cria um novo repositório no GitHub
gh repo clone usuario/repositorio # Clona um repositório
gh pr create                    # Cria um pull request
gh issue list                   # Lista issues do repositório

```

## 🎨 Prettier

O Prettier é um formatador de código automático. Ele garante consistência no estilo de escrita, padronizando indentação, aspas, ponto e vírgula e outros detalhes.

## 🧪 ESLint

O ESLint é uma ferramenta de linting para JavaScript e TypeScript. Ele analisa o código em busca de erros, problemas de estilo e padrões de codificação. O ESLint pode ser configurado com regras personalizadas ou usar configurações padrão.
