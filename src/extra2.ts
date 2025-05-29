// Strings Extra 2

// Nesta atividade, você tem o nome de um teorema, dois valores numéricos e uma string incompleta (os trechos a serem preenchidos estão marcados com asteriscos (*)).
// Realize as tarefas abaixo:
// 1. Transforme a string de aspas simples em um template literal (crase).
// 2. Substitua os quatro asteriscos por placeholders de template literal:
//    - O nome do teorema.
//    - Os dois valores numéricos fornecidos.
//    - O comprimento da hipotenusa de um triângulo retângulo, sabendo que os outros dois lados têm os valores fornecidos.

// TODO: Implemente abaixo:

const teorema = 'Teorema de Pitágoras';
const ladoA = 9;
const ladoB = 12;
const hipotenusa = Math.sqrt(ladoA ** 2 + ladoB ** 2); // ladoA^2 + ladoB^2 = hipotenusa^2

const resultado =
    '(*): Se um triângulo tem lados de (*) e (*), então a hipotenusa mede (*).';

// Saída esperada:
// Teorema de Pitágoras: Se um triângulo tem lados de 9 e 12, então a hipotenusa mede 15.

console.log(resultado);

// Comando para rodar este arquivo: npx tsx src/extra2.ts
// Comando para verificar o TypeScript: npx eslint src/extra2.ts
// Comando para testar todos os arquivos: npm test
