let jogosAlugados;

function alterarStatus(id) {
    /*
    Detalhe interessante: ao utilizar getElementByClass() após
    o getElementById, não consegui pegar todo o elemento como em
    querySelector.
    Consegui utilizar o classList apenas quando usei o querySelector
    netes caso.
    */
    let anchorAluga = document.getElementById(`game-${id}`)
                      .querySelector('.dashboard__item__button');
    let itemImg = document.getElementById(`game-${id}`)
                  .querySelector('.dashboard__item__img');
    let nomeJogo = document.getElementById(`game-${id}`)
                   .querySelector('.dashboard__item__name').innerText;
    let operacao = anchorAluga.innerText == 'Alugar' ? 'alugar' : 'devolver';

    if(confirm(`Você gostaria de ${operacao} o jogo ${nomeJogo}?`)) {
        alternaClasse(anchorAluga, 'dashboard__item__button--return');
        alternaClasse(itemImg, 'dashboard__item__img--rented');

        if (anchorAluga.innerText == 'Alugar') {
            anchorAluga.innerText = 'Devolver';
        } else {
            anchorAluga.innerText = 'Alugar';
        }
    } else {
        alert('Operação cancelada');
    }
}

function alternaClasse(elemento, classe) {
    if (elemento.classList.contains(classe)) {
        elemento.classList.remove(classe);
    } else {
        elemento.classList.add(classe);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    jogosAlugados = document.querySelectorAll('.dashboard__item__img--rented')
                    .length;
    console.log(`Quantidade de jogos alugados: ${jogosAlugados}`);
});

const ANCHORS = document.querySelectorAll('.dashboard__item__button');

ANCHORS.forEach(anchor => anchor.addEventListener('click', function() {
    jogosAlugados = document.querySelectorAll('.dashboard__item__img--rented')
                    .length;
    console.log(`Quantidade de jogos alugados: ${jogosAlugados}`);
}));