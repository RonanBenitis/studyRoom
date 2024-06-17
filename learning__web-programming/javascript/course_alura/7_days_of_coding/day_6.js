let frutas = [];
let laticinios = [];
let congelados = [];
let doces = [];
let categorias = [frutas, laticinios, congelados, doces]

let resp = perguntaInicial();

// *****   AREA INICIAL   *****
while (resp != 0) {
    if (resp == 1) {
        alert('***   Opção escolhida: Adicionar item   ***');
        adicionaItem();
        alert('***   Item adicionado com sucesso!   ***');
    } else if (resp == 2) {
        alert('***   Opção escolhida: Remover item   ***');
        if (verificaCategoriasVazias() == true) {
            alert('A lista de compras está vazia');
        } else {
            printListaCompras();
            removeItem();
        }
    }
    resp = perguntaInicial();
}

if (verificaCategoriasVazias() == true) {
    alert('A lista de compras está vazia');
} else {
    printListaCompras();
}

// *****   AREA DE FUNÇÔES   *****
function adicionaItem(){
    let item = prompt('Escreva o item que deseja inserir');
    let indexCategoria = prompt(`Qual categoria o item se refere? (insira o número do indice): \n${listaCategorias()}`)
    pushCategoria(indexCategoria, item);
}

function removeItem(){
    let item = prompt('Escreve o item que deseja excluir');
    let exclusoes = 0;
    for (i = 0; i < categorias.length; i++) {
        if (categorias[i].includes(item)) {
            let index = categorias[i].indexOf(item);
            categorias[i].splice(index, 1);
            alert(`***   Item ${item} excluído com sucesso!   ***`);
            exclusoes++;
        }
    }
    if (exclusoes == 0) {
        alert(`Item ${item} não foi encontrado na lista de compras`);
    } else {
        alert(`Foram feitas ${exclusoes} exclusões.`);
    }
}

function perguntaInicial() {
    let respostaInicial = prompt('Digite a opção desejada:\n1 - Adicionar item\n2 - Remover item\n0 - Encerrar operação');
    while (respostaInicial != 1 && respostaInicial != 2 && respostaInicial != 0) {
        alert('Resposta invalida');
        respostaInicial = prompt('Digite a opção desejada:\n1 - Adicionar item\n2 - Remover item\n0 - Encerrar operação');
    }
    return respostaInicial;
}

function printListaCompras() {
    alert(`Lista de Compras:
        Frutas: ${frutas}
        Laticínios: ${laticinios}
        Congelados: ${congelados}
        Doces: ${doces}`)
}

function listaCategorias() {
    return '0 - Frutas \n1 - Laticínios;\n2 - Congelados;\n3 - Doces;';
}

function pushCategoria(index, item) {
    if (index < categorias.length) {
        categorias[index].push(item);
    } else {
        alert('Categoria inexistente');
    }
}

function verificaCategoriasVazias() {
    for (let i = 0; i < categorias.length; i++) {
        if (categorias[i].length > 0) {
            return false;
        }
    }
    return true;
}