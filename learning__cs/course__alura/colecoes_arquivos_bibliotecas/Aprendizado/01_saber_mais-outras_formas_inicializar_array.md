Como vimos, os arrays, ou vetores, são um agrupamento de elementos que armazenamos em uma sequência, sendo o primeiro elemento do array o índice zero. Normalmente, quando criamos uma estrutura deste tipo, temos que definir sua dimensão, que pode ser única ou multidimensional. Vamos a um exemplo de um array de uma dimensão:

```
int[] numeros = new int[10]; 
```

Podemos ter ainda um array com mais de uma dimensão, como por exemplo:

```
int[,] numeros = new int[3,3];
```

Depois de entender como criar arrays, é importante entender que eles são tipos por referência, daí a palavra reservada new na sua declaração. Mas afinal, quais as formas que temos para iniciar esse tipo de estrutura? Primeiramente temos que lembrar que para manipular os arrays, vamos utilizar seus índices, e que todo array em C# inicia no 0.

Na forma mais básica de se declarar e inicializar um array temos:string[] palavras = new string[10] e para inserir valores recorremos à: palavras[0]="André.". Neste exemplo primeiro é declarado o array e depois inserimos os elementos em cada índice. Mas também podemos declará-lo e iniciá-lo por exemplo:

```
string [] palavras= new string[5] {"André","Jose","Andressa","Neia","Sarah"}`.
```

Podemos também omitir o número de elementos como no exemplo:

```
double[] valores={2.6,9.7,7.5,1.8};
```

Estas são algumas das formas que temos para definir um array usando o C#. Para saber ainda mais vamos deixar aqui o link da documentação oficial da Microsoft Matrizes Guia de Programação em C#.

