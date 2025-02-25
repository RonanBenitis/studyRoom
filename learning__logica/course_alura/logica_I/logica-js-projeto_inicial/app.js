alert('Boas vindas ao jogo do número secreto');
let numeroMaximo = 100;
// Trate variaveis como o envelope que armazena o número secreto
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);
// Imprimir informações no lugar "secreto" dos devs
console.log(`Número secreto: ${numeroSecreto}`);
// Prompt é emite um alerta ao usuário e coleta sua resposta
// Agora, armazenaremos seu retorno na variavel "chute"
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 a ${numeroMaximo}`);
    if (chute == numeroSecreto) {
        break;
    } else {
        if (chute < numeroSecreto) {
            alert(`O número é maior do que ${chute}`);
        } else {
            alert(`O número é menor do que ${chute}`);
        }
        tentativas++;
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso aí! Você descobriu o número secreto! (${numeroSecreto}) com ${tentativas} ${palavraTentativa}`);
