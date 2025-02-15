# <span style="color: #87BBA2">===   JavaScript: conhecendo objetos   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">===   MÉTODO: Speed Run   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">O QUE SÃO OBJETOS</span>

## O QUE SÃO OBJETOS
Uma estrutura de dados ideal para grupos mais complexos de informações.

Uma Array, por exemplo, funciona muito bem para guardar grupos de u mtipo só de dados e acessando-os através de indices.

Mas, quando precisamos "imitar a realidade", como descrever uma pessoa, descrever um usuário, descrever um computador, ou seja, são conjuntos de varias informações diferentes, podemos utilizar a estrutura de dados chamada de "Objeto", que busca **refletir, de forma bastante abstrada, as coisas da vida real e carregar caracteristicas/informações diversas**.

**Os objetos sempre serão compostos por uma estrutura de chaves e valores**.

## ACESSANDO OBJETOS COM NOTAÇÂO DE PONTO
```js
// Objeto
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript'
}
```
Acessando tudo: `console.log(estudante)`
Tipo do retorno: `Object`

### Notação de ponto
Forma de acessar um propriedade de um objeto através da separação por ponto. A cada ponto, é uma referência a uma propriedade interna àquele objeto.

Acessando proporiedade nome: `console.log(estudante.nome)`
Tipo do retorno: `Tipo do valor desta propriedade`

**Propriedade**: Conjunto de chave e valor

## ACESSANDO OBJETOS COM NOTAÇÂO DE COLCHETES
Ideal para acessar propriedades quando não sabemos de antemão quais são suas propriedades.

Notação de ponto, por exemplo, exige conhecimento prévio sobre quais são as propriedades daquele objeto.

```js
// Objeto
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript'
}

function exibeInfoEstudante(objEstudante, infoEstudante) {
  /*
  Não podemos ter notação de ponto aqui pois este escopo
  desconhece explicitamente quais propriedades existem neste objeto
  */

  /*
  Passando o nome da chave entre colchetes, acessaremos, então
  o seu valor.
  */
  return objEstudante[infoEstudante];
}

console.log(exibeInfoEstudante(estudante, 'nome'));
console.log(exibeInfoEstudante(estudante, 'idade'));
```

### Particularidade da notação por colchete
Com a notação de colchetes podemos passar uma propriedade como um dado variável.

O que foi feito acima seria a mesma coisa que acessarmos com notação de colchete passando o nome da chave diretamente:
```js
console.log(estudante['nome']);
console.log(estudante['idade']);
```

**Importante!:** É importante acessar com string, pois, é o nome da propriedade ao qual queremos coletar o seu valor. Caso colocarmos **sem aspas**, estaremos dando a instrução que dentro do colchetes é para coletar a **a propriedade do objeto estudante onde o nome de sua propriedade corresponda a variável chamada nome** e não **a propriedade do objeto estudante chamado nome**.

### Undefined quando propriedade inexistente
Comportamento importantíssimo de se alertar: **O JavaScript não retorna erro caso não identificar a propriedade que se tenta acessar, mas sim, retornará undefined**.

## ADICIONANDO E ALTERANDO
```js
// Objeto
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript'
}

estudante.telefone = '1111111'; // Propriedade criada com valor 1111111
estudante.nome = 'José Souza'; // Aletando valores existentes
```

Ou seja, se a propriedade não existe e atribuimos valor, ela será criada com aquele valor. Caso a propriedade já exista, nós alteraremos seu valor.

Podemos também construir um objeto através de um objeto vazio:
```js
const objetoConstruido = {};
const objetoConstruido.nome = 'Objeto construido 1';
```

## DELETANDO PROPRIEDADE
```js
const objPersonagem = {
 nome: "Gandalf",
 classe: "mago",
 nivel: "20",
 aliado: {
   nome: "Saruman",
   classe: "mago"
 },
 status: "desaparecido"
}

delete objPersonagem.aliado
delete objPersonagem["status"]
 
console.log(objPersonagem.aliado) //undefined
console.log(objPersonagem.status) //undefined
```

O valor de retorno do operador delete é um booleano, ou seja, retorna sempre true ou false para cada operação. Porém, é importante notar que ele não retorna false se tentarmos remover, por exemplo, uma propriedade que não existe no objeto
```js
const delProp = delete objPersonagem.aliado
const delPropInexistente = delete objPersonagem["endereco"]
 
console.log(delProp) //true
console.log(delPropInexistente) //true
```

# MANIPULANDO OBJETOS

## OBJETOS EM OBJETOS
Feito dessa maneira para representar dados mais complexos ou aproximar ainda mais da realidade, como exemplo:

```js
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript',
  bolsista: true,
  telefones: ['551199999998', '551199999993'],
}

estudante.endereco = {
  rua: 'Rua Joseph Climber',
  numero: '45',
  complemento: 'apto 43'
}

console.log(estudante.endereco.rua); // Rua Joseph Climber

/* Resultado do objeto neste momento
{
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript',
  bolsista: true,
  telefones: [ '551199999998', '551199999993' ],
  endereco: { rua: 'Rua Joseph Climber', numero: '45', complemento: 'apto 43' },
}****
*/
```

### Representando a realidade
Note o porque tornamos o endereço do estudante como um Objeto: Como queremos nos aproximar de uma descrição do mundo real, não faz sentido dizermos que "rua, numero, complemento" faz parte de um "estudante", mas sim que faz parte de um **endereço** e um estudante possui um endereço.

É um tópico que pode ser facil de se confundir e demandará bastante prática no dia a dia.

### Quando Array, quando Objeto
Quando precisamos juntar dados do mesmo tipo usamos **Arrays**, quando precisamos juntar dados diferentes que pertencem a um mesmo contexto, usamos **Objetos** e essas estruturas podem ser mescladas umas com as outras.
- Como lista de objetos, ou objetos com listas

## LISTAS DE OBJETOS
```js
// Montando objeto
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript',
  bolsista: true,
  telefones: ['551199999998', '551199999993'],
  enderecos: [{
    rua: 'Rua Joseph Climber',
    numero: '45',
    complemento: 'apto 43'
  }]
}

// Adicionando endereço à lista de endereços
estudante.enderecos.push({
  rua: 'Rua Dona Clotilde',
  numero: '71',
  complemento: ''
})

console.log(estudante.endereco); // Retorne todos os endereços na lista
console.log(estudante.endereco[0]); // Acessa o primeiro endereço retornando um obejto

// Filtrando lista de objetos de Endereços buscando apenas os que possuem complementos
const listaEnderecosComComplemento = estudante.endereco
  .filter((endereco) => endereco.complemento)

console.log(listaEnderecosComComplemento);
```

## FUNÇÕES
Podemos, também, declarar funções nos objetos que estamos criando, como no `estaAprovado` representado abaixo:
```js
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript',
  bolsista: true,
  telefones: ['551199999998', '551199999993'],
  media: 7.5,
  estaAprovado: function(mediaBase) {
    return this.media >= mediaBase ? true : false
  }
}

console.log(estudante.estaAprovado(8)); // true
```

### Sobre o this
Significa o acesso a uma propriedade **daquele objeto**, ou seja, "this object". Então, this.nomePropriedade acessaremos os valores das propriedades **daquele objeto**.

Vimos isso mais claramente quando montamos classes para separar quando coletamos os dados de uma classe ou de uma instancia dessa classe (objeto).

> O JavaScript utiliza essa palavra chave para fazer referencia ao contexto da função.

### Sobre o this e arrow function
A utilização do this em uma Arrow Function não tem um comportamento igual a quando declaramos uma função com `function`. Com o `function`, o this chama o contexto interno ao objeto a qual àquela função foi chamada.

Já com o `arrow function`, ele fica meio perdido em quanto ao seu contexto e acaba pegando de outro lugar, onde acredito que ele pegue do contexto da classe geral ao qual ele está inserido, e não ao objeto em questão.

### O .log() de console é um método?
Sim! O `.log()` do `console` é um método do objeto chamado `console`, sendo este um objeto global.

Tudo que utilizamos no JavaScript é basicamente ou uma propriedade de objeto, ou um método!
- Uma função que está sendo chamado dentro do contexto de um objeto chama-se **método**
- Uma função que está sendo chamado dentro de um contexto de uma classe se chama **método estático**

## ENTENDENDO O THIS E SEU COMPORTAMENTO EM FUNCTION E EM ARROW FUNCTION
No contexto de um objeto em Node.js, this refere-se ao próprio objeto no qual a função está sendo chamada. Ela é uma referência dinâmica, o que significa que o valor de this pode mudar dependendo do contexto em que a função é chamada.

No caso de métodos de objetos, o this se liga ao objeto que chamou o método. Confira este exemplo:
```js
const pessoa = {
  nome: "Maria",
  idade: 30,
  apresentar: function() {
    console.log(`Olá, meu nome é ${this.nome} e eu tenho ${this.idade} anos.`);
  }
};

pessoa.apresentar(); // Saída: Olá, meu nome é Maria e eu tenho 30 anos.
```

Aqui, this dentro da função apresentar faz referência ao objeto pessoa, a partir de onde a função está sendo executada.

### Arrow functions e o this
As arrow functions não possuem um this próprio. Em vez disso, elas herdam o valor de this do contexto em que foram definidas. Isso pode causar problemas em métodos de objetos, pois this pode não se referir ao objeto esperado. Por exemplo:
```js
const pessoa = {
  nome: "João",
  idade: 25,
  apresentar: () => {
    console.log(`Olá, meu nome é ${this.nome} e eu tenho ${this.idade} anos.`);
  }
};

pessoa.apresentar(); // Saída: Olá, meu nome é undefined e eu tenho undefined anos.
```
Neste exemplo, this dentro da função de seta não se refere ao objeto pessoa, resultando em valores indefinidos para nome e idade.

### Conclusão
Ao trabalhar com objetos em Node.js, é crucial compreender o comportamento de this para garantir referências corretas. Arrow functions podem ser inadequadas em certos contextos, especialmente ao definir métodos de objetos. Em vez disso, **opte por funções tradicionais ao criar métodos em objetos para garantir que this seja vinculado ao contexto apropriado, facilitando o acesso e manipulação de dados de forma consistente.**

## OBJETOS LITERAIS, SUAS CÓPIAS OU REFERENCIAS
Vimos anteriormente como é a estrutura de um objeto, com seus pares de chave e valor:
```js
const objPersonagem = {
 nome: "Gandalf",
 classe: "mago",
 nivel: "20"
}
```
O exemplo acima, assim como o que estamos criando durante esta aula, é o de um objeto literal.

Um objeto literal é um objeto criado com a notação literal, ou seja, uma lista de chave e valores dentro de chaves { }, que atribuímos a uma variável para que o valor possa ser acessado depois. Exatamente como no exemplo acima.

Objetos literais funcionam bem quando queremos ter um objeto único com seus próprios dados. Isso porque um objeto literal sempre aponta para um mesmo local na memória, mesmo se você criar cópias dele. Vejamos o código a seguir:
```js
const objPersonagem = {
 nome: "Gandalf",
 classe: "mago",
 nivel: "20"
}
 
const objPersonagem2 = objPersonagem
```
Se alterarmos apenas o objPersonagem2, o resultado é:
```js
const objPersonagem2 = objPersonagem
objPersonagem2.nome = "Saruman"
 
console.log(objPersonagem.nome) //Saruman
console.log(objPersonagem2.nome) //Saruman
```
A variável objPersonagem2 não fez uma cópia do objeto original, apenas serviu como referência para o objeto original objPersonagem. Assim, qualquer alteração em qualquer um dos objetos altera ambos. Isso porque o JavaScript, quando trabalha com objetos, acessa os valores deles fazendo referência ao original. mas não cria uma cópia. Já o acesso por cópia funciona com tipos primitivos (string, number, booleano, null, symbol):
```js
let num = 50
let num2 = num
 
num2 = 100
console.log(num) //50
console.log(num2) //100
```
Como podemos contornar esse comportamento quando criamos objetos? Além de utilizar a notação literal, objetos também podem ser criados através do método Object.create():
```js
const objPersonagem = {
 nome: "Gandalf",
 classe: "mago",
 nivel: "20"
}
 
const objPersonagem2 = Object.create(objPersonagem)
objPersonagem2.nome = "Saruman"
 
console.log(objPersonagem.nome) //Gandalf
console.log(objPersonagem2.nome) //Saruman
```
O método Object.create() cria um novo objeto utilizando como protótipo o objeto passado via parâmetro. Dessa forma, objPersonagem2 é uma instância diferente de objPersonagem e pode ser trabalhada de forma independente.

Você pode ver [mais exemplos do método Object.create() na documentação do MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Object/create).

# PERCORRENDO OBJETOS

## FOR..IN
Método para iterar (ação de repetição) um objeto.

### Diferença entre for...of e for...in
- **For...of** é utilizado, geralmente, para iterar uma lista de forma mais semantica, porém, com menos controle, iterando do iniciao ao fim da lista (array).
- **For...of** é utilizado para iterar um objeto, acessando, a cada iteração, uma chave do objeto indicado. Ou seja, para o seguinte objeto, temos o seguinte retorno:
```js
const estudante = {
  nome: 'José Silva',
  idade: 32,
  cpf: '12312312312',
  turma: 'JavaScript',
  bolsista: true,
  telefones: ['551199999998', '551199999993'],
  enderecos: [{
    rua: 'Rua Joseph Climber',
    numero: '45',
    complemento: 'apto 43'
  },
  {
    rua: 'Rua Dona Clotilde',
    numero: '71',
    complemento: null
  }]
}

for (const chave in estudante) {
    console.log(chave);
}

/* Retorno:
nome
idade
cpf
turma
bolsista
telefones
enderecos
*/
``` 

Ou seja, para acessar cada valor do objeto, podemos fazer a seguinte operação:
```js
for (const chave in estudante) {
    console.log(estudante[chave]);
}
```

### Problema com [object Object]
Nos deparamos com esse erro, como exemplo, quando tentamos passar um objeto em uma template string:
```js
for (let chave in estudante) {
    const texto = `a chave ${chave} tem o valor ${estudante[chave]}`
    console.log(texto);
}

/*
a chave nome tem o valor José Silva
a chave idade tem o valor 32
a chave cpf tem o valor 12312312312
a chave turma tem o valor JavaScript
a chave bolsista tem o valor true
a chave telefones tem o valor 5511999999998,5511999999993
a chave enderecos tem o valor [object Object],[object Object]
*/
```
Isso acontece pois o JavaScript tenta transformar a lista de objetos em String, porém, não gera o resultado desejado, tento como retorno `object Object`.

**O que um Template String faz**, ele tenta transformar todos os valores inseridos dentro dele em String, ou seja, todo o retorno do Template String será efetivamente uma String, mas, o caso acima é um exemplo de erro de conversão em função da complexidade da estrutura de dados que é um objetom logo, ele retorna a informação que trata-se de uma instancia de Objeto: `object Object`.

### Ajuste para ignorar os casos que dariam [object Object]

```js
for (let chave in estudante) {
    const tipo = typeof estudante[chave];
    if (tipo !== 'object' && tipo !== 'function')
        const texto = `a chave ${chave} tem o valor ${estudante[chave]}`
        console.log(texto);
}
```
**O que está acontecendo?**
- typeof coleta o tipo do dados
- Caso o tipo seja object ou function, ignore, pois, são os casos que causariam este erro
  - **DETALHE**: Importante lembrar que uma **array TAMBÉM É um Object, assim como null**. Ou seja, não existe "typeof array" ou "typeof null"; 