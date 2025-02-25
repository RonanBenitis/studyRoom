let produtoElement = document.getElementById('produto');
let qtdElement = document.getElementById('quantidade');
let valorTotalElement = document.getElementById('valor-total');
let listaCarrinhoInterno = document.getElementById('lista-produtos')
        .querySelector('.carrinho__produtos__produto');
        
function adicionar() {
    // Colocado aqui pois o valor deverá ser atualizado a cada click
    let nomeProduto = produtoElement.value.split(' -')[0];
    let valorProduto = produtoElement.value.split('R$')[1];
    let valorTotalProd = valorProduto * qtdElement.value;
    let valorTotalAnterior = parseInt(valorTotalElement.innerText.split('R$')[1]);

    // Verificar se o produto selecionado é válido, se fosse necessario
    if (!produto || produto.trim() === "") {
        alert("Selecione um produto válido.");
        return;
    }

    // Valida se quantidade
    if (isNaN(qtdElement.value) || qtdElement.value <= 0) {
        alert("Insira uma quantidade válida.");
        return; // Sai da função
    }

    // Valida se já existe item no carrinho para pular linha corretamente
    if (listaCarrinhoInterno.innerHTML == '') {
        listaCarrinhoInterno.innerHTML = listaCarrinhoInterno.innerHTML + `<br>` +
                `\n<span class="texto-azul">${qtdElement.value}x</span> ${nomeProduto} <span class="texto-azul">R$${valorTotalProd}</span>`;
    } else {  
        listaCarrinhoInterno.innerHTML = listaCarrinhoInterno.innerHTML + `<br>` +
                `\n<span class="texto-azul">${qtdElement.value}x</span> ${nomeProduto} <span class="texto-azul">R$${valorTotalProd}</span>`;
    }

    qtdElement.value = '';
    valorTotalElement.innerText = `R$${valorTotalAnterior + valorTotalProd}`;
}

function limpar() {
    listaCarrinhoInterno.innerHTML = '';
    valorTotalElement.innerText = `R$0`
}