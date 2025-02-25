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
- **For...in** é utilizado para iterar um objeto, acessando, a cada iteração, uma chave do objeto indicado. Ou seja, para o seguinte objeto, temos o seguinte retorno:
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

## SOBRE APIS

### O que são APIs?
APIs são interfaces entre aplicações. Podemos pensar em APIs como pontos de contato ou comunicação entre partes de um sistema ou entre sistemas diferentes, por exemplo:

O back-end de uma aplicação disponibiliza uma API para que o front-end possa buscar dados para popular uma página (no caso da API da Alura).
Uma aplicação quer utilizar um sistema de busca de CEPs disponibilizado por terceiros. O serviço de busca disponibiliza uma API para ser usada pela aplicação (um exemplo famoso é o ViaCEP).
Grande parte dos serviços em nuvem, como a AWS e o Google Cloud, disponibilizam APIs para que clientes possam utilizar seus serviços.
Parece muita coisa? Não se preocupe! Nas próximas formações de Node.js vamos abordar a fundo os usos e os tipos de API, além de criarmos nossas próprias APIs.

### APIs e JSON
O formato JSON é o padrão atual para envio de recebimento de dados entre aplicações. Na prática, isso significa que usamos JSON para, por exemplo:
- Um front-end pegar dados de um formulário em uma página e enviar para o back-end criar um cadastro de cliente, como em {“nome”: “José”, “email”: “jose@email.com”, “telefone”: “551199999999”};
- Um back-end consultar dados armazenados em tabelas de um banco de dados e formatá-los em JSON para enviá-los ao front (como a API da Alura).
E como é feito esse envio e recebimento de JSON?

### JSON e requisições
Quando queremos “transitar” um objeto JSON entre computadores na web através do protocolo HTTP é necessário transformar toda a estrutura em strings, pois nessa comunicação trafegam apenas dados em texto.

Por esse motivo, é bastante comum a operação de transformar um JSON em string e também reconverter um texto em JSON para que o objeto possa ser utilizado pelo programa.

Você vai ter oportunidade de praticar mais com APIs e com o envio e recebimento de JSON nas próximas formações e cursos de Node.js.

## LENDO UM ARQUIVO JSoN
Com o arquivo json posicionado em nosso projeto, fazemos a seguinte operação:

**Conteúdo Json**
```json
{
    "nome": "Ana",
    "idade": 32,
    "cpf": "23423423423",
    "email": "ana@email.com",
    "telefones": ["551198745632", "551198745633"],
    "endereco": {
        "rua": "Rua Joseph Climber",
        "numero": "45",
        "complemento": "apto 43"
    }
}
```

**Realizando operação com o Json**
```js
// IMPORTAÇÃO
const estudante = require('../assets/estudante.json');

console.log(estudante); // O mesmo contéudo do arquivo Json
console.log(typeof estudante); // Tipo de dado: Object

const chaves = Object.keys
```
O que podemos observar
- O tipo desta variável é `Object`, ou seja, o JavaScript já realiza uma certa conversão deste elemento json em um Objeto em JavaScript

Já que o JavaScript realizou essa conversão, podemos executar operações de objeto nesta variável:
```js
const chaves = Object.keys(estudante);
console.log(chaves); // Retorno: [ 'nome', 'idade', 'cpf', 'email', 'telefones', 'endereco' ]
```
O que é importante entender:
- `Json` não é um Objeto JavaScript, para utilizarmos, precisaremos convertê-lo e assim conseguiremos utilizar os métodos de objetos.

### Nota
Com o avançar do curso veremos a versão mais moderna de realizar uma importação Node, que seria o `import from` ao invés do `require`:
```js
import estudante from '../assets/estudante.json'; // Versão nova
const estudante = require('../assets/estudante.json'); // Versão antiga (nativa)
```

Estamos utilizando `require` no momento por ser nativo e a outra importação demandar configuração, mas, apenas por esse motivo mesmo. No momento, isso não gerará impacto para nós.

### Require como conversor de Json para JavaScript Object
- **A função require não é apenas para importação**, mas sim, **também realiza a conversão de um arquivo Json em Objeto JavaScript**. É importante ter essa funcionalidade em mente.

## OPERAÇÕES COM JSON
Uma comunicação Cliente/Servidor, não podemos mandar um arquivo `.json`, não posso mandar um arquivo `.js`, e sim, apenas fazer essa conversa através de **strings**.

### Convertendo a requisição em string
Faremos essa operação para possibilitar o envio de uma requisição e, consequentemente, ela ser recebida:
```js
const estudante = require('../assets/estudante.json');

const stringEstudante = JSON.stringify(estudante);
console.log(stringEstudante);
/*
Retorno: {"nome":"Ana","idade":32,"cpf":"23423423423","email":"ana@email.com","telefones":["551198745632","551
198745633"],"endereco":{"rua":"Rua Joseph Climber","numero":"45","complemento":"apto 43"}}
*/
console.log(typeof stringEstudante); // Retorna: string
```
Agora, com essa conversão, nossa aplicação backend conseguira mandar isso através de uma requição HTTP para o Frontend.

Mas, se tentarmos acessar uma propriedade após a conversão?
```js
console.log(stringEstudante.nome); // Retorna: undefined
```
Após convertê-lo, ele perderá a caracteristica de ser um Objeto e passará a ser uma string, logo, não teremos o mesmo controle em função de seu tipo distinto.

Observação
- É mais um caso que o JavaScript não retorna um erro

E como podemos retornar seu estado para ser um `Objeto`?
```js
// Parseando de String para Json
const objEstudante = JSON.parse(stringEstudante);
console.log(objEstudante); // Retorno: A mesma estrutura que está no arquivo Json.
console.log(objEstudante.nome); // Retorno: Ana
```

### Concluindo
- Um Objeto JavaScript é feito para rodar dentro de uma aplicação JavaScript
- As strings nós utilizamos para transmitir os dados entre conexões, por exemplo, através de protocolo HTTP e o JSON empresta esse padrão de objeto JavaScript por ser de uma leitura simples, mais simples do que o XML

## COPIAR OBJETOS
Aprendemos a diferença entre **atribuição de valor (primitivos)** e **atribuição de referencia (objetos, arrays e afins)**. Agora, como podemos cloná-los?

Já conhecemos copiar com **Spread Operator** e, saiba mais, vimos como fazer a cópia com **JSON.parse(JSON.stringfy())**. Mas, também existe o método nativo chamado **structuredClone()**. Qual utilizar?

### Comparação: JSON vs. Spread Operator (`...`)

#### 🔹 **Usando JSON**
```js
const copiaProfunda = JSON.parse(JSON.stringify(objetoOriginal));
```
**Prós**:
✅ Faz uma **cópia profunda** (deep copy), ou seja, copia todos os valores, incluindo objetos aninhados.  
✅ Garante que a cópia seja independente do original.  

**Contras**:
❌ **Não copia funções** – se o objeto tiver métodos (funções), eles serão perdidos.  
❌ **Não copia valores `undefined`, `NaN`, `Infinity`** – esses valores desaparecem na conversão.  
❌ **Não mantém referências a objetos complexos (como Map, Set, Date, RegExp)** – eles podem ser convertidos para strings ou perderem a funcionalidade.  
❌ Pode ser **mais lento** para objetos grandes devido ao parsing de JSON.  

---

#### 🔹 **Usando o Spread Operator (`...`)**
```js
const copiaRasa = { ...objetoOriginal };
```
**Prós**:
✅ **Mais rápido** para objetos simples e rasos.  
✅ **Preserva valores como `undefined`, funções e referências a objetos complexos**.  

**Contras**:
❌ Faz apenas uma **cópia rasa** (shallow copy) – se houver objetos aninhados, a referência deles será mantida na cópia.  

```js
const objetoOriginal = { chave: { subchave: 'valor' } };
const copiaRasa = { ...objetoOriginal };

copiaRasa.chave.subchave = 'novoValor';
console.log(objetoOriginal.chave.subchave); // Saída: novoValor (efeito colateral)
```

---

### 🚀 **Qual usar?**
✔ **Se o objeto for simples e raso** → `...` (Spread Operator) é mais rápido e mantém propriedades especiais.  
✔ **Se precisar de uma cópia profunda sem objetos complexos** → `JSON.parse(JSON.stringify(obj))` pode ser útil.  
✔ **Se precisar de uma cópia profunda mais robusta** → Use `structuredClone()` (nativo no navegador) ou bibliotecas como `lodash.cloneDeep()`.

Exemplo com `structuredClone()`:
```js
const copiaProfunda = structuredClone(objetoOriginal);
```
📌 **Esse método preserva funções e valores especiais!**  

Se precisar de algo mais avançado, me chama! 😃

# <span style="color: #87BBA2">MANIPULANDO LISTAS DE OBJETOS</span>

## OPERAÇÕES COM JSON (ENCONTRANDO OBJETO)
Agora vamos praticar a manipulação de elementos de JSON
```js
const estudantes = require('../assets/estudantes.json');

function buscaInformacao(lista, chave, valor) {
  /*
  A função fará: Busque estudante onde Chave (pode ser nome, email, telefone e afins)
  é igual ao valor informado.

  Ou seja, podemos dizer: se estudante['nome'] === 'Olva', o retorno será a primeira
  ocorrencia encontrada ou undefined caso não encontrar.
  */
  return lista.find((estudante) => estudante[chave] === valor);
}

const estudanteEcontrado = buscaInformacao(estudantes, 'nome', 'Juliet');
const estudanteNaoEcontrado = buscaInformacao(estudantes, 'nome', 'ABC');
console.log(estudanteEcontrado); // Retorna: Objeto Juliet
console.log(estudanteNaoEcontrado); // Retorna: undefined
```
O que um método de Array (o `.find()`) está fazendo no meio deste Objeto?
- Visualizando o `estudantes.json`, podemos ver que ele é um grande **array de informações**
  - Um Json pode ser um Objeto, assim como pode ser uma Lista dos tipos ao que ele aceita.
- O retorno do método `.find()` é a primeira ocorrência ou undefined

**Temos um problema nessa função**
- Quando vamos buscar por telefone, mesmo passando um telefone existente receberemos um `undefined`, uma vez que os telefones estão sendo armazenados como array.

**Como arrumar?**
- Ao invés de utilizar um operador de comparação (`===`), utilizaremos o método `.includes()`, que, pelo que entendi, busca se este dado existe em uma estrutura de dados independente de como ele está armazenado.
```js
const estudantes = require('../assets/estudantes.json');

// Função ajustada
function buscaInformacao(lista, chave, valor) {
  return lista.find((estudante) => estudante[chave].includes(valor));
}

const estudanteEcontrado = buscaInformacao(estudantes, 'nome', 'Juliet');
const telefoneEcontrado = buscaInformacao(estudantes, 'telefone', '9466883489');
console.log(estudanteEcontrado); // Retorno: Objeto encontrado
console.log(telefoneEcontrado); // Retorno: Objeto encontrado
```

### Concluindo
O que fizemos agora é algo muito comum no dia a dia, que são forma de acessar e capturar elementos. Neste exemplo, fizemos a captura com formas de acessar uma Array e capturar os objetos que nela existem.

## FILTRANDO OBJETOS
Quando estamos trabalhando com find, desejamos encontrar uma informação especifica, mas, agora, desejamos fazer um filtro.

```js
const estudantes = require('./assets/estudantes.json');

// Função para verificar quais estudantes não possuem a propriedade informada em seu endereço
function filtraPorPropriedade(lista, propriedadade) {
    return lista.filter((estudante) => {
        return !estudante.endereço.hasOwnProperty(propriedadade);
    })
}

const listaEnderecosIncompletos = filtraPorPropriedade(estudantes, 'cep').endereço
console.log(listaEnderecosIncompletos);
```
**O que é hasOwnProperty?**
- Função para verificar a existencia da propriedade inserida em seus parenteses no objeto que se chama este método
> The hasOwnProperty() method of Object instances returns a boolean indicating whether this object has the specified property as its own property (as opposed to inheriting it).
- Ou seja, verifica se o objeto possui a propriedade informada como própria. (Ou seja, desconsidera propriedades herdadas).

### Lembrando diferença de Find e Filter
- **Find**: Retorna **A primeira ocorrencia** ou undefined.
  - O método find() retorna o valor do primeiro elemento do array que satisfizer a função de teste provida. Caso contrario, undefined é retornado.
- **Filter**: Retorna **Array de ocorrencias** ou array vazia.
  - O método filter() cria um novo array com todos os elementos que passaram no teste implementado pela função fornecida.

## ORDENANDO OBJETOS
Outra operação comum é ordenação dos elementos em uma array

```js
const estudantes = require('./assets/estudantes.json');

function ordena(lista, propriedade) {
    return lista.sort((a, b) => {
        if (a[propriedade] < b[propriedade]) return -1;
        if (a[propriedade] > b[propriedade]) return 1;
        return 0;
    });
}

const listaOrdenada = ordena(estudantes, 'nome');
console.log(listaOrdenada);
```
**O que é .sort()**?
- Método do JavaScript de ordenação de Array conforme lógica que indicarmos.
> O método sort() ordena os elementos do próprio array e retorna o array. A ordenação não é necessariamente estável. A ordenação padrão é de acordo com a pontuação de código unicode.
>
> A complexidade do tempo de execução ou a quantidade de memória utilizada pela ordenação não pode ser garantido e depende da implementação realizada.

O .sort() utiliza lógica de comparação para ordenar os elementos, e, também, tem comportamento padrão. [Veja mais aqui](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).

Exemplo:
```js
var stringArray = ["Blue", "Humpback", "Beluga"];
var numericStringArray = ["80", "9", "700"];
var numberArray = [40, 1, 5, 200];
var mixedNumericArray = ["80", "9", "700", 40, 1, 5, 200];

function compararNumeros(a, b) {
  return a - b;
}

console.log("stringArray:", stringArray.join());
console.log("Ordenada:", stringArray.sort());

console.log("numberArray:", numberArray.join());
console.log("Ordenada sem função de comparação:", numberArray.sort());
console.log("Ordenada com compararNumeros:", numberArray.sort(compararNumeros));

console.log("numericStringArray:", numericStringArray.join());
console.log("Ordenada sem função de comparação:", numericStringArray.sort());
console.log(
  "Ordenada com compararNumeros:",
  numericStringArray.sort(compararNumeros),
);

console.log("mixedNumericArray:", mixedNumericArray.join());
console.log("Ordenada sem função de comparação:", mixedNumericArray.sort());
console.log(
  "Ordenada com compararNumeros:",
  mixedNumericArray.sort(compararNumeros),
);

// RETORNOS
/* stringArray: Blue,Humpback,Beluga
Ordenada: Beluga,Blue,Humpback

numberArray: 40,1,5,200
Ordenada sem função de comparação: 1,200,40,5
Ordenada com compararNumeros: 1,5,40,200

numericStringArray: 80,9,700
Ordenada sem função de comparação: 700,80,9
Ordenada com compararNumeros: 9,80,700

mixedNumericArray: 80,9,700,40,1,5,200
Ordenada sem função de comparação: 1,200,40,5,700,80,9
Ordenada com compararNumeros: 1,5,9,40,80,200,700 */
```

### Explicação Alura
Utilizamos o sort() de array e tem duas formas de ser utilizado:
- **A forma mais simples (sem parametros)**
  - não possibilita nos acessarmos as propriedades internas de um objeto.
  - Funciona apenas para textos, e não para valores numéricos, (como vimos, ele pega o valor unicode, ou seja, 100 virá antes de 2 pois o valor numérico unicode de 100, que começa com 1, vem antes de 2)
  - Ideal mais para lista de strings.
- **Forma de comparação (a, b)**
  - a e b são representações dos elementos internos a array, por exemplo, a é o elemento atualmente iterado e o b é o elemento subsequente ao a.
  - Ao fazermos comparação, caso a comparação for negativa, a fica antes de b, caso positiva, b fica antes de a, caso 0, mantêm-se como está.
  - No caso, compara-se string com operador lógico pois o sort verifica o valor unicode da primeira letra, ou seja, a palavra "Abelha" tem valor menor que "Bufalo", já que o valor unicode da palavra A é menor que a palavra B.
  - Isso gera algumas particularidades, por isso, é importante ter em mente [a documentação](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/sort).