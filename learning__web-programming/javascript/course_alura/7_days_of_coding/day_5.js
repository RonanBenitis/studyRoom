let frutas = [];
let laticinios = [];
let congelados = [];
let doces = [];
let categorias = [frutas, laticinios, congelados, doces]

let resp = prompt('Deseja adicionar algum item na sua lista de compras? (s/n)');
validaResp(resp);

while (resp != 'n') {
    let item = prompt('Escreva o item que deseja inserir');
    let indexCategoria = prompt(`Qual categoria o item se refere? (insira o número do indice): \n${listaCategorias()}`)
    pushCategoria(indexCategoria, item);
    resp = prompt('Deseja incluir mais algum item na sua lista de compras? (s/n)')
    validaResp(resp);
}

alert(printListaCompras());

function validaResp(resp) {
    while (resp != 's' && resp != 'n') {
        alert('Responsta invalida');
        resp = prompt('Deseja adicionar algum item na sua lista de compras? (s/n)');
    }
}

function printListaCompras() {
    return `Lista de Compras:
        Frutas: ${frutas}
        Laticínios: ${laticinios}
        Congelados: ${congelados}
        Doces: ${doces}`
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