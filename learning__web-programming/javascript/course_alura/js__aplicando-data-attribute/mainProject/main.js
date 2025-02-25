function tocaSom(seletorAudio) {
    const elemento =  document.querySelector(seletorAudio);

    // Tratando possiveis erros de input
    if (elemento && elemento.localName === 'audio') {
        /*
        Javascript interpreta, quando colocamos nenhuma condição (observe
        o caso if(elemento)) para iniciar a condição caso o parametro
        EXISTA, ou seja, quando o parametro É UM VALOR, ou seja, não for
        igual a null, 0, vazio, undefined
        */
        elemento.play();
        console.log("Olá Mundo! Mais um curso finalizado! :)")
    } else {
        alert('Elemento inválido ou não encontrado');
        console.log('Elemento inválido ou não encontrado');
    }
}

// Declaração de referência
const listaDeTeclas = document.querySelectorAll('.tecla'); 

for (let i = 0; i < listaDeTeclas.length; i++) {
    const tecla = listaDeTeclas[i]; // deixando código mais limpo
    const instrumento = tecla.classList[1];

    // Aplicando Template String
    const idAudio = `#som_${instrumento}`;

    tecla.onclick = function() {
        tocaSom(idAudio);
    };

    tecla.onkeydown = function(evento) {
        if (evento.code === "Enter" || evento.code === "Space") {
            tecla.classList.add('ativa');
        }
    }

    tecla.onkeyup = function() {
        tecla.classList.remove('ativa');
    }
}

// APLICANDO DATA ATTRIBUTES CONFORME VISTO EM
// https://cursos.alura.com.br/extra/alura-mais/data-attributes-do-html5-c109
const titulos = document.querySelectorAll('[data-titulo]');

// Deixado para visualizar sintaxe do forEach
// function esconderConteudos() {
//     const conteudos = document.querySelectorAll('[data-conteudo]');

//     conteudos.forEach(conteudo => conteudo.classList.add('hide'));
// }

function alternaConteudo(valor) {
    const conteudo = document.querySelector(`[data-conteudo="${valor}"]`);

    if (conteudo.classList.contains('hide')) {
        conteudo.classList.remove('hide');
    } else {
        conteudo.classList.add('hide');
    }
}

titulos.forEach(titulo => titulo.addEventListener('click', function() {
    /*
    captura o valor do Data Attribute data-titulo, que nos casos
    seria "abrir"
    */
    const valor = titulo.dataset.titulo;

    /*
    passando o valor como parametro, conseguimos selecionar o
    [data-conteudo="abrir"], possibilitando sua manipulação pontual
    */
    alternaConteudo(valor);
}))