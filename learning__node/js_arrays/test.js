const listaEstudantes = ['João', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Leo'];
const outraArray = ['1', '2', '3']
listaEstudantes.splice(3, 5, outraArray);
console.log(listaEstudantes) // [ 'João', 'Ana', 'Caio', ['1', '2', '3'] ]