const fs = require('fs'); // Declarando Biblioteca File System

const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

fs.readFile(link, 'utf-8', (erro, texto) => {
    verificaPalavrasDuplicadas(texto);
    if (erro) console.log(erro);
});

const verificaPalavrasDuplicadas = (texto) => {
    // Indicamos o separador sendo um espaço, ou seja, toda vez que existir um espaço, splitaremos a string. Com isso, construiremos um array com as palavras do texto
    const listaPalavras = texto.split(' ');

    // Iniciando objeto vazio
    const resultado = {};

    // Construindo objeto de retorno
    for (const palavra of listaPalavras) {
        // Se existe, pega o valor, se não, é 0 e então incrementa
        resultado[palavra] = (resultado[palavra] || 0) + 1;
    }

    console.log(resultado);
}