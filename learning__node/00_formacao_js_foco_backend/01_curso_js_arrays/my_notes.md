# <span style="color: #87BBA2">===   JavaScript: conhecendo arrays   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">01. O que são arrays</span>

## COMO FUNCIONAM AS ARRAYS
Um ponto importante é que **arrays no JavaScript aceitam diversos tipos de dados diferentes**: 
![alt text](assets\arrays.png)

Ou seja, na mesma array pode ter:
- numero
- string
- outra array
- objetos
- etc

Em JavaScript, **arrays também são conhecidas como listas**, ou, falando por completo, **lista ordenada de valores enumerados**.
- Um conteúdo unitário de uma array chama-se **item**
- A posição do item se chama **indice**

### Como JS trata as arrays
Quando se trata de como os índices são armazenados na memória em JavaScript, é importante entender que os arrays em JavaScript são implementados como objetos. Internamente, os índices são tratados como chaves (ou propriedades) de um objeto, onde cada chave é associada ao seu valor correspondente (o elemento do array).

A memória em JavaScript é gerenciada automaticamente pelo mecanismo do navegador ou do ambiente de execução. Quando você cria um array e adiciona elementos a ele, o mecanismo aloca espaço na memória para armazenar esses elementos sequencialmente, de acordo com seus índices.
![alt text](assets\array_memoria.png)

### Arrays esparsos
Em programação, chamamos os arrays onde os elementos não estão todos em índices contíguos (como no caso acima em que há “espaços” sem nenhum valor) de arrays esparsos (sparse arrays). Em arrays esparsos, a quantidade de elementos no array será menor ao número indicado pela propriedade length, e não equivalente.

Na prática, a maior parte dos arrays que trabalhamos no dia-a-dia não serão esparsos, e a maior parte dos interpretadores vai trabalhar com arrays esparsos da mesma forma que os arrays normais (que podem ser chamados de “densos”), com elementos undefined.

Porém, é importante entender o conceito para termos um entendimento melhor de como os arrays funcionam em JavaScript, especialmente em casos de manipulação e exclusão de elementos.

# <span style="color: #87BBA2">02. Alterando arrays</span>

## DIVIDINDO COM SLICE()
```js
const listaEstudantes = ['João', 'Juliana', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Guilherme', 'Aline', 'Fabiana', 'André', 'Carlos', 'Paulo', 'Bia', 'Vivian', 'Isabela', 'Vinícius', 'Renan', 'Renata', 'Daisy', 'Camilo'];

// Cortando do incio a metade
const sala1 = listaEstudantes.slice(0,listaEstudantes.length/2);
// Cortando da metade pro fim
const sala2 = listaEstudantes.slice(listaEstudantes.length/2);
// Printando
console.log(sala1);
console.log(sala2);
```
### Inicial inclusivo, final exclusivo
No método de slice, pede-se 2 parametros: o inicio e o fim. Como visto na documentação do MDN, o método considera o item de inicio mas desconsidera o item final, fazendo com que sala1 e sala2 não tenham informações sobrepostas.
- Note: na sala1, indicamos a posição inicial (indice 0) e a posição final (metade de Array.length, que nesse caso dará 10).
  - Nosso retorno da sala1 foram os itens de 0 a 9, o 10 não foi incluído (parou-se um antes)
- Na sala2 pedimos para iniciar da metade de Array.length (indice 10) até o final.
  - Nosso retorno foi o indice 10 até o fim da Array
- Ou seja, o indice 10, por mais que apareceu na posição final da sala1, não foi considerada na sala1 e mesmo utilizando o mesmo indice não houve sobreposição

Imporante, então, ter a seguinte questão em mente: No método Array.slice(), assim como em diversos métodos que exista um range de posição, **considera-se o item da posição inicial e não inclui o item da posição final**.

Ou seja: Muitos métodos e funções em linguagens de programação, como o slice() em JavaScript, utilizam esse conceito de **intervalo fechado no início e aberto no final**. Isso significa que o **índice inicial é inclusivo, enquanto o índice final é exclusivo**.

### Não altera a array e sim gera uma nova
Outra caracteristica do método slice é que ele não altera a array, como em pop e push, e sim, **cria uma nova array com base na primeira array**. 

## DIVIDINDO COM SPLICE()
Método para deletar itens a partir de uma posição desejada, podendo, opcionalmente, acrescentar elementos na mesma chamada
- Importante: **este método altera a array original, não criando uma cópia**

```js
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];

// Excluindo itens e adicionando um no lugar
// splice(posição_inicio, qtd_elementos_a_deletar, elemento_adicionar)
listaEstudantes.splice(1, 2, 'Rodrigo');

console.log(listaEstudantes) // [ 'João', 'Rodrigo', 'Lara', 'Marjorie', 'Leo' ]
```

Outras manipulações que podemos fazer é:
```js
// Deletando tudo a partir de uma posição
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
listaEstudantes.splice(1);
console.log(listaEstudantes) // [ 'João' ]

// A quantidade de itens pode passar
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
listaEstudantes.splice(3, 5);
console.log(listaEstudantes) // [ 'João', 'Ana', 'Caio' ]

// Passando separadamente, acrescenta normal e a deleção ocorre antes da adição
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
listaEstudantes.splice(3, 5, '1', '2', '3');
console.log(listaEstudantes) // [ 'João', 'Ana', 'Caio', '1', '2', '3' ]

// Assim acrescenta uma array dentro de outra array
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
const outraArray = ['1', '2', '3']
listaEstudantes.splice(3, 5, outraArray);
console.log(listaEstudantes) // [ 'João', 'Ana', 'Caio', ['1', '2', '3'] ]

// Adicionando elementos de dentro de outra array com operador de espalhamento
const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
const outraArray = ['1', '2', '3']
listaEstudantes.splice(3, 5, ...outraArray);
console.log(listaEstudantes) // [ 'João', 'Ana', 'Caio', '1', '2', '3' ]
```

# <span style="color: #87BBA2">04. Funções callback</span>

## MÉDIA COM FOREACH, UMA FUNÇÃO CALLBACK
O que é uma função callback?
- Uma função callback é aquela que serve como parâmetro para outra função, chamando-a de volta quando executamos a função principal (no caso, a função principal é aquela que chama a callback).
- Ou seja, chamamos de callback as funções que são passadas no parametro daquelas funções que solicitam outras funções, ou seja, de funções que pedem como parametro outra função (e a executará de forma "callback")

O que o forEach faz?
> Essa função vai ser executada para cada elemento do array. É o que chamamos de “função callback”, quando uma função é passada como parâmetro de outra função e executada dentro deste contexto.

```ts
const notas = [10. 6.5, 8, 7.5];

let somaDasNotas = 0;

// forEach é uma função callback
notas.forEach(function (nota) {
  somaDasNotas += nota;
});
```

O que está acontecendo no forEach?
- forEach retornará um elemento correspondente a um item a cada iteração e este retorno poderá ser coletado através do parâmetro passado na função callback, ou seja, o parametro interno à função callback coletará automaticamente o valor retornado pelo forEach.
- Imagino que seja por isso que é chamado de callback, pois, "nota" é um nome genérico que damos para o dado que o forEach está retornando para manipularmos.
- forEach retorna o dado, nos operamos utilizando-o (no caso, para incrementar em somaDasNotas) e forEach segue para o proximo passo, fornecendo no chamado "nota" o segundo elemento da array e por aí em diante.

### Utilizando callback com função externa
```ts
const notas = [10. 6.5, 8, 7.5];

let somaDasNotas = 0;

// forEach é uma função callback
notas.forEach(somaNotas);

function somaNotas (notas) {
  somaDasNotas += notas;
}
```
**Mas como estamos passando o parametro?**
- Note que estamos apenas referenciando a função somaNotas, ao invés de estarmos executando o método ao utilizar a chamada com os parenteses e parametro.
- O manejo do parametro, ou seja, o manejo de cada elemento de cada passo do loop é realizado internamente ao forEach
  - O método forEach **pegara cada um dos elementos e passará para dentro da função somaNOtas como sendo o parametro nota**

### Na documentação sobre forEach
Na documentação do **mdn web docs** visualizamos que a função forEach retornará um `undefined`, isso significa que este método executa o código que está dentro do bloco passado em seu parâmetro mas não retorna nada.
- Ou seja, conseguimos executar o que quisermos mas nada será retornado desta operação.

### Utilizando arrowfunction
```ts
const lista = [1, 2, 3, 4, 5];
let soma = 0;
 
lista.forEach(numero => soma += numero);
console.log(soma) //15
```
- Aqui estamos fazendo algo similar ao declarar a função da forma tradicional internamente ao forEach, porém com a sintaxe de arrow function.
- Ou seja:
```ts
// As 3 operações fazem a mesma coisa, mas
// por convenção utiliza-se as arrow function

// Declaração de função tradicional interna
funcaoPedeCallback(function(param) {
  // bloco texto
});

// Arrow function unilinha
funcaoPedeCallback(param =>
  //instrução de uma linha
)

// Arrow function multilinha
funcaoPedeCallback(param => {
  // Instruções multilinhas
});
```

Referente a utilizando a forma "tradicional" de declarar função quando esta é chamada de forma callback, Alura diz:
>Ou ainda, utilizando a palavra-chave function ao invés de arrow functions; essa forma de escrita não é usual, pois quando usamos funções callback o padrão adotado é o de arrow functions, mas serve para o propósito de legibilidade.

## REVISANDO CALLBACKS
Agora, veremos a utilização de callback na função `map`, destinada modificar cada elemento presente em uma array

```ts
const notas = [10, 9.5, 8, 7, 6].

const notasAtualizadas = notas.map((nota) => nota + 1 >= 10 ? 10 : nota + 1);
```

### Sobre a arrow function
- Substitui a declaração explicita de função e é muito recomendada sua utilização quando callback
```ts
// Notação de função explicita
const notasAtualizadas = notas.map(function (nota) {
  return nota + 1; // Essa função pede retorno para o callback
});

// Notação de arrow function multilinha
const notasAtualizadas = notas.map((nota) => {
  return nota +1;
});

// Notação de arrow function unilinha
/* 
- Não precisa dos parenteses no parametro, caso for um único
parametro
- Quando for uma unica linha, o retorno é automatico e não
precisa ser declarado
- Mas, concordo com a professora em que fica mais elegante
utilizar ((nota) => nota + 1)
*/
const notasAtualizadas = notas.map(nota => nota + 1 >= 10 ? 10 : nota + 1);
```

### Sobre a função map
Segundo o MDN (Mozzila):
> O método map chama a função callback recebida por parâmetro para cada elemento do Array original, em ordem, e constrói um novo array com base nos retornos de cada chamada. A função callback é chamada apenas para os elementos do array original que tiverem valores atribuídos; os elementos que estiverem como undefined, que tiverem sido removidos ou os que nunca tiveram valores atribuídos não serão considerados.

Ou seja, o map sempre irá retornar um array com os resultados, um array com cada retorno de função.

Por isso que a nossa variável `notasAtualizadas` é um array com cada um dos resultados, pois, cada resultado está sendo retornado para a fora da função callback e está sendo capturado dentro de um outro array, que chamamos de notasAtualizadas.

## ALTERANDO STRINGS COM MAP()
Deixando todos os nomes de uma lista em maisuculo

```ts
cosnt nomes = ["ana Julia", "Caio vinicius", "BIA silva"];
const nomesPadronizados = nome.map((nome) => nome.toUpperCase());
console.log(nomesPadronizados) // Retorno de todo conteúdo, agora maisuculo
```

Utilizamos o map para fazer qualquer tipo de alteração de forma iterável em uma array, ou seja, alterar os itens internos da lista (criando uma nova lista, não alterando diretamente a array)

## MAIS DENOMINAÇÕES SOBRE O QUE É CALLBACK
> O termo callback se refere à função que é “chamada de volta” dentro de outra função. Após o lançamento do ES6 (também conhecido como EcmaScript 2015) o uso desse tipo de método foi se consolidando, então é importante entender como utilizá-lo.

Ou seja, a função callback é aquela que será chamada (call) de volta na execução de outra função que espera como parametro uma função callback.

```ts
// Exemplo de uma função callback
function multiplicaPorDez(num) {
 return num * 10;
}

// Exemplo da chamada de uma função callback
const arraySomada = arrayNums.map(multiplicaPorDez);
```

Entendo que, callback é um estado de uma função. Caso ela seja chamada por outra função que espera receber uma função, a função chamada será uma callback neste momento.

Quem define se a função é uma callback é a função chamante, pois, ela determina que um dos seus parametros trata-se de uma função callback (que chamará esta função de volta para si).

Podemos utilizar também uma arrow function (função anonima em seta) para instruir o comportamento diretamente no parametro da função
```ts
const arraySomada = arrayNums.map(num => num * 10)
``` 

### Importante
Note que quando passamos uma função nomeada com a quantidade de retornos da função chamante, não precisamos declarar seus parametros, pois, a linguagem automaticamente realiza isso para nós.

Ou seja, se a função que será usada como callback pede um parametro, e o a função chamante retorna um parametros, a assinatura dar-se-á da seguinte forma `const exemplo = funcaoChamante(funcaoCallBack)`, caso a função callback tenha a seguinte assinatura `function funcaoCallBack(parametro)`.

Mas, podemos também utilizar função anonima / função lambda / arrow function para instruir diretamente o comportamento no parametro pedido pela função. Ambos os casos são interpretados como função callback.

> Para o JavaScript, qualquer função que seja chamada como argumento de outra é considerada uma função callback, não apenas em caso de métodos. Você pode ver outros exemplos no [MDN](https://developer.mozilla.org/pt-BR/docs/Glossary/Callback_function).

# <span style="color: #87BBA2">03. Avançando em arrays</span>

## FILTRANDO ELEMENTOS

Utilize o método `.filter` de uma `Arrays`
- Filter aceita função callback de 2 parametros, sendo o primeiro parametro o elemento interno da Array e o segundo parâmetro o seu índice.
- Logo, podemos realizar `Elementos.filter((elemento, indice) => return Operação_Lógica);`

```ts
const alunos = ['Ana', 'Marcos', 'Maria', 'Mauro'];
const medias = [7, 4.5, 8, 7.5];

const tamanhoNome = alunos
  .filter((aluno) => return aluno.lenght < 4);

console.log(tamanhoNome) // retornará todos os alunos que possuem menos do que 4 letras em seu nome, no caso, Ana

const reprovados =  alunos
  .filter((aluno, indice) => return medias[indice] < 7);

console.log(reprovados) // retorna a lista daqueles que tiraram menos do que 7, uma vez que o indice de alunos é pareado com o indice de notas. Ou seja, aluno do indice 1 corresponde a nota do indice 1.
```

**IMPORTANTE**: Os parametros sempre seguem em ordem, ou seja, se uma função pede (elemento, indice), o primeiro parametro SEMPRE será o elementos e o segundo SEMPRE será indice. Se você não passar o primeiro, o segundo parâmetro passa a ser o primeiro.

Para passar nada ao primeiro parametro e acessar apenas o segundo parametro em diante, é uma convenção utilizarmos `_` no parametro, como `(_, indice)` para capturarmos APENAS o indice e não o elemento. Se fizessemos `(indice)`, nóe estariamos passando um "alias" chamado "indice" no campo que se espera um elemento.

## SOMANDO COM REDUCE
Um laço especial do JavaScript que faz tarefas especificas. Neste caso, o método reduce() executa uma função reducer (fornecida por você) para cada elemento do array, resultando num único valor de retorno.

O valor de retorno da sua função reducer é atribuída ao acumulador. O acumulador, com seu valor atualizado, é repassado para cada iteração subsequente pelo array, que por fim, se tornará o valor resultante, único, final.

**Ou seja, reduz todos os elementos de uma Array a um elemento só. **

```ts
const salaJS = [7, 8, 8, 7, 10, 6.5, 4, 10, 7];
const salaJava = [6, 5, 8, 9, 5, 6];
const salaPython = [7, 3.5, 8, 9.5];

function calculaMedia(listaDeNotas) {

  const somaDasNotas = listaDeNotas.reduce((acumulador, nota) => 
    acumular + nota,
    0
  );

  const media = somaDasNotas / listaDeNotas.length;
  return media;
}

console.log(calculaMedia(salaJs)); // Teremos o retorno da média
console.log(calculaMedia(salaJava)); // Teremos o retorno da média
console.log(calculaMedia(salaPython)); // Teremos o retorno da média

```
### A sintaxe do Reduce
**Sintaxe de Reduce**
- Primeiro parametro: Callback Function para acumulo e iteração
- Segundo parametro: Definição do valor inicial

**Sintaxe da callback no reduce**
- Primeiro parametro: acumulador
- Segundo parametro: elemento que está sendo iterado
- Retorna o valor acumulado da interação

### Outras formas de escrever a mesma operação
A apresentada acima é a mais usual, mas outras formas funcionam:
```ts
// Function explicita e com bloco de código e return
const soma = numeros.reduce(function (acc, atual) {
 return atual + acc
}, 0)

// Callback Function externa
function operacaoNumerica(acc, atual) {
 return atual + acc
}
 
const soma = numeros.reduce(operacaoNumerica, 0)
```

## CLONANDO ARRAYS
Existem duas formas de se atribuir valores a uma variável:
- Atribuição por valor
  - Geralmente ocorre com os valores primitivos
- Atribuição por referencia
  - Normalmente visto com Arrays

### Atribuição por valor
Atribuição por valor é quando atribuimos a uma variável o valor do que foi instruído, e não o seu endereço na memória.
```ts
// Atribui valor 10 à variavel Nota
let nota = 10;
// Atribui o valor de Nota à novaNota
let novaNota = nota;
// Alterando valor de nota
nota = 9;

console.log(novaNota); // Retorno é 10
```

### Atribuição por referencia
Atribuição por referencia é quando atribuimos o endereço da memória a uma variável, ou seja, referenciamos àquele endereço. Logo, se reatribuirmos este valor a outra variável, estaremos apontando ao mesmo endereço de memória e, ao realizar uma ação em uma destas variáveis, afetaremos a outra por estarem apontando ao mesmo endereço.

```ts
// Referenciando uma lista à notas
const notas = [7, 7, 8, 9];
// Referenciando a lista de notas à novaListaNotas
const novaListaNotas = notas;
// Incluindo o valor 10 à lista novaListaNOtas
novaListaNotas.push(10);

// O retorno será o mesmo entre as duas variáveis
console.log(notas);
console.log(novaListaNotas);
```

### Clonando arrays com spread operator
Este operador "abre" o array e espalha seu conteúdo. É como se abrisse uma caixa e retira-se o seu conteúdo ao invés de referenciar a localização desta caixa.

```ts
// Referenciando uma lista à notas
const notas = [7, 7, 8, 9];
// Referenciando uma nova lista contendo os valores internos da array de notas + o item 10. A partir de agora, novaListaNotas referencia uma nova lista
const novaListaNotas = [...notas, 10];

console.log(notas); // [7, 7, 8, 9];
console.log(novaListaNotas); // [7, 7, 8, 9, 10];
```

## MAIS SOBRE VALOR E REFERENCIA

No vídeo anterior, você viu como clonar um array de forma apropriada no JavaScript. Atribuir diretamente um array para outro com o sinal = faz com o que o JavaScript entenda o novo array como uma referência ao anterior.

Para evitar esse comportamento, devemos criar um array totalmente novo, com a ajuda do spread operator ... (ou operador de espalhamento).

Porém, esse comportamento não acontece com strings, números e booleanos, que são tipos primitivos do JavaScript.

Considere o seguinte código:
```ts
let num1 = 10;
let num2 = num1;

num2 += 5;
num1 += 1;

console.log(`Num1 é ${num1}. Num2 é ${num2}`);
```

Ao executar o código, teremos a frase “Num1 é 11. Num2 é 15”. Ou seja, com o código let num2 = num1, o JavaScript entende que queremos criar uma cópia de num1, e cria uma nova variável, com seu próprio espaço na memória guardando seu valor. Então, ao modificar uma das variáveis, a outra não é alterada.

Esse comportamento de copiar um valor primitivo, o atribuindo a uma nova variável, é chamado de atribuição por valor.

### Comportamento em funções
O mesmo comportamento ocorre quando trabalhamos com parâmetros de funções. Veja o seguinte exemplo:
```ts
let numeroOriginal = 10;

function alteraNumero(numero) {
  numero = 50;

  console.log(`numero do parâmetro é ${numero}. numeroOriginal é ${numeroOriginal}`);
}

alteraNumero(numeroOriginal);
```

Executando o código, teremos a frase “numero do parâmetro é 50. numeroOriginal é 10”. Ao chamar a função passando numeroOriginal como parâmetro, foi feita uma cópia de seu valor para ser utilizada como o parâmetro numero dentro da função. Dessa forma, mesmo alterando numero dentro da função, numeroOriginal permanece inalterado.

Mas como você viu, com arrays não funciona bem dessa forma, afinal, eles não são um tipo primitivo. Considere o exemplo utilizado no vídeo passado:
```ts
const notas = [7, 7, 8, 9];

const novasNotas = notas;

novasNotas.push(10);

console.log(`As novas notas são ${novasNotas}`);
console.log(`As notas originais são ${notas}`);
```

A partir do código const novasNotas = notas, o JavaScript entende que novasNotas e notas passam a ser o mesmo array, e agora eles apontam para o mesmo espaço na memória. Como estamos lidando com dados mais complexos, o JavaScript faz isso por padrão para otimizar memória e performance, em vez de realizar uma cópia do array em toda nova atribuição.

Uma atribuição de um array é chamada de atribuição por referência, pois nela é passada a referência do array em si, e não uma cópia de seu valor.

O mesmo comportamento ocorre quando arrays são passados como parâmetro de funções. Veja o código abaixo:
```ts
const arrayOriginal = [7, 7, 8, 9];

function alteraArray(array) {
  array.push(10);

  console.log(`array do parâmetro é ${array}`);
  console.log(`arrayOriginal é ${arrayOriginal}`);
}

alteraArray(arrayOriginal);
```

Executando o código, teremos essa saída:
```ts
array do parâmetro é 7,7,8,9,10
arrayOriginal é 7,7,8,9,10
```

Após passar arrayOriginal como parâmetro de alteraArray, o utilizamos como o parâmetro array. O código array.push(10) alterou ambos os arrays, assim como o que houve no exemplo que fizemos a atribuição. Ou seja, novamente, foi passada a referência do array em si, e não uma cópia dele.

De forma análoga à solução do vídeo, caso queiramos passar uma cópia do array e não sua referência, trocamos o código alteraArray(arrayOriginal) por alteraArray([...arrayOriginal]). Assim, a saída será:
```ts
array do parâmetro é 7,7,8,9,10
arrayOriginal é 7,7,8,9
```

## TEMOVENDO DUPLICATAS
Caso fossemos fazer isso com for, poderiamos, por exemplo, comparar os valores da Array e se for diferente atribui a lista, e se for igual "desencana". Mas, utilizaremos soluções já construidas no JavaScript, como o `new Set()`.

```ts
const nomes = ["Ana", "Clara", "Maria", "Maria", "João", "João", "João"];

const nomesAtualizados = new Set(nomes);

console.log(nomesAtualizados);
```

### Sobre Set
O `Set` é um conjunto que armazena valores únicos. Costuma-se dizer que **Set é um array-like**, mas **não necessariamente é uma array**, ou seja, métodos de array com o Set não funcionará (como reduce, push, pop).

### Transformando Set em Array
Utilizando operador de espalhamento, podemos fazer essa conversão.

```ts
const nomes = ["Ana", "Clara", "Maria", "Maria", "João", "João", "João"];

const nomesAtualizados = new Set(nomes);
const listaNomesAtualizados = [...nomesAtualizados];

// Realizando todas as operações em um mesmo processo
const listaNomesAtualizados = [... new Set(nomes)]
```

## OUTRA FORMA DE UTILIZAR REDUCE
Interessante usar reduce para trabalhar com valores acumulados, não somente para realizar mappers

```ts
const numeros = [1, 2, 3, 4, 5];

const soma = numeros.reduce((acumulador, valorAtual) => {
    return acumulador + valorAtual;
}, 0);

console.log("A soma dos números é:", soma);
```