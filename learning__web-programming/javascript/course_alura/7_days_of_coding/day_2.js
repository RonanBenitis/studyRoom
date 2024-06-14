let nome = prompt('Qual seu nome?');
let idade = prompt('Qual é sua idade?');
let linguagem = prompt('Qual linguagem de programação você está estudando?');

alert(`Olá ${nome}, você tem ${idade} anos e já está aprendendendo ${linguagem}!`);

const resposta = prompt(`Você gosta de estudar ${linguagem}? Responda com número 1 para SIM ou 2 para NÃO.`);

if (resposta == 1) {
    alert('Muito bom! Continue estudando e você terá muito sucesso.');
} else if (resposta == 2) {
    alert('Ahh que pena... Já tentou aprender outras linguagens?')
} else {
    alert('Opçao invalida');
}