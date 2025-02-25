function comprar() {
    // Quantidade
    let qtdInput = document.getElementById('qtd');
    let qtdInputValue = qtdInput.value;
    // Tipo ingresso
    let opcaoSelect = document.getElementById('tipo-ingresso');
    let nomeTipoIngresso = opcaoSelect.options[opcaoSelect.selectedIndex].text;
    // Estoque
    let estoqueIngressoSpan = document.getElementById(`qtd-${opcaoSelect.value}`);
    let estoqueIngressoContent = parseInt(estoqueIngressoSpan.textContent);


    // Valida se o input não é numero ou está vazio ou é nulo.
    if (isNaN(qtdInputValue) || qtdInputValue == '' || qtdInputValue == null
            || qtdInputValue < 0) {
        alert('Valor invalido! Insira quantidade valida.');
        return;
    }

    /*
    Verifica se a quantidade inserida é menor ou igual ao estoque
    do tipo selecionado.
    */
    if (qtdInputValue <= estoqueIngressoContent) {
        estoqueIngressoSpan.textContent = estoqueIngressoContent - qtdInputValue;
        alert(`Compra de ${qtdInputValue}x ingressos "${nomeTipoIngresso}" realizada com sucesso!`);
    } else if(estoqueIngressoContent == 0) {
        alert(`Os ingressos para "${nomeTipoIngresso}" esgotaram!`);
    } else {
        alert(`Ingresso "${nomeTipoIngresso}" indisponível para a quantidade selecionada!`);
    }
    
    qtdInput.value = '';
}