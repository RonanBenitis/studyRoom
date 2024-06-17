let frutas = [];
let laticinios = [];
let congelados = [];
let doces = [];

let resp = prompt('Deseja adicionar algum item na sua lista de compras? (s/n)')
while (resp != 'n') {
    let item = prompt('Qual item deseja inserir?');
    let indexCategoria = prompt(`Qual caregoria o item se refere? (insira o número do indice): \n${listaCategorias()}`)
    let categoria = getCategoria(indexCategoria);
    acrescentaCategoria(categoria, item);
    resp = prompt('Deseja incluir mais algum item na sua lista de compras? (s/n)')
}

alert(printListaCompras());

function printListaCompras() {
    return `Lista de Compras:
        Frutas: ${frutas}
        Laticínios: ${laticinios}
        Congelados: ${congelados}
        Doces: ${doces}`
}

function getItensCategoria(categoria) {
    return categoria.forEach(item => `${item}`);
}

function acrescentaCategoria(categoria, item) {
    categoria.push(item);
    alert(`Item ${item} inserido com sucesso!`);
}

function listaCategorias() {
    return '1 - Frutas \n2 - Laticínios;\n3 - Congelados;\n4 - Doces;';
}

function getCategoria(num) {
    switch (num) {
        case '1':
            return frutas;
            break;
        case '2':
            return laticinios;
            break;
        case '3':
            return congelados;
            break;
        case '4':
            return doces;
            break;
        default:
            alert('Numero inválido');
    }
}