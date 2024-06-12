// Link do exercicio: https://codepen.io/vanessametonini/pen/eYEVEqR

// Resposta

// Capturando a lista de teclas
const listaDeTeclas = document.querySelectorAll('input[type=button]');
// Capturando o input de "Digite seu telefone"
const inputTel = document.querySelector('input[type=tel]');

for (let i = 0; i < listaDeTeclas.length; i++) {
    const tecla = listaDeTeclas[i];

    /* 
    A lógica da função é: Quando clicar na tecla (que corresponde ao
    indice de listaDeTeclas), faça com que o valor de inputTel seja
    a concatenação do valor anterior de inputTel com o valor da
    tecla clicada. Aconteceu a concatenação pois o número, neste
    caso, é uma String. Se fosse int ou decimal, ocorreria uma
    soma
    */
    tecla.onclick = function () {
        inputTel.value = inputTel.value + tecla.value;
    };
};
