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
