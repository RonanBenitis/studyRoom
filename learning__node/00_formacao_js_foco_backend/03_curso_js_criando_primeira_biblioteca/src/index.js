const fs = require('fs'); // Declarando Biblioteca File System

const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

fs.readFile(link, 'utf-8', (erro, texto) => {
    contaPalavras(texto);
    if (erro) console.log(erro);
});

const contaPalavras = (texto) => {
    const paragrafos = extraiParagrafos(texto);
    const contagem = paragrafos.flatMap(( paragrafo ) => {
        if (!paragrafo) return [];
        return verificaPalavrasDuplicadas(paragrafo);
    })

    console.log(contagem);
}

const extraiParagrafos = (texto) => {
    // Aqui esperamos que tenha um array composto, não de palavras separadas, mas sim de paragrafos separados
    return texto.toLowerCase().split(/\n|\r/);
}

const limpaPalavras = (palavra) => {
    return palavra.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()']/g, '');
    // return palavra;
}

const verificaPalavrasDuplicadas = (texto) => {
    // Indicamos o separador sendo um espaço, ou seja, toda vez que existir um espaço, splitaremos a string. Com isso, construiremos um array com as palavras do texto
    const listaPalavras = texto.split(' ');

    // Iniciando objeto vazio
    const resultado = {};

    // Construindo objeto de retorno
    for (const palavra of listaPalavras) {
        // Retirando palavras curtas
        if (palavra.length >= 3) {
            // Realizando limpeza da palavra
            const palavraLimpa = limpaPalavras(palavra);
            // Se existe, pega o valor, se não, é 0 e então incrementa
            resultado[palavraLimpa] = (resultado[palavraLimpa] || 0) + 1;
        }
    }

    return resultado;
}