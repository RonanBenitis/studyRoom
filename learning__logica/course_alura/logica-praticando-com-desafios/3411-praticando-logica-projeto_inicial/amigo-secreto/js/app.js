let amigos = [];

function adicionar() {
    let amigo = document.getElementById('nome-amigo');

    // Acrescenta o valor de amigo na lista amigos
    amigos.push(amigo.value);

    // Limpa campo
    amigo.value = '';

    atualizarLista();
    atualizarSorteio();
}

function sortear() {
    embaralha(amigos);
    let sorteio = document.getElementById('lista-sorteio');

    for (let i = 0; i < amigos.length; i++) {

        if (i == amigos.length - 1) {
            sorteio.innerHTML = sorteio.innerHTML + amigos[i] + ' --> ' +
                    amigos[0] + '<br>';
        } else {
            sorteio.innerHTML = sorteio.innerHTML + amigos[i] + ' --> ' +
                    amigos[i + 1] + '<br>';
        }
    }
}

function embaralha(lista) {

    for (let indice = lista.length; indice; indice--) {

        const indiceAleatorio = Math.floor(Math.random() * indice);

        // atribuição via destructuring
        [lista[indice - 1], lista[indiceAleatorio]] =
                [lista[indiceAleatorio], lista[indice - 1]];
    }
}

function reiniciar() {
    amigos = [];
    document.getElementById('lista=amigos').textContent = '';
    document.getElementById('lista-sorteio').textContent = '';
}

function atualizarLista() {
    let lista = document.getElementById('lista-amigos');
    lista.innerHTML = '';


    for (let i = 0; i < amigos.length; i++) {
        // Cria um elemento de parágrafo para cada amigo
        let paragrafo = document.createElement('p');
        paragrafo.textContent = amigos[i];
       
        // Adiciona um evento de clique para excluir o amigo
        paragrafo.addEventListener('click', function() {
            excluirAmigo(i);
        });

        // Adiciona o parágrafo à ao elemento HTML de id lista-amigos
        lista.appendChild(paragrafo);
    }
}

function atualizarSorteio() {
    let sorteio = document.getElementById('lista-sorteio');
    sorteio.innerHTML = '';
}

function excluirAmigo(index) {
    // Remove a partir do indice index 1 elemento (index, 1)
    amigos.splice(index, 1);
    atualizarLista();
    atualizarSorteio();
}