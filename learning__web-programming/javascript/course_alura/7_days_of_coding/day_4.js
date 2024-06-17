/* Lembrando, Math.random é 0 até e exclusivamente 1, ou seja,
0 até < 1 (não inclui o número 1). Como queremos valores de 0 a 10,
fazemos então Math.random () * 11, pois, 11 * 0.99 é 10.8989989 e 
parseamos para inteiro (rola um truncante). Se fosse de 1 a 10, fariamos
Math.random() * 10 + 1.

Math.floor(Math.random() * (máximo - mínimo + 1) + mínimo) deve
funcionar também.
*/
const numeroAdivinhar = parseInt(Math.random() * 11); 
const limiteTentativas = 3;
let tentativa = 1;
let chute;

while (tentativa <= limiteTentativas) {
    chute = prompt('Chute um número de 0 a 10');
    if (chute == numeroAdivinhar) {
        break;
    } else {
        alert(`Errou! Você tem ${limiteTentativas - tentativa} tentativa(s)`)
        tentativa++;
    }
}

if (chute == numeroAdivinhar) {
    alert(`Você acertou na ${tentativa} tentativa! Parabéns!`);
} else {
    alert(`Tentativas esgotadas! O número era ${numeroAdivinhar}, não foi dessa vez. :(`)
}

/*
Declarar a variável chute fora do loop foi uma boa prática para garantir
que ela tenha o escopo correto e para evitar qualquer confusão com o valor
que ela mantém após o loop ser concluído. Isso também ajuda a prevenir
erros se houver outros scripts ou partes do programa que possam estar
usando uma variável com o mesmo nome.

Se precisar de mais alguma ajuda ou tiver outras dúvidas, estou aqui para ajudar!
*/