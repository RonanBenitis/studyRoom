let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1', 'Jogo do Número Secreto');
exibirTextoNaTela('p', 'Escolha um número entre 1 a 10');

function verificarChute() {
    // Para capturar o valor da primeira tag input
    let chute = document.querySelector('input').value;
    if (chute == numeroSecreto) {
        exibirTextoNaTela('h1', 'Acertou!');
        // Operador ternário
        let textoTentativas = tentativas > 1? 'tentativas' : 'tentativa';
        // Transpor Template String para String
        let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${textoTentativas}`;
        /*
        Não passaremos uma template string direto no exibirTextoNaTela,
        pois, o HTML espera uma String e não uma Template String.
        Por isso, criamos o mensagemTentativa.
        */
        exibirTextoNaTela('p', mensagemTentativas);
    } else {
        if (chute > numeroSecreto){
            exibirTextoNaTela('p', 'O número secreto é menor do que o chute');
        } else {
            exibirTextoNaTela('p', 'O número secreto é maior que o chute');
        }
        tentativas++;
    }
}

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1);
}