Não deixe de praticar com os exemplos desta atividade!

Durante seus estudos você pode ter se deparado com a seguinte estrutura:

const valor = 50;
const texto = valor < 50 ? ‘valor insuficiente’ : ‘valor suficiente’;
console.log(texto); // retorna ‘valor suficiente’
Copiar código
O valor da variável texto representa o que chamamos de operador ternário e sua sintaxe é a seguinte:

//condição ?      caso 'true'    :     caso 'false'
valor < 50 ? 'valor insuficiente' : 'valor suficiente';
Copiar código
O operador ternário tem esse nome pois é o único em JavaScript que utiliza três operandos:

a condição, seguida do sinal ?
o código a ser executado se a condição for true, seguida de :
o código a ser executado se a condição for false.
O operador ternário é normalmente utilizado em substituição ao if…else em que as condições têm apenas uma linha de retorno.

Confira abaixo alguns exemplos de blocos if nos quais é possível utilizar o operador ternário:

let matriculaAtiva = true;

function verificaMatriculaAtiva() {
 if (matriculaAtiva === true) {
   return 'matrícula ativa no sistema';
 } else {
   return 'matrícula não está ativa';
 }
}

console.log(verificaMatriculaAtiva());
// retorna 'matrícula ativa no sistema'
Copiar código
O exemplo acima mostra um if em que os códigos dentro dos blocos {} são compostos por somente uma linha cada, retornando uma string para cada caso.

A mesma lógica, usando o operador ternário:

let matriculaAtiva = true;

function verificaMatriculaAtiva() {
 return matriculaAtiva ? 'matrícula ativa no sistema' : 'matrícula não está ativa';
}

console.log(verificaMatriculaAtiva());
// retorna 'matrícula ativa no sistema'
Copiar código
Agora a função, ao invés de retornos (return) diferentes para if e else, tem apenas um retorno, que é o resultado da condicional feita pelo operador ternário.

Podemos interpretar a linha do return em português, da seguinte forma: “A matrícula está ativa? Em caso positivo (true), retorne o texto ’matrícula ativa no sistema’. Em caso negativo (false), retorne o texto ’matrícula não está ativa’.

Observe que o sinal ? separa a condição, enquanto o sinal : separa os casos true e false.

Notou que, em vez de matriculaAtiva === true, escrevemos apenas matriculaAtiva na condição? Nesses casos, quando a condição avalia se algo é “igual a true”, podemos suprimir a parte === true. A regra do JavaScript de valores truthy e falsy também se aplica aqui!

Vamos praticar com mais um exemplo:

let idadeEstudante = 16;
let precisaDeAutorizacao;

if (idadeEstudante < 18) {
 precisaDeAutorizacao = true;
} else {
 precisaDeAutorizacao = false;
}

console.log(precisaDeAutorizacao);
Copiar código
Mantendo o mesmo fluxo com operador ternário:

let idadeEstudante = 16;
const precisaDeAutorizacao = idadeEstudante < 18 ? true : false;
console.log(precisaDeAutorizacao); // true
Copiar código
Dessa forma o operador ternário substituiu todas as linhas do if…else, retornando true ou false conforme o caso e salvando o valor direto na variável precisaDeAutorizacao.

O operador ternário deixa o código bem enxuto, mas pode dificultar a leitura e a compreensão caso as condições fiquem muito “compridas”. Analise caso a caso e quebre o código em um if…else caso tenha que executar lógicas mais complexas.