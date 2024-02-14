// Snipet in JavaScript

// Pom ------------------------------------------------
function tocaSomPom(){
    // Bloco ou corpo da função
    document.querySelector('#som_tecla_pom').play();
}

// Declaração de referência
const listaDeTeclas = document.querySelectorAll('.tecla'); 

listaDeTeclas[0].onclick = tocaSomPom;

// Desafio: Automatizar a reprodução sem utilizar o método de copiar e colar para cada indice existente.