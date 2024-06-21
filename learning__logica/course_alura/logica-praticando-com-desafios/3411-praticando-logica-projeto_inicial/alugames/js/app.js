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

    alternaClasse(anchorAluga, 'dashboard__item__button--return');
    alternaClasse(itemImg, 'dashboard__item__img--rented');

    if (anchorAluga.innerText == 'Alugar') {
        anchorAluga.innerText = 'Devolver';
    } else {
        anchorAluga.innerText = 'Alugar';
    }

}

function alternaClasse(elemento, classe) {
    if (elemento.classList.contains(classe)) {
        elemento.classList.remove(classe);
    } else {
        elemento.classList.add(classe);
    }
}