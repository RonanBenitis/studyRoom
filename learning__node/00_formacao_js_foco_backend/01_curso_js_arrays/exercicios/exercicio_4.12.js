// >>> DADOS
const nomesTurmaA = [
    'João Silva',
    'Maria Santos',
    'Pedro Almeida'
];
  
const nomesTurmaB = [
    'Carlos Oliveira',
    'Ana Souza',
    'Lucas Fernandes'
];

const numeros = [6, 9, 12, 15, 18, 21];

// >>> 1 - Utilize o método forEach para imprimir cada elemento de um array juntamente com seu índice.
nomesTurmaA.forEach((nome) => {
    console.log(`${nomesTurmaA.indexOf(nome)} - ${nome}`); 
});

// >>> 2 - Crie uma função chamada executaOperacaoEmArray que recebe dois parâmetros: um array e uma função de callback que executa alguma operação matemática. Essa função deve iterar por cada elemento do array e aplicar a função de callback em cada um dos elementos, imprimindo o resultado da operação no console.
// Construindo função que pede callback
const executaOperacaoEmArray = (listaNumeros, operacaoMatematica) => {
    return listaNumeros.map(operacaoMatematica);
}

// Chamando função com Arrow Function no callback
console.log(executaOperacaoEmArray(numeros, (num) => num * 10))

// >>> 3 - Você recebeu um array numeros contendo valores numéricos. Crie um programa que verifique se um número específico está presente nesse array. Se estiver, o programa deve retornar a posição (índice) desse número. Caso contrário, se o número não estiver presente, o programa deve retornar "-1".
const numeroNoArrayExiste = (numero, listaNumeros) => {
    return listaNumeros.indexOf(numero);
}

console.log(`${numeroNoArrayExiste(1, numeros)}, ${numeroNoArrayExiste(6, numeros)}`);