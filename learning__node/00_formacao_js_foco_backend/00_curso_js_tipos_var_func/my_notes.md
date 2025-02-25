# <span style="color: #87BBA2">JavaScript: utilizando tipos, variáveis e funções</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [01. JS, Node.js e o backend](#01-js-nodejs-e-o-backend)
  - [JAVASCRIPT E O BACKEND](#javascript-e-o-backend)
    - [Diferença](#diferença)
  - [NODE.JS](#nodejs)
  - [ARQUITETURA BASEADA EM EVENTOS E LOOP DE EVENTOS](#arquitetura-baseada-em-eventos-e-loop-de-eventos)
- [02. Variáveis](#02-variáveis)
  - [VARIAVEIS NO JS](#variaveis-no-js)
  - [CASE SENSITIVE](#case-sensitive)
    - [Convenções de nomes](#convenções-de-nomes)
  - [ESCOPO DE VARIAVEL](#escopo-de-variavel)
    - [Bloco, função e global](#bloco-função-e-global)
      - [Escopo de bloco](#escopo-de-bloco)
      - [Escopo de função](#escopo-de-função)
      - [Escopo global](#escopo-global)
    - [Var, let e const](#var-let-e-const)
      - [var](#var)
      - [let](#let)
      - [const](#const)
      - [Exemplos](#exemplos)
    - [Proteção com const](#proteção-com-const)
  - [TRANSPILANDO (BABEL)](#transpilando-babel)
  - [LIDANDO COM ERROS](#lidando-com-erros)
- [03. Tipo de dados](#03-tipo-de-dados)
  - [NUMBER](#number)
    - [Convertendo para número e trabalhando com ele](#convertendo-para-número-e-trabalhando-com-ele)
  - [STRING](#string)
  - [BOOLEAN](#boolean)
    - [Sobre o uso do operador de igualdade estrita (===)](#sobre-o-uso-do-operador-de-igualdade-estrita-)
  - [NULL E UNDEFINED](#null-e-undefined)
    - [Valor indefinido != Não existe valor](#valor-indefinido--não-existe-valor)
    - [Usando typeof](#usando-typeof)
    - [undefined](#undefined)
- [04. Operadores](#04-operadores)
  - [OPERADORES ARITMÉTICOS](#operadores-aritméticos)
  - [OPERADORES LÓGICOS](#operadores-lógicos)
  - [TRUTHY E FALSY](#truthy-e-falsy)
    - [Negação](#negação)
  - [OPERADORES DE COMPARAÇÃO](#operadores-de-comparação)
- [04. Funções](#04-funções)
  - [FUNÇÕES](#funções)
    - [Declaração de função](#declaração-de-função)
    - [Expressão de função](#expressão-de-função)
    - [Arrow function](#arrow-function)
      - [Multiplas instruções](#multiplas-instruções)
      - [Instrução única](#instrução-única)

# <span style="color: #87BBA2">01. JS, Node.js e o backend</span>

## JAVASCRIPT E O BACKEND
- FrontEnd: Tudo que é renderizado no navegador
- BackEnd: Server side, lado do servidor, cuida da regra de negócio, ou seja, o que acontece com as informações que saem da tela, como as compras são processadas, como são guardadas no banco de dados. O processamento não é feito no navegador.
- Para o Javascript, para isso ocorrer fora do navegador, precisamos utilizar um framework chamado Node, que possibilita o uso do Javascript fora do navegador

### Diferença
No front, tem necessidade de cliques de botão, por exemplo. Já no back não precisa, mas tem outras peculiaridades que um front não tem.

## NODE.JS
- Navegador: Interpretador original do JS
  - Cada navegador, tem um motor (engine) que interpreta o JS
- O Node.js é meio que mais um destes motores
  - "Meio que" pois ele utiliza da engine do Chrome por baixo dos panos
  - Mas, aplicado de uma forma especifica para back-end
  - Em outras palavras, Node é um ambiente de interpratação Javascript fora do navegador

## ARQUITETURA BASEADA EM EVENTOS E LOOP DE EVENTOS
https://www.alura.com.br/artigos/arquitetura-node-js-entenda-loop-de-eventos (Terminar de ler)

# <span style="color: #87BBA2">02. Variáveis</span>

## VARIAVEIS NO JS
Entendendo a diferença da declaração e importancia de declarar com let e const uma variável:
- Ao declarar como `let`, deixamos essa variável disponível para ser alterada ao longo do script. Isso pode gerar comportamentos indesejados, como outros que interagirão com o código poderem reatribuí-lo.
- Para isso e por via de regra, recomenda-se utilizar o `const`, para encerrar a atribuição no momento da sua declaração, assim, a variável torna-se mais segura
  - `const`, ao contário de `let`, demanda que seja inicializado com um valor onde este tornar-se-á constante (inalterável). Já `let` deixa inicializar vazio e em seguida reatribui-la.

O `let` e `const` vieram posteriormente a criação da linguagem, onde antes atribuia-se com `var`. Atualmente, o `var` se tornou obsoleto por conta da sua flexibilidade tão grande que pode tornar-se prejudicial.

Por via de regra, recomenda-se utilizar `const` e, caso a reatribuição dessa variável for necessária, utiliza-se `let`, porém, na incerteza, utilize `const`.

## CASE SENSITIVE

Para os comandos e nomes de variável, ou seja, basicamente em tudo, JS é **Case Sensitive**

```js
const minhaVar = 1;
const MinhaVar = "texto";
const minhavar = "3";
const MINHAVAR = 2;

console.log(minhaVar, MinhaVar, minhavar, MINHAVAR)
```

### Convenções de nomes
- camelCase: inicia com letra minúscula e a primeira letra de cada palavra em seguida é escrita com letra maiúscula. Por exemplo: minhaVar ou senhaDoUsuario. **Esta é a convenção utilizada pelo JavaScript para variáveis e funções.**
- snake_case: os espaços são substituídos pelo caractere _ (underline), com todas as palavras em letra minúscula. Por exemplo: minha_variavel ou senha_do_usuario. É o padrão utilizado, por exemplo, pela linguagem Python.
- kebab-case: similar ao anterior, porém com os espaços substituídos por hífens. Por exemplo: minha-var ou senha-do-usuario. **Esta convenção não pode ser utilizada no JavaScript para variáveis e funções**, pois o sinal - representa um operador de subtração. Porém, pode ser utilizada para nomear arquivos, como por exemplo exercicios-variaveis.js.
- PascalCase: similar ao camelCase, porém neste caso todas as palavras começam com letra maiúscula. Por exemplo: MinhaVar ou SenhaDoCliente.
> Importante: nunca utilize espaço nem caracteres especiais e também não inicie os nomes das variáveis com números.

## ESCOPO DE VARIAVEL
Limite/espaço que nós trabalhamos

### Bloco, função e global

#### Escopo de bloco
- Bloco: Que está dentro de as chaves de algo, seja de uma estrutura de controle (if), seja em uma função ou afins e pode ser chamado apenas dentro deste bloco
  - Variáveis declaradas dentro de chaves { }, como no caso de if, for, while etc., não ficam acessíveis para código que esteja de fora. Chamamos o código dentro das { } de bloco.
```js
if (1 > 0) {
  let nome = ‘Ana’;
  console.log(nome); // ‘Ana’
}

// variável `nome` não está acessível
console.log(nome); // Error: nome is not defined
```

#### Escopo de função
- Função: Que está dentro de uma função e pode ser chamado apenas dentro desta função.
  - Variáveis declaradas dentro de uma função são consideradas “locais” (ou seja, o oposto de “globais”) e não podem ser acessadas por código que esteja fora do bloco da função.
```js
function cumprimentar() {
  const nome = 'Camila'; // variável local
  const cumprimento = 'Olá'; // variável local
  console.log(`${cumprimento}, ${nome}!`); // “Olá, Camila!”
}

// as variáveis não podem ser acessada de fora da função
console.log(`${cumprimento}, ${nome}!`); // Dará erro de “not defined” no console
```

#### Escopo global
- Global: Pode ser chamado em qualquer local do script.
  - Qualquer variável que esteja no escopo global pode ser acessada por outras partes do programa. Uma variável é considerada global quando não é declarada dentro de nenhuma função ou bloco.
```js
const nome = ‘Camila’; // variável global

function cumprimentar() {
  console.log(`Olá, ${nome}!`); // Acessa a var global
}

cumprimentar(); // ‘Olá, Camila!”
```

### Var, let e const
Todas as variáveis que declararmos **sem passar seu tipo**, como **var, let ou const** será automaticamente **atribuido como var**.

#### var
- `var`: Uma variável que pode ser declarada dentro de um escopo de bloco e poder ser acesada fora dele.
  - Variáveis declaradas com `var` não seguem a regra do escopo de bloco! Elas serão consideradas globais e poderão ser acessadas de fora do bloco.
  - > A falta de “controle” de escopo é um dos motivos pelo qual o uso de `var` foi abandonado e as boas práticas atuais recomendam apenas o uso de `const` e `let`.

#### let
- `let`: Variável que é declarada e pode ser acessada/alterada em seus escopos internos, ou seja, se declarado globalmente, pode ser alterada por função ou bloco. Mas, caso declarado em escopo reduzido, não poderá acessar externamente a este escopo (se declarado dentro de um bloco, não poderá ser acessado fora dele)

#### const
- `const`: Variável que não pode ser alterada.

#### Exemplos
```js
estudante = 'Fulano'; // esta variável será um var
```

Ou seja, duas situações diferentes:
```js
// Opção var no bloco
  /*
  Reatribuição da variável estudante
  */
if (1 > 0) {
    var estudante = 'Caroline'; // variavel #1
    console.log(estudante)
}

estudante = 'Ana'; // variavel #1
console.log(estudante);

// Opção let no bloco
  /* 
  Agora temos duas variaveis estudante
  a let estudante e a var estudante
  */
if (1 > 0) {
    let estudante = 'Caroline'; // variavel #1
    console.log(estudante)
}

estudante = 'Ana'; // variavel #2 (aqui é var)
console.log(estudante);
```

### Proteção com const
Um ponto crucial da utilização do `const` é proteger a variável de alterações indesejadas em escopo distinto do projeto. Pois, **uma variável que está fora de um bloco pode ser alterada por uma variável que está dentro de um bloco.**

Alteração da variável dentro do bloco:
```js
let estudante;

if (1 > 0) {
    estudante = 'Caroline';
    console.log(estudante)
}

estudante = 'Ana';
console.log(estudante);
```

Protegendo a alteração
```js
const estudante = 'Caroline';

if (1 > 0) {
    estudante = 'Caroline';
    console.log(estudante)
}

estudante = 'Ana';
console.log(estudante);
```

Por isso, só usamos `let` onde expressamente precisamos.

## TRANSPILANDO (BABEL)
Para garantir a compatibilidade, ferramentas como transpiladores (por exemplo, Babel) são utilizadas para converter código escrito em versões mais recentes do JavaScript (como ES6+) para versões mais antigas, permitindo que seja executado em ambientes que não suportam esses recursos mais recentes.

A retrocompatibilidade é essencial para usar o JavaScript em front-end por basicamente dois motivos:
- Não é possível garantir que os computadores clientes que acessam as páginas web estejam sempre atualizados com as últimas versões dos navegadores.
- Os próprios navegadores levam algum tempo para atualizarem seus interpretadores de acordo com as últimas atualizações da linguagem.

No caso do Node.js este problema não é tão grande, pois quem desenvolve a aplicação escolhe qual a versão que quer utilizar do Node.js e adequa o computador-servidor para que execute o código de acordo. Porém, a questão da retrocompatibilidade fez com que alguns comportamentos das primeiras versões do JS não pudessem ser corrigidos, como o null que veremos mais adiante neste curso.

## LIDANDO COM ERROS
Do topo da linha em diante:
- Caminho do arquivo que deu problem : linha do erro
- Comando que deu erro e seu ponto exato
```bash
console.log(variavel);
            ^
```
- Tipo do erro e motivo
```bash
ReferenceError: variavel is not defined
```
- Agora vem o stacktrace
  - Pilha de comandos que foram chamados internamente pelo node que foi executado pelo programa
  - Além da mensagem de erro, o node mostra todo o caminho dos comandos executados até dar o problema

# <span style="color: #87BBA2">03. Tipo de dados</span>

## NUMBER
Sempre importante levarmos em consideração os tipos de dados que estamos trabalhando:

Abaixo temos um exemplo do tipo de operação realizado entre tipos de dados distintos:
```js
const notaPrimeiroBi = 8;
const notaSegundoBi = 6.3;
const notaTerceiroBi = -2;
const notaQuartoBi = '5';

/*
Vai realizar a soma entre o primeiro, segundo e terceiro bimestre
concatenando com o valo do quarto bimestre
*/
const total = notaPrimeiroBi + notaSegundoBi + notaTerceiroBi + notaQuartoBi;
console.log(total); // retorna 12.35 ao invés de 17.3

// Demonstrando o operador + como concatenador
const nome = 'Fulano';
console.log('Olá ' + nome);
```

Percebemos que o mesmo operador realizará ações diferentes frente ao tipo de dado com que ele está trabalhando.

### Convertendo para número e trabalhando com ele
```js
const notaPrimeiroBi = 8;
const notaSegundoBi = 6.3;
const notaTerceiroBi = -2;
const notaQuartoBi = Number.parseInt('5'); // Convertendo

const total = notaPrimeiroBi + notaSegundoBi + notaTerceiroBi + notaQuartoBi;
console.log(total); // Retorna 17.3

/*
.toFixed é um método da classe Number. No caso, como todos os
tipos são int ou float, o tipo da variável será "number".
Ao passar o mouse sobre a variável total veremos que agora estará
como "number"
*/
console.log('A média é ' + total.toFixed(2)); // Retorna 'A média é 17.30'
```

## STRING
```js
const estudante = 'Caroline';
const docente = 'Ana';
const cumprimento = 'Nosso lema é "estudar bastante"!';
/*
Usando acento grave pra possibilitar usar os dois acentos
para integrar a string
*/
const citacao = `Ju diz: "Nosso lema é 'estudar bastante!'"`;

console.log(cumprimento);
console.log(citacao);

// STRING COM +
// Concatenando com operador +
console.log('A estudante chama ' + estudante);

// STRING COM TEMPLATE STRING
// Concatenando com template string (mais moderno)
console.log(`A estudante chama ${estudante}`);


// MANIPULANDO STRING
console.log(`Agora, deixando em maiusculo o nome de ${estudante.toUpperCase()}`)
```

## BOOLEAN
Muito utilizado para retornar valor de SIM/NÃO, VEDADEIRO/FALSO, pois o código não entenderá o que é o texto "SIM", mas sim, entender que isso é uma sequencia de letras. Já um Boolean, todos os códigos entenderão e poderemos utilizar validações especificas.

```js
const estudante = 'Fernando';
const estaAprovado = true;

// estaAprovado === true
if (estaAprovado) {
    console.log('Parabéns, boas festas');
} else {
    console.log('REPROVADO, boas festas');
}

if (estudante === 'Fernando') {
    console.log(`Olá, ${estudante}`);
} else {
    console.log('Quem é você?');
}
```

### Sobre o uso do operador de igualdade estrita (===)
Em JavaScript, o operador `===` é conhecido como o operador de igualdade estrita, enquanto `==` é o operador de igualdade frouxa. A principal diferença entre eles é como eles tratam os tipos de dados:

- **`==` (igualdade frouxa)**: Este operador compara os valores após converter os tipos de dados, se necessário. Por exemplo, `5 == '5'` retornará `true` porque ele converte a string `'5'` para o número `5` antes de comparar.

- **`===` (igualdade estrita)**: Este operador compara tanto os valores quanto os tipos de dados, sem fazer qualquer conversão. Por exemplo, `5 === '5'` retornará `false` porque um é número e o outro é string.

Usar `===` é geralmente considerado uma prática melhor porque evita resultados inesperados devido à conversão de tipos. Isso torna o código mais previsível e menos propenso a erros.

Se precisar de mais alguma coisa, estou aqui para ajudar!

## NULL E UNDEFINED

### Valor indefinido != Não existe valor
null geralmente aparece em situações de cadastro, onde tempos um campo
mas existe nenhum valor nele. Mas, o campo ainda existe.

Outra diferença é com AS OPERAÇÕES:
- Operações com null, o null se comporta como 0
- Operações com undefined, o resultado será NaN.
    - NaN: Valor do tipo number que representa qualquer operação matematica
    mal formada

### Usando typeof
Para fazer validações do tipo de uma variável ou valor, usa-se o `typeof`.
- Importante: É um erro do Javascript, mas, quando damos `typeof` em um valor `null`, o seu retorno será `object`. É importantíssimo levar isso em consideração.

### undefined
`undefined` é um tipo não muito comum em outras linguagen de programação, criado no Javascript para evitar alguns erros em páginas web.

`undefined` indica que uma variável está associada a nenhuma valor no momento em que ela foi acessada
- Costuma indicar que uma operação não aconteceu como deveria
- Ou, está tentando pegar um valor que não está acessivel naquele momento
- Ou, resultado de operação sem return

`undefined` e `null` são tipos primitivos.
- Importante ter isso em mente: `undefined` é uma indicação de que algo no código pode não ter acontecido como esperado.

# <span style="color: #87BBA2">04. Operadores</span>

## OPERADORES ARITMÉTICOS
```js
const nota1 = 8;
const nota2 = 6.3;
const nota3 = 7;
const nota4 = 9.3;

let media = (nota1 + nota2 + nota3 + nota4) / 4;

if (media >= 7) {
    // Incremento: media = media + media * 0.1
    media += media * 0.1;
}

console.log(`Média é ${media.toFixed(2)}`);
```

Lembre-se da precedência, ou seja, a ordem de resolução de uma equação aritmética.

## OPERADORES LÓGICOS
```js
const notaFinal = 6;
const faltas = 5;

if (notaFinal < 7 || faltas > 4) {
    console.log('reprovado, boas festas')
} else {
    console.log('Recuperação. Faltou demais ou tirou menos')
}

if (notaFinal < 7 && faltas > 4) {
    console.log('reprovado, boas festas')
} else {
    console.log('Aprovado')
}
```

## TRUTHY E FALSY
Em JavaScript, um valor truthy é aquele que se traduz como verdadeiro quando avaliado em um contexto booleano. Falsy, é a mesma lógica mas retornadas como falso.

### Negação
```js
const notaFinal = 6;
const faltas = 5;
const advertencias = 0;

if (faltas >= 2 && !advertencias) {
    console.log('recebeu bonus');
} else {
    console.log('não recebeu bônus');
}
```
- O `0` é interpretado como Falsy, logo, quando aplicamos a negação na advertencia ele será transformado em Truthy.

Interessantissimo, caso aplicarmos operador de negação em um valor numérico, transformamos este em um booleano e o invertemos:
- Caso o valor seja 0: O retorno será True (False invertido)
- Caso o valor tenha algum valor numérico (positivo ou negativo): O retorno será False (True invertido)

Ou seja, uma forma de transformar um valor numérico (e provavelmente, outros tipos de valores) em boolenado não invertido, é realizando uma dupla negação (!!):
- valor 0 com dupla negação: O retorno será False (False invertido > True, True invertido > False)
- Qualquer valor numerico: O retorno será True (True invertido > False, False invertido > True)
```js
const advertencias = 2;

console.log(advertencias); // retorno Valor: 2
console.log(!advertencias); // retorno Bool negação: False
console.log(!!advertencias); // retorno Boll dupla negação: True
```

## OPERADORES DE COMPARAÇÃO

Sobre os operadores de igualdade, por via de regra, utilize a estrita (`===`) para ter mais segurança sobre a comparação a ser feita e não ocorrer casos inesperados.
```js
const aprovado = ture;

if (aprovado === true) {
    console.log('aprovado');
}

/*
IGUALDADE FROUXA
Compara só o conteúdo
- JS faz algumas conversões por baixo dos panos
*/
if ('0' == 0) {
    console.log('Passou');
} else {
    console.log('Não passou');
}

/* 
IGUALDADE ESTRITA
Compara conteúdo e seu tipo
- Nenhuma conversão feita, mais seguro pela restrição
*/
if ('0' === 0) {
    console.log('Passou');
} else {
    console.log('Não passou');
}
```

# <span style="color: #87BBA2">04. Funções</span>

## FUNÇÕES
Veremos nas funções abaixo o termo **Hoisting**. Significa "içar" ou "levantar". Uma caracteristica de hoisting é quando seu comando já é lido antes de percorrer linha a linha, ou seja, o interpretador "iça" sua leitura, "iça" o comando para o topo de leitura.

Ou seja, se uma declaração de função ocorrer no fim da aplicação, se ela possui hoisting, essa função poderá ser chamada no início da aplicação. Caso não possua hoisting, o interpretador só considerará a existencia dessa função quando passar pela linha especifica dele (não içando-o).

Uma função sem hoisting só pode ser chamada **após sua declaração**, onde o interpretador só o levará em consideração quando passar por sua declaração. Isso geralmente ocorre em funções anonimas (e acho que em funções lambdas também), onde o interpretador só realizará a operação quando passar por ela, não tendo sua lógica imediatamente realizada como ocorre com as declarações clássicas.
- Será que isso é feito para dar agilidade no processamento, chamando as funções apenas quando necessário?

### Declaração de função
Forma clássica de declarar uma função, tendo
- Palavra function
- Nome da função
- Seus parametros
- Corpo (bloco)
- **Hoisting:** Sim!

```js
function exibeInfosEstudante(nome, nota) {
  return `o nome é ${nome} e a nota é ${nota}`;
}

console.log(exibeInfosEstudante('Caroline', 10));
// retorna "o nome é Caroline e a nota é 10";
```

### Expressão de função
Forma alternativa, bastante comum, que é atribuir uma função a uma `const`:
- inicia com const
- nome da função
- atribuição seguido da palavra function e seus parametros
- corpo da função (bloco)
- **Hoisting:** Não!

Expressão de função é tido como uma **função anonima**.

```js
const estudanteReprovou = function (notaFinal, faltas) {
  if (notaFinal < 7 && faltas > 4) {
    return true;
  } else {
    return false;
  }
}

console.log(estudanteReprovou(6, 5));
```

### Arrow function
Também é uma expressão de função, sendo a aplicação **mais moderna** de funções.
- inicia com const
- nome da função
- atribuição seguido dos parametros
- Arrow (=>)
- corpo da função (bloco)
- **Hoisting:** Não!

Por ser uma sintaxe mais moderna de uma expressão de função, ela também é uma **função anonima**

#### Multiplas instruções
```js
const estudanteReprovou = (notaFinal, faltas) => {
  if (notaFinal < 7 && faltas > 4) {
    return true;
  } else {
    return false;
  }
}

console.log(estudanteReprovou(6, 5));
```

#### Instrução única
Em instruções únicas, podemos suprimir:
- Chaves
- Palavra return

Neste caso, ou suprimimos os dois, ou mostramos os dois
```js
// Suprimindo
const exibeNome = (nome) => nome;

// Mostrando
const exibeNome = (nome) => { 
  return nome
};
```

Essa sintaxe, a resumida, é **muito muito muito** utilizada nas **funções dentro de funções (callbacks functions)** e funções de instrução única.