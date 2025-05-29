# Variáveis

<!-- toc -->

- [Trabalhando com texto — strings em JavaScript](#trabalhando-com-texto--strings-em-javascript)
    - [O poder das palavras](#o-poder-das-palavras)
    - [Strings — O básico](#strings--o-básico)
    - [Concatenando strings](#concatenando-strings)
    - [Conclusão](#conclusão)
- [Métodos úteis de string](#métodos-úteis-de-string)
    - [Strings como objetos](#strings-como-objetos)
    - [Encontrando o comprimento de uma string](#encontrando-o-comprimento-de-uma-string)
    - [Recuperando um caractere específico de uma string](#recuperando-um-caractere-específico-de-uma-string)
    - [Testando se uma string contém uma substring](#testando-se-uma-string-contém-uma-substring)
    - [Encontrando a posição de uma substring em uma string](#encontrando-a-posi%C3%A7%C3%A3o-de-uma-substring-em-uma-string)
    - [Extraindo uma substring de uma string](#extraindo-uma-substring-de-uma-string)
    - [Alterando a capitalização](#alterando-a-capitaliza%C3%A7%C3%A3o)
    - [Atualizando partes de uma string](#atualizando-partes-de-uma-string)
    - [Exemplos para aprendizado ativo](#exemplos-para-aprendizado-ativo)
    - [Conclusão](#conclusão-1)
- [Referências](#referências)

<!-- toc -->

# Strings — O básico

Strings são sequências de caracteres usadas para representar texto, que podem ser criadas utilizando aspas simples, duplas ou crases (para templates literais).

```typescript
let single = 'Aspas simples';
let double = 'Aspas duplas';
let backtick = `Template literal`;
```

Strings podem conter qualquer caractere Unicode e suportam caracteres especiais como `\n` para nova linha.

Se você tem aspas no seu texto, pode usar a barra invertida `\` para escapar as aspas ou usar o outro formato para delimitar a string:

```typescript
var naruto =
    '"Trabalho duro" é inútil para aqueles que não acreditam em si mesmos.';
var aspasNoTexto1 = "Essas são aspas únicas: '";
var aspasNoTexto2 = "Essas são aspas únicas: '";
```

## Concatenando strings

Concatenar strings significa uni-las. Isso pode ser feito com o operador `+` ou utilizando templates literais.

```typescript
let greeting = 'Olá, ';
let name = 'Mundo';
let message = greeting + name; // "Olá, Mundo"

let templateMessage = `${greeting}${name}`; // "Olá, Mundo"
```

Templates literais permitem interpolar variáveis diretamente dentro da string, tornando o código mais legível.

# Métodos úteis de string

Agora que vimos o básico sobre strings, vamos explorar operações úteis que podemos realizar com métodos integrados, como encontrar o comprimento de uma string de texto, juntar e dividir strings, substituir um caractere por outro e muito mais.

## Encontrando o comprimento de uma string

Use a propriedade `length` para obter o número de caracteres em uma string:

```typescript
const tipoNavegador = 'mozilla';
tipoNavegador.length; // Retorna 7
```

## Recuperando um caractere específico de uma string

Você pode acessar qualquer caractere dentro de uma string usando a notação de colchetes `[]`:

```typescript
const tipoNavegador = 'mozilla';
tipoNavegador[0]; // Retorna 'm'
```

Para obter o último caractere de qualquer string:

```typescript
tipoNavegador[tipoNavegador.length - 1];
```

## Testando se uma string contém uma substring

Para verificar se uma substring está presente dentro de uma string maior, use o método `includes()`:

```typescript
const tipoNavegador = 'mozilla';

if (tipoNavegador.includes('zilla')) {
    console.log('Encontrado zilla!');
} else {
    console.log('Zilla não encontrado!');
}
```

Para verificar se uma string começa ou termina com uma substring específica, use `startsWith()` e `endsWith()`:

```typescript
tipoNavegador.startsWith('moz'); // Retorna true
tipoNavegador.endsWith('zilla'); // Retorna true
```

## Encontrando a posição de uma substring em uma string

Use o método `indexOf()` para encontrar a posição de uma substring dentro de uma string maior:

```typescript
const slogan = 'Recursos para desenvolvedores';
console.log(slogan.indexOf('desenvolvedores')); // Retorna 14
```

Se a substring não for encontrada, `indexOf()` retorna `-1`.

Para encontrar ocorrências subsequentes de uma substring:

```typescript
const slogan = 'Recursos para desenvolvedores, por desenvolvedores';
const primeiraOcorrencia = slogan.indexOf('desenvolvedores');
const segundaOcorrencia = slogan.indexOf(
    'desenvolvedores',
    primeiraOcorrencia + 1
);

console.log(primeiraOcorrencia); // 14
console.log(segundaOcorrencia); // 35
```

## Extraindo uma substring de uma string

Você pode extrair partes de uma string usando os métodos `slice()`, `substring()` ou `substr()`:

```typescript
const nomeCompleto = 'Maria Silva';

// Usando slice
const primeiroNome = nomeCompleto.slice(0, 5); // "Maria"

// Usando substring
const sobrenome = nomeCompleto.substring(6); // "Silva"
```

## Alterando a capitalização

Para converter uma string para letras maiúsculas ou minúsculas, use `toUpperCase()` e `toLowerCase()`:

```typescript
const saudacao = 'Olá Mundo';

saudacao.toUpperCase(); // "OLÁ MUNDO"
saudacao.toLowerCase(); // "olá mundo"
```

## Atualizando partes de uma string

Para substituir partes de uma string, use o método `replace()`:

```typescript
const frase = 'Eu gosto de maçãs';

const novaFrase = frase.replace('maçãs', 'pizza');
console.log(novaFrase); // "Eu gosto de pizza" 😏 
```

Para substituir todas as ocorrências, use uma expressão regular com a flag `g`:

```typescript
const texto = 'maçã, maçã, maçã';
const novoTexto = texto.replace(/maçã/g, 'pizza');
console.log(novoTexto); // "pizza, pizza, pizza"
```

Expressões regulares são úteis para trabalhar com strings. Se quiser entender mais sobre expressões regulares, veja [este guia na MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Regular_expressions).


## Referências

[qxcodefup/arcade](https://github.com/qxcodefup/arcade)

[Trabalhando com texto — strings em JavaScript](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Scripting/Strings)

[Métodos úteis de string](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Scripting/Useful_string_methods)
