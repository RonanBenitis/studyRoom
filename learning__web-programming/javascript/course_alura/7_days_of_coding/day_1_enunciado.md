Chegou a hora, Ronan Benitis Ferraz! Você vai começar a sua jornada no #7DaysOfCode ;)

Este primeiro dia é super importante! Ao final dele, você terá um novo conhecimento que é essencial para os próximos desafios.

Existe uma situação super comum para quem utiliza o Javascript: problemas com os tipos de variáveis na hora de comparar os valores de duas variáveis entre si. Eu já passei muito por isso!

Em linguagens de programação compiladas, como Java e C#, esse problema é detectado em tempo de compilação, e você que está desenvolvendo o código tem um aviso claro do erro.

Já no Javascript, esses erros passam despercebidos, já que o código não passa por um compilador. Ou seja, os erros só aparecem em tempo de execução.

A parte mais confusa para quem está começando a aprender lógica com Javascript é a operação de igualdade entre valores. Dependendo de como você escrever o seu código, o Javascript fará uma conversão de tipo para um tipo booleano de maneira implícita (automática), e isso afetará variáveis que eram Strings, Numbers, Object, etc….

Isso causa alguns comportamentos estranhos, como todos esses exemplos aqui abaixo retornando true:

```JAVASCRIPT
console.log( false == '0' );
console.log( null == undefined );
console.log( " \t\r\n" == 0 );
console.log( ' ' == 0 );
```
O que não faz necessariamente muito sentido.

(Você pode testar tudo isso indo no seu navegador, clicando com o botão direito, escolhendo a opção “Inspecionar” e a aba “Console”. Nessa aba, basta copiar e colar cada uma das linhas acima para confirmar que todas realmente retornam true).

Sendo assim, a sua tarefa de hoje é reescrever o código abaixo de maneira que ele imprima as informações de maneira correta, que faça sentido e sem erros:
```JAVASCRIPT
let numeroUm = 1
let stringUm = '1'
let numeroTrinta = 30
let stringTrinta = '30'
let numeroDez = 10
let stringDez = '10'

if (COMPARAR O numeroUm e a stringUm) {
  console.log('As variáveis numeroUm e stringUm tem o mesmo valor, mas tipos diferentes')
} else {
  console.log('As variáveis numeroUm e stringUm não tem o mesmo valor')
}

if (COMPARAR O numeroTrinta e a stringTrinta) {
  console.log('As variáveis numeroTrinta e stringTrinta tem o mesmo valor e mesmo tipo')
} else {
  console.log('As variáveis numeroTrinta e stringTrinta não tem o mesmo tipo')
}

if (COMPARAR O numeroDez e a stringDez) {
  console.log('As variáveis numeroDez e stringDez tem o mesmo valor, mas tipos diferentes')
} else {
  console.log('As variáveis numeroDez e stringDez não tem o mesmo valor')
}
```
### DICA
Você também pode utilizar o próprio navegador para executar esse seu programa, caso ainda não tenha familiaridade com editores de código, como o Visual Studio Code.

Para isso, como eu falei acima, basta você clicar com o botão direito do mouse em qualquer página, selecionar a opção “Inspecionar”, ir na aba “Console” e digitar o seu código. Bem simples, né?

Se você quiser mudar os nomes das variáveis e valores, fique à vontade. Mas jamais imprima algo que não seja verdadeiro, hein!

### EXTRA
Separei um artigo da Alura para você [aprender mais sobre operadores de comparação.](https://empresas.alura.com.br/e3t/Ctc/I8+113/d2z6gD04/VX0QGw9h4V5RW6bTfbr3v566vVkMXxJ5gcKyZN8yKgCK5kvg0W6N1X8z6lZ3pqW6LVkw94khJ53W51qf-38CgX5TN4h9r7_CyZp5V6mkY46tTp35VNKHvx8Vdd5wW1rTs151ppBgmW3f5DQG1-dvSsW4tY8j87CqF5FW19_qV27YJ0mMVQw6sz2l8YmVW58q07k64zlvwW2dhxpM7V1D1qW6j_C5w1QvfcHW5yrhQ55YmHyqW8PsxGx4gc6jBW3QLS6s8g_ZHBW7kWShh8Hk47TW3hM1sV7MPcbPW3ltcP15V1nZKTND_73BZWHpW7Tq6N01_Dt0DW3frZl53K8G3pW6dwCb2617tpXW3_D53S4LhpfQW2lb-Fk91cWMgW6MhPCB4X9lCfW8rk3bM5vhLp_W8N5tlH4tX_CdW75Rq0g8rQtDGW6RS-3C7jQ65RW5FDbpc8C-kv8W6VPYSr6dfzPtW1Nmf3C29gtFXW5Vtc043tzcLDW4sV8TD4D2xlCW3KWR6r83Sf7xW9gCT1k1b4znFVjKQ-B4YQZkQf7_L2Yn04)