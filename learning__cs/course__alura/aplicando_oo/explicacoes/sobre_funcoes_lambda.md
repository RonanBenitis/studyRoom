No C#, lambdas são funções anônimas que podem ser usadas para criar expressões ou blocos de código compactos e concisos. Eles são especialmente úteis quando se trata de trabalhar com coleções de dados, realizar operações em uma sequência de elementos ou lidar com delegados.

Vamos começar com um exemplo simples de um código sem lambda. Suponha que você tenha uma lista de números inteiros e deseje filtrar apenas os números pares. Aqui está um exemplo sem o uso de lambda:

```CS
List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

List<int> numerosPares = numeros.FindAll(BuscarNumerosQueSaoPares);

bool BuscarNumerosQueSaoPares(int numero)
{
    return numero % 2 == 0;
}

foreach (int numero in numerosPares)
{
    Console.WriteLine(numero);
}
```

Ao executar esse programa, o resultado será:
```
2
4
6
8
10
```

Neste exemplo, definimos um método chamado BuscarNumerosQueSaoPares, que recebe um número inteiro e retorna um valor booleano indicando se o número é par. Em seguida, usamos o método FindAll da classe List<T> para filtrar os números da lista com base nessa condição e exibimos os valores no console.

## Como seria esse código com funções lambdas?
Lembrando que a estrutura de código de uma função lambda no C# segue um formato geral. Aqui está a estrutura básica de uma função lambda:
```
(parametros) => expressao
```

**Parâmetros**: É uma lista opcional de parâmetros, separados por vírgulas, que especifica as entradas da função lambda. Cada parâmetro pode ser tipado explicitamente ou pode ser inferido pelo compilador.

**Operador** `=>`: É o operador de seta (=>), que separa a lista de parâmetros da expressão lambda. Ele indica que os parâmetros estão sendo mapeados para a expressão ou bloco de código seguinte.

**Expressão ou bloco de código**: É a expressão ou o bloco de código que define a lógica da função lambda. Pode ser uma única expressão ou um bloco de código delimitado por chaves ({}). Se a função lambda contiver um único comando, a expressão será automaticamente retornada. Caso contrário, você pode usar a palavra-chave return para retornar explicitamente um valor.

## Mão nas teclas
Vamos iniciar substituindo a função `BuscarNumerosQueSaoPares` por uma função anônima que tem a mesma finalidade:
```CS
List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
List<int> numerosPares = numeros.FindAll(numero => numero % 2 == 0);
```
A expressão lambda especifica um parâmetro numero seguido por uma seta (=>) e uma expressão que retorna um valor booleano. A função FindAll utiliza essa expressão lambda como critério para filtrar os números da lista.

Em seguida, podemos usar uma função lambda na exibição dos números pares:
```
numerosPares.ForEach(numero => Console.WriteLine(numero));
```

Segue o código completo:
```CS
List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

List<int> numerosPares = numeros.FindAll(numero => numero % 2 == 0);
numerosPares.ForEach(numero => Console.WriteLine(numero));
```

## Algumas vantagens das lambdas em relação ao código sem lambda
**Concisão**: As lambdas permitem escrever código de forma mais concisa, eliminando a necessidade de definir métodos separados para funções simples.

**Legibilidade**: As lambdas são mais fáceis de ler e entender, especialmente quando o critério de filtragem ou a lógica do código é curto e direto.

**Flexibilidade**: As lambdas podem ser usadas em várias situações, como filtrar, ordenar, mapear ou reduzir coleções de dados. Elas permitem que você especifique a lógica do código diretamente no local onde é necessário, sem a necessidade de criar métodos adicionais.

**Encerramento de escopo**: As lambdas têm acesso às variáveis do escopo em que são definidas, o que permite que você capture e utilize valores externos dentro da expressão lambda. Isso pode ser útil em casos onde você precisa fazer referência a variáveis externas dentro de um loop, por exemplo.

> Em resumo, lambdas no C# são funções anônimas que fornecem uma sintaxe concisa para escrever blocos de código em situações onde a criação de um método separado seria inconveniente ou desnecessário. Elas oferecem vantagens em termos de concisão, legibilidade, flexibilidade e encerramento de escopo.

## Quando não é recomendado o uso de código lambda?
**Complexidade excessiva**: Se a lógica da expressão lambda se tornar muito complexa ou difícil de entender, é preferível usar métodos e blocos de código separados para manter a clareza e legibilidade do código.

**Reutilização de código**: Se você precisa reutilizar a lógica em várias partes do seu código, é mais adequado criar um método separado em vez de usar uma função lambda repetidamente. Isso promove a reutilização do código e torna mais fácil a manutenção.

**Aumento da complexidade do código**: Em alguns casos, o uso excessivo de funções lambda pode tornar o código mais difícil de entender e dar manutenção, especialmente quando as expressões lambdas são aninhadas. Nesses casos, pode ser melhor dividir o código em partes menores e mais legíveis.

> Embora as funções lambda sejam uma ferramenta poderosa e muito usada no mundo de desenvolvimento C#, há situações em que é mais apropriado evitar o seu uso.