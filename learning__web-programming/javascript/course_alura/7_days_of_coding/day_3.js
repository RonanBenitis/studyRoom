let nome = prompt('Qual seu nome?');

let resposta = prompt(`Olá ${nome}! Você gostaria de seguir para a área de Front-End ou Back-End?`);

if (resposta.toLowerCase().includes('front')) {
    resposta = prompt(`Você gostaria de aprender React ou Vue?`);
} else if (resposta.toLowerCase().includes('back')) {
    resposta = prompt(`Você gostaria de aprender C# ou Java?`);
} else {
    alert('Opção invalida');
}

resposta = prompt(`Você gostaria de seguir se especializando na área escolhia ou seguir se desenvolvendo para se tornar Fullstack`);
if (resposta.toLowerCase().includes('especia')) {
    resposta = alert(`Você escolheu seguir se especializando na área escolhida!`);
} else if (resposta.toLowerCase().includes('full')) {
    resposta = alert(`Você escolheu se desenvolver para se tornar Fullstack!`);
} else {
    alert('Opção invalida');
}
resposta = ".";
while (resposta != null) {
    resposta = prompt('Quais tecnologias você gostaria de se especializar? Insira uma tecnologia, para inserir mais clique OK, para encerrar clique CANCELAR');
    alert(`Você inseriu ${resposta}!`);
}