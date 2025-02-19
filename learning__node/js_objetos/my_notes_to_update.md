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

## OPERAÇÕES COM JSON
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