Não deixe de praticar, executando os exemplos desta atividade em seu computador!

Vamos revisar os métodos do JavaScript para conversão de strings e números e também conhecer outros que não praticamos em vídeo.

Conversão para números
Number()
Esta função converte qualquer outro tipo de dado em um tipo Number. Caso o valor não possa ser convertido, retornará NaN.

Number("1"); // retorna o número 1 
Number("Alura"); // retorna NaN
Number(undefined); // retorna NaN
Number(null); // retorna 0
Copiar código
Number.parseInt() e Number.parseFloat()
Ambos funcionam de forma parecida, porém, 'parseIntvai tentar converter o valor em um número inteiro eparseFloat`, em um número de ponto flutuante.

parseInt(‘4’); // retorna o número 4
parseInt(‘4.5’); // retorna o número 4

parseFloat(‘4’); // retorna o número 4
parseFloat(‘4.5’); // retorna o número 4.5
parseFloat(‘4.5abc’); // retorna o número 4.5
Copiar código
Uma outra forma de fazer a coerção de tipos (quando o JavaScript tenta “forçar” de forma implícita a conversão de um valor de um tipo para outro) é utilizando o operador unário +. Por exemplo:

+’45’ // retorna o número 45
+true // retorna o número 1

console.log(typeof +’45’); // retorna ‘number’
console.log(typeof +true); // retorna ‘number’
Copiar código
Importante: embora seja prático, o uso do operador + para coerção de tipos não é tão conhecido e sua função no código não fica tão óbvia quanto a das funções. Se for o caso, combine o seu uso junto às outras pessoas que trabalharão no mesmo código.

Qual a diferença?
As funções parseInt() e parseFloat() funcionam de forma similar a Number(), porém convertem apenas strings, enquanto Number() é capaz de converter outros tipos de dados conforme os exemplos acima.

Confira mais usos detalhados de cada um na documentação do MDN:

[number](https://developer.mozilla.org/pt-br/docs/Web/JavaScript/Reference/Global_Objects/Number);
[parseInt](https://developer.mozilla.org/pt-br/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt);
[parseFloat](https://developer.mozilla.org/pt-br/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat);
Conversão para strings
Assim como Number(), o JavaScript também disponibiliza a função global String() quando é necessário converter outros tipos de dado em formato de texto.

String(2); // retorna '2'
String(undefined); // retorna 'undefined'
String(true); // retorna 'true'
Copiar código
É possível utilizar diversos métodos do JavaScript para modificar strings. Confira abaixo alguns dos mais comuns:

[includes](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String/includes)()
Determina se um conjunto de caracteres pode ser encontrado dentro de uma string, retornando true ou false:

'estudando JavaScript'.includes('Java'); // retorna true
Copiar código
É sempre possível passar o valor a ser convertido a partir de uma variável:

const texto = 'estudando JavaScript';
texto.includes('Java'); // retorna true
Copiar código
toLowerCase()
Converte todos os caracteres da string para letras minúsculas.

'POR FAVOR, NÃO GRITE'.toLowerCase(); // retorna 'por favor, não grite'
Copiar código
Assim como no exemplo anterior, a string que será convertida pode estar em uma variável:

const texto = 'POR FAVOR, NÃO GRITE';
texto.toLowerCase(); // retorna 'por favor, não grite'
Copiar código
Da mesma forma que existe um método para transformar textos em minúsculas, também é possível usar texto.toUpperCase() para converter em maiúsculas.

Confira a [lista completa de métodos de string na documentação do MDN.](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/String#m%C3%A9todos)