// EXERCICIO 01
const biblioteca = [
    { id: 1, titulo: "O Senhor dos Anéis", autor: "J.R.R. Tolkien", anoPublicacao: 1954 },
    { id: 2, titulo: "Dom Quixote", autor: "Miguel de Cervantes", anoPublicacao: 1605 },
    { id: 3, titulo: "1984", autor: "George Orwell", anoPublicacao: 1949 }
]

const enconstrarLivroPorId = (id) => {
    return biblioteca.find((livro) => livro.id === id)
        ?? 'O livro não foi encontrado';
}

const findValue = (list, key, value) => {
    return list.find((item) => item[key] === value)
        ?? 'O livro não foi encontrado';
}

console.log(enconstrarLivroPorId(1));
console.log(findValue(biblioteca, 'id', 1));
console.log(findValue(biblioteca, 'id', 999));

// EXERCICIO 02
const catalogoFilmes = [
    { id: 1, titulo: "Matrix", diretor: "Lana Wachowski", anoLancamento: 1999 },
    { id: 2, titulo: "Jurassic Park", diretor: "Steven Spielberg", anoLancamento: 1993 },
    { id: 3, titulo: "Inception", diretor: "Christopher Nolan", anoLancamento: 2010 }
]

const filtrarFilmesPorAno = (anoLancamento) => {
    return catalogoFilmes.filter((filme) =>
            filme.anoLancamento === anoLancamento);
}

const filterValue = (list, key, value) => {
    return list.filter((item) => item[key] === value);
}

console.log(filtrarFilmesPorAno(1999));
console.log(filterValue(catalogoFilmes, 'anoLancamento', 1999));
console.log(filterValue(catalogoFilmes, 'anoLancamento', 2050));

// EXERCICIO 03
const listaProdutos = [
    { id: 1, nome: "Camiseta", preco: 25.99 },
    { id: 2, nome: "Calça Jeans", preco: 49.99 },
    { id: 3, nome: "Tênis", preco: 79.99 },
    { id: 4, nome: "Boné", preco: 15.99 }
]

const filterByMaxValue = (list, key, maxValue) => {
    return list.filter((item) => item[key] <= maxValue);
}

const filtrarOrdernarProdutosPorPreco = (maxValue) => {
    const filteredList = filterByMaxValue(listaProdutos, 'preco', maxValue);
    return filteredList.sort((a,b) => a.preco - b.preco);
}

console.log(filtrarOrdernarProdutosPorPreco(50));

// EXERCICIO 04
const animais = [
    { id: 1, nome: "Leão", especie: "Felino", idade: 5 },
    { id: 2, nome: "Elefante", especie: "Mamífero", idade: 10 },
    { id: 3, nome: "Pinguim", especie: "Ave", idade: 3 }
]

const ordernarAnimais = (key, decrescente = false) => {
    return animais.sort((a, b) => {
        const comparingItemA = a[key];
        const comparingItemB = b[key];

        if (comparingItemA < comparingItemB) {
            return decrescente? 1 : -1;
        }

        if (comparingItemA > comparingItemB) {
            return decrescente? -1 : 1;
        }

        return 0;
    })
}

console.log(ordernarAnimais('nome', true));

// EXERCICIO 05
const departamentos = [
    {
        id: 1,
        nome: "Vendas",
        funcionarios: [
            { id: 101, nome: "Ana", cargo: "Vendedor" },
            { id: 102, nome: "Carlos", cargo: "Gerente de vendas" }
        ]
    },
    {
        id: 2,
        nome: "TI",
        funcionarios: [
            { id: 201, nome: "Maria", cargo: "Desenvolvedor" },
            { id: 202, nome: "João", cargo: "Analista de sistemas" }
        ]
    }
]

const encontrarFuncionarioPorId = () => {
    for (const departamento of departamentos) {
        const funcionarioEncontrado = departamento.funcionarios.find(funcionario => funcionario.id === id);
        if (funcionarioEncontrado) {
            return funcionarioEncontrado;
        }
    }
    return null;
}

// Encontra um funcionário com ID existente e imprime no console
const funcionarioEncontrado1 = encontrarFuncionarioPorId(201);
console.log("Funcionário encontrado (ID 201):");
console.log(funcionarioEncontrado1);

// Encontra um funcionário com ID inexistente e imprime no console
const funcionarioEncontrado2 = encontrarFuncionarioPorId(103);
console.log("\nFuncionário encontrado (ID 103):");
console.log(funcionarioEncontrado2)