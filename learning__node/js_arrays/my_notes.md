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