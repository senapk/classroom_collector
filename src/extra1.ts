// Strings Extra 1

// Nesta atividade, você tem duas variáveis: frase e trecho, que contêm duas strings. Realize as tarefas abaixo:

// 1. Descubra o comprimento da frase e armazene em uma variável chamada comprimentoTrecho.
// 2. Encontre a posição (índice) onde o trecho aparece na frase e armazene em uma variável chamada indice.
// 3. Usando as variáveis e métodos de string disponíveis, recorte a frase original para ficar apenas com "Eu não gosto de spoilers." e armazene em uma variável chamada fraseRevisada.

// Dica: Use os métodos length, indexOf e slice.

// TODO: Implemente abaixo:

const frase = 'Eu não gosto de spoilers e memes sem graça.';
const trecho = 'e memes sem graça.';

let comprimentoTrecho: number;
let indice: number;
let fraseRevisada: string;

// Seu código aqui 👇

fraseRevisada = `"`;

console.log(`Comprimento do trecho: ${comprimentoTrecho}`); //18
console.log(`Índice do trecho: ${indice}`); // 25
console.log(`Frase revisada: ${fraseRevisada}`); // "Eu não gosto de spoilers."

// Comando para rodar este arquivo: npx tsx src/extra1.ts
// Comando para verificar o TypeScript: npx eslint src/extra1.ts
// Comando para testar todos os arquivos: npm test
