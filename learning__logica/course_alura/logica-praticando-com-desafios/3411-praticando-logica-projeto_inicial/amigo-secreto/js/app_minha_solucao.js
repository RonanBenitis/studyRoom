let friendsList = [];

function adicionar() {
    let nomeEl = document.getElementById('nome-amigo');
    let friendsEl = document.getElementById('lista-amigos');
    
    // Valida se o campo está vazio
    if (nomeEl.value == '') {
        alert('Campo vazio, por favor, acrescente um nome!');
        return;
    }

    if (friendsList.includes(nomeEl.value)) {
        alert('Este amigo já se encontra na lista.')
        return;
    }

    // Acrescenta nome no display e incrementa
    friendsEl.textContent = friendsEl.textContent == '' ? `${nomeEl.value}`
            : `${friendsEl.textContent}, ${nomeEl.value}`;

    // Acrescenta amigos na lista
    friendsList.push(nomeEl.value);

    // Reseta campo nome
    nomeEl.value = ''; 
}

function sortear() {
    let listA = [];
    let listB = [];

    // Copia friendsList para as listas
    for (let i = 0; i < friendsList.length; i++) {
        listA[i] = friendsList[i];
        listB[i] = friendsList[i];
    }

    let drawEl = document.getElementById('lista-sorteio');
    drawEl.innerHTML = '';
    let max = listA.length;

    if (max <= 1) {
        alert('Operação cancelada! Precisam ter 2 ou mais integrantes.');
        return;
    }

    for (let i = 0; i < max; i++) {
        let elementA, elementB;

        // loopa enquanto elemento não estiver na lista
        do {
            elementA = listA[getRandomInt(max)];
        } while(!listA.includes(elementA));

        // Tira elemento A da lista A
        listA.splice(listA.indexOf(elementA), 1);
        
        // loopa enquanto elemento não estiver na lista
        // Ou enquanto element B for igual a element A
        do {
            elementB = listB[getRandomInt(max)];
        } while(!listB.includes(elementB) || elementB == elementA);

        // Tira elemento B da lista B
        listB.splice(listB.indexOf(elementB), 1);

        drawEl.innerHTML += `${elementA} → ${elementB} <br>`;
    }
}

function getRandomInt(numIntegrantes) {
    return parseInt(Math.random() * numIntegrantes);
}

function reiniciar() {
    document.getElementById('lista-amigos').textContent = '';
    document.getElementById('lista-sorteio').textContent = '';
    friendsList = [];
}