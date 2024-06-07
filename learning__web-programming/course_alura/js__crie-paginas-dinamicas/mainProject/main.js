function tocaSom(idElementoAudio) {
    document.querySelector(idElementoAudio).play();
}

// Declaração de referência
const listaDeTeclas = document.querySelectorAll('.tecla'); 

let i = 0;

while(i < listaDeTeclas.length) {
    const tecla = listaDeTeclas[i]; // deixando código mais limpo
    const instrumento = tecla.classList[1];

    // Aplicando Template String
    const idAudio = `#som_${instrumento}`;

    tecla.onclick = function () {
        tocaSom(idAudio) // concatenando com o
                                        // valor obtido
    };

    i++;
    // console.log(i);
}