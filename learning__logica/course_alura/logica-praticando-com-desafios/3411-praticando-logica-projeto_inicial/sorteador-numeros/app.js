let botaoSortear = document.getElementById('btn-sortear')
let botaoReiniciar = document.getElementById('btn-reiniciar');
let resultado = document.getElementById('resultado'); // busca a div
let tagMsgInicial = '<label class="texto__paragrafo">Números sorteados:  nenhum até agora</label>';
// Se eu fosse refatorar o código, declararia globalmente quantidade, deNumero e ateNumero
// e acessaria seus valores pela variavel dentro das funções.

function sortear() {
    let quantidade = parseInt(document.querySelector('#quantidade').value);
    let deNumero = parseInt(document.getElementById('de').value);
    let ateNumero = parseInt(document.getElementById('ate').value);
    let numero;
    let sorteados = [];

    if (deNumero >= ateNumero) {
        alert('Campo "Do número" deve ser inferior ao campo "Até o número"!');
        reiniciar();
        return; // interromper operação
    }

    /*
    Colocou-se o +1 pois precisamos gerar o numero INCLUSIVE o ATÉ
    por exemplo, queremos 2 numeros de 2 a 3. 3 - 2 = 1, mas o resultado
    esperado deveria ser 2, 3, pois queremos incluir o numero ATÉ. Então,
    colocamos +1 garantindo que o retorno será, sim, 2, 3.
    */
    if (quantidade > (ateNumero - deNumero + 1)) {
        alert('A quantidade de números deve ser igual ou maior do que o intervalo dos números inseridos!');
        reiniciar();
        return; // interromper operação
    }

    for (let i = 0; i < quantidade; i++) {
        numero = obterNumeroAleatorioInt(deNumero, ateNumero);

        while (sorteados.includes(numero)) {
            numero = obterNumeroAleatorioInt(deNumero, ateNumero);
        }

        sorteados.push(numero);
    }
    resultado.innerHTML = `<label class="texto__paragrafo" id="resultado-numero-sorteado">Números sorteados: ${sorteados}</label>`

    habilitaBotao(botaoReiniciar);
}

function obterNumeroAleatorioInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function reiniciar() {
    limparCampo();
    desabilitaBotao(botaoReiniciar);
    resultado.innerHTML = tagMsgInicial;
}

function limparCampo() {
    document.querySelector('#quantidade').value = '';
    document.getElementById('de').value = '';
    document.getElementById('ate').value = '';
}

function habilitaBotao(botao) {
    if (botao.classList.contains('container__botao-desabilitado')) {
        botao.classList.remove('container__botao-desabilitado');
        botao.classList.add('container__botao');
    }
}

function desabilitaBotao(botao) {
    if (botao.classList.contains('container__botao')) {
        botao.classList.add('container__botao-desabilitado');
        botao.classList.remove('container__botao');
    }
}