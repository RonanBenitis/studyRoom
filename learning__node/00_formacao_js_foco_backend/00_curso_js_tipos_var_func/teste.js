const aprovado = ture;

if (aprovado === true) {
    console.log('aprovado');
}

/*
IGUALDADE FROUXA
Compara só o conteúdo
- JS faz algumas conversões por baixo dos panos
*/
if ('0' == 0) {
    console.log('Passou');
} else {
    console.log('Não passou');
}

/* 
IGUALDADE ESTRITA
Compara conteúdo e seu tipo
- Nenhuma conversão feita, mais seguro pela restrição
*/
if ('0' === 0) {
    console.log('Passou');
} else {
    console.log('Não passou');
}
