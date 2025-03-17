# <span style="color: #87BBA2">===   JavaScript com Node.js: criando sua primeira biblioteca   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">Acessando e lendo arquivos</span>

## INICIANDO UM PROEJTO NODE.JS
Qual runtime escolher?
- Temos, por exemplo, o Node, o Deno e o Bam
- Trabalharemos com o Node por ser a mais antiga, a mais utilizada e a mais testada.
- Então, Node é visto como o sinonimo de JavaScript para o Backend, mas, ele é mais uma entre as opções de se utilizar JavaScript serverside (porém, é a mais utilizada)

### Bibliotecas
Um ambiente de execução é composto por Bibliotecas. Seja esse ambiente Serverside ou seja no próprio navegador.

Bibliotecas são:
- Pacotes de código reutilizável que resolvem um problema ou necessidade especifica
- Busca evitar "reinventar a roda"
  - Reinventar a roda seria criar uma solução para um problema que já possui solução disponibilizada e testada. Como seria o caso de construir uma biblioteca para printar um texto no console, o qual seria desnecessário uma vez que o ambiente já possui biblioteca nativa para realizar essa mesma ação (biblioteca Console com método console.log)
  - As bibliotecas nativas são ótimos exemplos de soluções construidas de problemas muito comuns entre os desenvolvedores, tão comuns que se tornaram nativas ao ambiente. Novamente, como printar uma informação no console.

#### Por que utilizar bibliotecas?
**Pelos seus diversos usos e funcionalidades**:
- Pelo tamanho da complexidade dos problemas de programação, existem bibliotecas para basicamente tudo, como
  - Para faze validação
  - Para fazer teste
  - Conexão com banco de dados
  - Conexão para diversos serviços
  - Frontend, para fazer animação
  - Fazer converção de arquivos

São problemas comuns em programação que qualquer aplicação vai ter de resolver e pra não reinventar a roda utilizamos pacotes prontos e códigos que são disponibilizados pra gente, as tais das bibliotecas.

**Além disso, temos o reaproveitamento e eficiencia**:
- Ao invés de escrever e diagramar funcionalidades, já as teremos pronta
- Isso trará maior eficiência pois bibliotecas robustas já sofreram muitos testes, evitando que tenhamos que fazer o mesmo. 
- Torna-se um trabalho colaborativo uma vez que utilzaremos código desenvolvido por outras pessoas.

**Empresas e comunidade** desenvolvem bibliotecas:
- Muitas bibliotecas importantes, como as de autenticação, validação e conexão com bancos de dados, são desenvolvidas por empresas ou comunidades externas. Frequentemente, as empresas criam essas bibliotecas e as disponibilizam para uso geral.
- Algumas dessas bibliotecas são originalmente desenvolvidas para uso interno, mas, ao perceberem sua utilidade geral, são liberadas para uso externo. Isso ocorre porque resolveram problemas específicos dentro da empresa, mas viram potencial em compartilhar essas soluções com outras pessoas desenvolvedoras.

**Qualquer pessoa pode criar uma lib e publicá-la** atendendo certos pré-requisitos.

## USANDO A LINHA DE COMANDO
Criamos um um diretório src, com arquivo `index.js` dentro que será o ponto de entrada de nossa aplicação.

Teremos que fazer 3 coisas basicamente:
1. Pegar um arquivo de texto
2. Processar o conteudo do arquivo
3. Pensar em como disponibilizar o processamento realizado

### Atacando a primeira demanda
```js
const caminhoArquivo = require('../arquivos/texto-web.txt');

console.log(caminhoArquivo);
```
**Problema**
- Quando usamos `require()`, o código tenta imediatamente executar o código nele atrelado, e como não é um JSON e nem um código em si, retorna-se erro, já que ele busca interpretar com se fosse:
```bash
Como a Web funciona
     ^

SyntaxError: Unexpected identifier 'a'
```
- Outro ponto de melhoria seria não precisarmos abrir o arquivo `index.js` para passar o arquivo de texto, uma vez que, neste momento, precisamos entrar no arquivo para indicar um caminho de texto. Seria bom não precisarmos abrir o `index.js` para indicarmos outro arquivo de texto.

#### Vetor de Argumentos (Argument Vector)
```js
const caminhoArquivo = process.argv;

console.log(caminhoArquivo);
```
```bash
# NO CLI
$ node src/index.js

# RETORNO
# [
#   'C:\\Program Files\\nodejs\\node.exe',
#   'C:\\Users\\RONAN.FERRAZ\\Desktop\\developing\\studyRoom\\learning__node\\00_formacao_js_foco_backend\\03_curso_js_criando
# _primeira_biblioteca\\src\\index.js'
# ]
```
Ao atribuirmos a `caminhoArquivo` a instrução `process.argv`, estamos atribuindo à caminhoArquivo o método de process chamado `Argument Vector`, que transformará os valores que são colocados no terminal em uma Array e isso na Ordem que são executados.

No exemplo do retorno acima, temos:
1. O endereço em nosso computador onde estão os arquivos binários do Node
2. O segundo se refere onde está o código que será interpretados

**Realizando mais um teste:**
```bash
# NO CLI
$ node src/index.js alura

# RETORNO
# [
#   'C:\\Program Files\\nodejs\\node.exe',
#   'C:\\Users\\RONAN.FERRAZ\\Desktop\\developing\\studyRoom\\learning__node\\00_formacao_js_foco_backend\\03_curso_js_criando
# _primeira_biblioteca\\src\\index.js',
#   'alura'
# ]
```
O comando que passamos no CLI entrou no array, fazendo que consigamos acessá-lo em nosso código:
```js
const caminhoArquivo = process.argv;

console.log(caminhoArquivo[2]); // Retorno: Alura
```

Agora, podemos atribuir o local do arquivo sem necessitar entrar no `index.js` passando, como argumento do comando, o local relativo do arquivo:
```js
const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

console.log(link);
```
```bash
$ node src/index.js arquivos/texto-aprendizado.txt 

# RETONRO
# arquivos/texto-aprendizado.txt
```

## LENDO ARQUIVOS COM FS
Agora vamos fazer a leitura do arquivo de texto, e nisso vem a pergunta:
- Existe uma biblioteca que faça isso por mim?
- Sim! Existe, pois, interagir com arquivos é uma das coisas mais importantes e mais básicas que um programa precisa fazer, e por esse motivo existe uma biblioteca nativa ao Node.

### Sobre o FS (File System)
Fyle System geralmente é uma biblioteca que existe em diversas linguagens de programação e é uma das bibliotecas mais importantes justamente por dar acesso à interação com o Sistema de Arquivos (File System).

Ou seja, poder acessar, criar e alterar arquivos.

Segue o [link da funcionalidade do File System](https://nodejs.org/api/fs.html#file-system), tratando-se de uma leitura um pouco extensa (por ser uma funcionalidade robusta e completa). Mas, utilizaremos o seu método `readFile`

### Método readFile
[Documentação do readFile](https://nodejs.org/api/fs.html#fsreadfilepath-options-callback)

Quais são os parametros do método `readFile`:
- string: do caminho do arquivo
  - Algo que não está na documentação, mas precisamos fazer, é informar o enconding do nosso arquivo, sendo `utf-8`, o qual é o enconding para a maior parte das linguas latinas
- função callback: (error, data)

Como método funcionará:
- O método pegará o conteúdo que está no endereço informado
- Decodificará conforme o enconding que informamos
- Passará para o parametro `data`, ou no nosso caso `texto` o conteúdo decodificado com sucesso.
- Caso contrário, retornará o `err`.

```js
const fs = require('fs'); // Declarando Biblioteca File System

const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

fs.readFile(link, 'utf-8', (erro, texto) => {
    console.log(texto);
});
```
```bash
$ node src/index.js arquivos/texto-web.txt

# https://developer.mozilla.org/pt-BR/docs/Learn/Getting_started_with_the_web/How_the_Web_works

# Como a Web funciona

# Como a Web funciona oferece uma visão simplificada do que acontece 
# resto do texto...
```
#### Importante
Caso não utilizarmos o parametro de erro da callback, caso ocorra algum erro com a função, teremos o retorno de `undefined` para o parametro `data` e não saberemos qual foi o erro que ocorreu.

O valor do parametro callback `erro` quando não há erro será `null`, então, ideal printá-lo somente quando de fato algum valor nele existir.

Ou seja: Se algum erro ocorrer, `data` estará `undefined` e `err` terá o valor do que ocorreu. Caso nenhum erro ocorrer, `data` terá o valor da conversão e o `err` terá valor `null`.

## CAMINHO ABSOLUTO VS CAMINHO RELATIVO
### Caminho absoluto
Chamamos de caminho absoluto quando a localização de um arquivo ou pasta é especificado a partir do diretório-raiz do sistema operacional. Por exemplo:
```bash
#caminho para um diretório (a última `/` é opcional)
/home/juliana/Documents/alura/projeto-js

#caminho para um arquivo dentro do diretório
/home/juliana/Documents/alura/projeto-js/index.js
```

### Caminho relativo
Um caminho relativo para um diretório ou arquivo é definido a partir de sua relação com o pwd, ou seja, o present working directory (diretório de trabalho atual). Na linha de comando, pwd também é o comando print working directory (imprimir o diretório de trabalho), que usamos justamente para saber onde na estrutura do sistema operacional se encontra o diretório em que estamos.

Veja no exemplo abaixo uma representação em árvore de um diretório, como o do curso em que estamos trabalhando (o diretório node_modules foi excluído para facilitar a leitura, pois é muito extenso):
```bash
/home/juliana/Documents/nodejs-lib
.
├── arquivos
│   ├── texto-aprendizado.txt
│   ├── texto-kanban.txt
│   └── texto-web.txt
├── lib
│   ├── index.js
```

Na representação acima, consideramos como pwd o diretório nodejs-lib. Então, o caminho relativo do arquivo texto-web.txt, por exemplo, seria ./arquivos/texto-web.txt, e o caminho absoluto seria /home/juliana/Documents/texto-web.txt.

Na estrutura de diretórios, o . representa “aqui”. Quando queremos sair do diretório atual e “voltar” um nível, utilizamos ... Por exemplo:
```bash
/home/juliana/Documents/nodejs-lib
.
├── arquivos
│   ├── texto-aprendizado.txt
│   ├── texto-kanban.txt
│   └── texto-web.txt
├── lib
│   ├── index.js
```
Se quisermos referenciar algum dos arquivos de texto no arquivo ./src/index.js, devemos fazer da seguinte forma:
```js
// arquivo ./lib/index.js

const stringCaminhoTexto = ‘../arquivos/texto-web.txt’;
```
Usamos o .. para “subir um nível” na hierarquia de diretórios para só então “entrar” no diretório que queremos. Dessa forma, não precisamos referenciar o caminho absoluto de todos os arquivos quando fizermos importações de módulos; o que também funcionaria, mas não é tão prático.

Outra diferença importante entre caminho absoluto e relativo é com relação à execução de programas a partir da linha de comando. Por exemplo, usando a árvore de diretórios acima, o comando node index.js só funcionaria caso o diretório atual (pwd) no terminal já fosse /home/juliana/Documents/nodejs-lib/lib. Por outro lado, o comando node /home/juliana/Documents/nodejs-lib/lib/index.js funcionaria independentemente do diretório atual no terminal, pois o Node.js vai acessar o arquivo index.js a partir de seu caminho absoluto.

O terminal é uma ferramenta poderosa. Além de executar comandos e rodar programas, com ele podemos fazer tudo que fazemos com as janelas e ícones do sistema operacional como navegar entre diretórios (ou pastas), criar arquivos, mudá-los de lugar e renomeá-los, entre outras tarefas.

Pratique os comandos para ir ganhando agilidade e para ficar confortável com o sistema de arquivos e diretórios. Além disso, temos um [curso focado no uso do terminal para Linux](https://cursos.alura.com.br/course/terminal-comandos-executar-tarefas), porém os comandos podem ser utilizados no Windows com a ferramenta GitBash (que pode ser instalada automaticamente junto com o [Git](https://git-scm.com/) e também no terminal nativo do MacOs).

# <span style="color: #87BBA2">Criando a lógica do projeto</span>

## CAPTURANDO AS PALAVRAS
Vamos relembrar a função principal solicitada para esse programa:
- Percorrer o texto e contar as ocorrencias de palavras

### Lista do que fazer
Interessante citar que a instrutora, assim como em outros instrutores em outros cursos, as vezes utilizar o comentário como uma TODO LIST do que precisa ser atendido, segue o exemplo:
```js
const fs = require('fs'); // Declarando Biblioteca File System

const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

fs.readFile(link, 'utf-8', (erro, texto) => {
    verificaPalavrasDuplicadas(texto);
    if (erro) console.log(erro);
});

// Criar um array com as palavras
// Contar as ocorrências
// Montar um objeto com o resultado
    // uma ideia é fazer um objeto com suas chaves sendo a palavra e o valor as ocorrências, como:
    // { 
    //     "web": 5,
    //     "compudaor": 5,
    // }

const verificaPalavrasDuplicadas = (texto) => {
    
}
```

### Primeira versão do código
```js
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
```
```bash
# RETORNO
{
  'https://developer.mozilla.org/pt-BR/docs/Learn/Getting_started_with_the_web/How_the_Web_works\n\nComo': 1,
  a: 3,
  Web: 3,
  'funciona\n\nComo': 1,
  funciona: 1,
  oferece: 1,
  uma: 4,
  'visão': 1,
  simplificada: 1,
  # outras palavras...
}
```
Temos o primeiro código funcionando! Mas, existem coisas que precisamos tratar:
- Neste momento, não desejamos contar palavras muito curtas, como "do", "a" e afins.
- Trataremos os `escapes characters` (no caso, as quebras de linhas estão aparecendo)
- Limpeza de parenteses e aspas
- Tratamento da diferenciação de maiusculos e minusculos

## SEPARaNDO EM PARÁGRAFOS
Como queremos realizar a contagem de palavras repetidas por paragrafos, então, não faz sentido contarmos as palavras para, depois, então, uni-las novamente.

Para isso, criaremos uma função de `quebraEmParagrafos` e a declararemos antes da função de verificação de palavras duplicadas:
```js
function quebraEmParagrafos(texto) {
  const paragrafos = texto.toLowerCase().split('\n'); // Aqui esperamos que tenha um array composto, não de palavras separadas, mas sim de paragrafos separados
  console.log(paragrafos);
}
```
- Métodos encadeados = Quando chamamos um método seguido do outro, que aproveitará o retorno do primeiro método.
  - No caso, estamos realizando o `.split('\n')`, com o retorno do split, realizamos `.toLowerCase()`.
  - No caso, não mudará no resultado se jogarmos tudo para minusculo ou tudo para maiusculo, mas, jogamos tudo para minusculos pois como tem muito menos letras maiuscula, **faz mais sentido jogar a poucas letras maiusculas para minusculas**. Talvez, isso possa reduzir o processamento (bem pouco, mas deve reduzir).
- `\n` = caracter de escape que representa quebra de linha. Caracteres de escape não são renderizados.

**Encadear métodos pode ter beneficios performaticos**, já que o programa já percorrerá todo o texto, encadear métodos o faz aproveitar a operação tornando-o mais performatico ao invés de realizar primeiro um e depois o outro.

### Contando palavras duplicadas em cada paragrafo
```js
const fs = require('fs'); // Declarando Biblioteca File System

const caminhoArquivo = process.argv;
const link = caminhoArquivo[2];

fs.readFile(link, 'utf-8', (erro, texto) => {
    quebraEmParagrafos(texto);
    // verificaPalavrasDuplicadas(texto);
    if (erro) console.log(erro);
});

const quebraEmParagrafos = (texto) => {
    // Aqui esperamos que tenha um array composto, não de palavras separadas, mas sim de paragrafos separados
    const paragrafos = texto.toLowerCase().split(/\n|\r/);

    // Aplicando contagem em cada paragrafo
    const contagem = paragrafos.map(( paragrafo ) => {
        return verificaPalavrasDuplicadas(paragrafo);
    })

    // Verificando retorno
    console.log(contagem);
}

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

    return resultado; // Trocamos console.log pelo retorno
}
```
- Note que agora percorremos a array de paragrafos e passamos a função de verificação de duplicatas em cada elemento da array, resultando em uma nova array com a contagem.
- Note, também, que utilizamos regex para splitar ou no caracter de escape de pular linha (`\n`) ou no caracter de escape de "carraiage return" (retorno de carro), que equivale ao vonteúdo disparado quando se aprta a tecla ENTER.
  - O `\r` força uma "quebra na linha" e reposiciona o cursor (ou o carro) na posição inicial da linha seguinte, porém, ele ainda pertence a linha de cima.
  - No `\n` já é criada uma nova linha independente das anteriores.
- Ainda temos coisas a fazer, já que linhas vazias estão sendo contadas como paragrafos.

## PARA SABER MAIS: CARACTERES DE QUEBRA DE LINHA
Durante esta aula vimos um caractere diferente, o \n. Caracteres precedidos pela barra \ são chamados “caracteres de escape” e deixam de ter significado literal (por exemplo, a letra N) e passam a significar instruções específicas dadas ao interpretador do texto. Por exemplo, inserir uma quebra de linha, inserir caracteres especiais, tabulação e espaços etc.

### Alguns exemplos de caracteres de escape:
- `\'` insere aspas simples
- `\"` insere aspas duplas
- `\\` insere barra invertida
- `\n` insere nova linha (new line)
- `\r` insere nova linha (carriage return)
- `\t` insere tabulação
- `\b` insere backspace

Para finalizar “fim de linha” ou “quebra de linha”, existem alguns caracteres diferentes e diferentes sistemas operacionais utilizam estes caracteres de formas diferentes ao interpretarem textos.

- Em sistemas Unix e Unix-like (como o Linux) o caractere usado é \n (new line).
- `\n` também é caractere de escape padrão para quebra de linha em todas as linguagens baseadas em C (é o caso do JavaScript).
- Em sistemas Windows, a quebra de linha usa o caractere \r, ou carriage return. O nome vem das antigas máquinas de escrever em que o posicionamento da peça responsável por imprimir as letras (carro ou carriage em inglês) era feito manualmente a cada fim de linha.
- Em antigos sistemas Mac (anteriores ao macOS X) o padrão era `\r\n`, nessa ordem.
- A diferença não é apenas no caractere: `\n` representa o fim de uma linha, o que para Linux e Mac é o equivalente a começar uma nova linha de texto. Já \r move o cursor para o início de uma nova linha (como a máquina de escrever).

É muito importante entender a forma como os sistemas operacionais e as linguagens “encodam” (ou interpretam) os caracteres em uma string para transformá-los em texto, pois as diferenças podem causar bugs de interpretação de caracteres onde menos se espera.

## REFINANDO A CONTAGEM
Agora, limparemos os caracteres especiais. Vamos fazer uma instrução que substitua caracteres especiais por nada (suprimindo)

Para isso, utilizaremos o método de string chamado `replace`, e ele faz justamente o que seu nome já diz: Substitui algo por outra coisa.
- `string.replace('elemento_a_ser_substituido', 'elemento_que_o_substitui');`

### Passando multiplos caracteres especiais
No caso de replace, poderiamos limpar um `(` da seguinte forma:
```js
string.replace('(', '');
```
Assim, substituiremos `(` por string vazia. Mas, isso serve apenas para um elemento. Caso escrevessemos diversos elementos dentro dessa aspa, o JavaScript interpretaria tudo como string única:
```js
string.replace('(!@#$', '');
// A string '(!@#$' será substituida por string vazia
```

#### Tornando manipulação de string mais abrangente (Regex)
Uma forma de tornar a manipulação de string mais abrangente é utilizando o recurso **Expressão Regular** ou **Regex**
```js
string.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, '')
```
**Explicando**
- Dentro dos colchetes foram passados todos os casos de caracter especial que achamos que ocorrerá no texto.
- Delimitadores `/`: Expressão começa e termina com `/`, que delimitam regex em JavaScript
- Conjunto de caracteres `[...]`: Os colchetes indicam que o regex está buscando **qualquer um** dos caracteres listados dentro deles
- Caracteres dentro do conjunto: São os caracteres que desejamos identificar, que no caso, são caracteres especiais.
- Barra invertida antes de alguns caracteres `\`: Alguns caracteres tem significado especial em regex (como o `/` e o `^`) e precisam ser "escapados" com `\`.
- Modificador `g` (global): O `g` faz com que regex **busque todos os caracteres correspondentes** na string em vez de para na primeira ocorrência
- No caso, o retorno da lista ainda existem algumas palavras que estão entre `''` mas essas aspas não são aspas do texto mesmo, eles estão com aspas por serem palavras com acento. Provavelmente, isso deve ser algo da linguagem para não retornar algo que execute alguma coisa indevidamente.

**Expressão regular** é um tipo de linguagem utilizado para identificar padrões em strings. Ou seja, toda vez que o `.replace()`, neste caso, identificar esse padrão, ele suprimirá por nada.

### Desenvolvimento do código
```js
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
```
Agora, criamos a função `limpaPalavras(palavra)` e a acrescentamos no for da lista de palavras, além de definir um limitador de tamanho de palavra.

## ORGANIZANDO A SAÍDA DOS DADOS
Agora, criaremos um método para limpar os paragrafos vazios.

```js
const quebraEmParagrafos = (texto) => {
    // Aqui esperamos que tenha um array composto, não de palavras separadas, mas sim de paragrafos separados
    const paragrafos = texto.toLowerCase().split(/\n|\r/);

    // Aplicando contagem em cada paragrafo
    const contagem = paragrafos
        .filter(( paragrafo ) => paragrafo)
        .map(( paragrafo ) => {
            return verificaPalavrasDuplicadas(paragrafo);
        })

    // Verificando retorno
    console.log(contagem);
}
```
### Pontos importantes
- Não podemos realizar um `if` dentro do `.map` pois ele **sempre retorna um valor**, já que a array de saída terá o mesmo tamanho da array de entrada. O retorno seria `undefined` caso colocassemos um `if` no `.map`.
- Para resolver a questão, passaremos um `.filter()` após o mapeamento.
  - `.filter()` é um método callback que sempre trabalha com uma comparação dentro da função, então, se a comparação for `true`, ele joga pra dentro da nova array. Se a comparação for `false`, ele ignora.
  - Para resolvermos isso de forma concisa, faremos da seguinte forma: `.filter(( paragrafo ) => paragrafo)`. Isso funcionará pois JavaScript interpreta string vazia como `falsy`, logo, se paragrafo for string vazia, ele será ignorado. Então, **se JavaScript tiver que transformar uma string vazia em booleano, ele retornará como false, e se a string não tiver vazia, JavaScript retornará como true**.
- Realizaremos estas operações de forma encadeada.

### Considerações
Para conseguir fazer primeiro o mapeamento (`.map()`) e depois a filtragem (`.filter()`), realizamos 2 loops:
- Primeiro percorremos o paragrafo inteiro para fazer a contagem (mapeamento com função de `verificarPalavrasDuplicadas()`)
- Depois percorremos toda a array novamente para realizar a filtragem.

Quando trabalhado com massas pequenas de dados, a questão de performance será risória em função da capacidade de processamento das maquinas atuais. Mas, caso trabalharmos com uma massa de dados de 2 milhões de usuários, poderemos começar a sentir maiores latências (não ficará muito performatico).

Para resolvermos essa questão, podemos utilizar o método `.flatMap()`.

### Método flatMap
> The flatMap() method of Array instances returns a new array formed by applying a given callback function to each element of the array, and then flattening the result by one level. It is identical to a map() followed by a flat() of depth 1 (arr.map(...args).flat()), but slightly more efficient than calling those two methods separately.

O método `.flatMap()` também é uma função callback.
```js
// Aplicando contagem em cada paragrafo
const contagem = paragrafos.flatMap(( paragrafo ) => {
    if (!paragrafo) return [];
    return verificaPalavrasDuplicadas(paragrafo);
})
```
- Este código terá o mesmo resultado do que o `.map()` e o `.filter()`, mas com um loop apenas.

#### O que o flat faz
O `flat`, sozinho, é um método que um array que tem arrays dentro e **"achata"**.
```js
const arrayComArray = [1, 2, 3, [4, 5], [6, 7], [8, 9]];
console.log(arrayComArray);
// retorno: [ 1, 2, 3, [ 4, 5 ], [ 6, 7 ], [ 8, 9 ] ]

const arrayNumeros = arrayComArray.flat();
console.log(arrayNumeros);
// retorno: [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Mas, por padrão, ele **"achata"** apenas um nivel, ou seja, "abre um nivel de array". Se tiver um array com 2 niveis, deixa-a com 1 nivel.
```js
const arrayComArrayComArray = [1, 2, 3, [4, 5], [6, 7], [8, 9, [10, 11, 12]]];
console.log(arrayComArrayComArray);
// retorno: [ 1, 2, 3, [ 4, 5 ], [ 6, 7 ], [ 8, 9, [ 10, 11, 12 ] ] ]

const arrayNumeros = arrayComArray.flat();
console.log(arrayNumeros);
// retorno: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, [ 10, 11, 12 ] ]
```

Porém, podemos configurar a profundidade do "achatamento", podendo até ir ao infinito `.flat(Infinity);`
```js
const arrayComArrayComArray = [1, 2, 3, [4, 5], [6, 7], [8, 9, [10, 11, 12]]];
console.log(arrayComArrayComArray);
// retorno: [ 1, 2, 3, [ 4, 5 ], [ 6, 7 ], [ 8, 9, [ 10, 11, 12 ] ] ]

const arrayNumeros = arrayComArrayComArray.flat(2);
console.log(arrayNumeros);
// retorno: [ 1,  2, 3, 4,  5, 6,  7, 8, 9, 10, 11, 12]
```

#### O que o flatMap faz
O flatMap combina as funcionalidades de `map` e `flat(1)`. Ou seja:
1. Transforma os elementos da array (como o map faz).
2. Achata (flatten) o resultado em um único nível de profundidade.

Isso significa que, se uma função dentro do `flatMap` retornar uma array vazia ([]), o resultado será removido da array final, funcionando de forma semelhante a um filtro.
```js
const contagem = paragrafos.flatMap(( paragrafo ) => {
    if (!paragrafo) return []; // Remove par
    return verificaPalavrasDuplicadas(paragrafo);
})
```
Aqui, flatMap está sendo usado para:
- ✅ Filtrar (return [] elimina elementos vazios).
- ✅ Transformar (verificaPalavrasDuplicadas processa os parágrafos).
- ✅ Achatar o resultado (flat(1) evita um array dentro de outro array).

Essa abordagem evita a necessidade de chamar map seguido de flat, deixando o código mais limpo e performático.

## UTILIZANDO REDUCE
Durante a aula praticamos a manipulação de arrays e objetos usando duas abordagens:
- filter e map
- flatMap

Porém, ainda há uma terceira abordagem para a resolução desse problema muito comum em programação: como suprimir objetos vazios de um array de objetos. Para isso, vamos usar o método de array reduce.

### Resolvendo utilizando reduce
O funcionamento básico do reduce é percorrer todos os índices de um array e “reduzir” seus valores a um único valor de retorno. Por exemplo:

```js
const numeros = [1, 2, 3, 4, 5];

const result = numeros.reduce((acum, atual) => acum + atual, 0);

console.log(result); //15
```

No exemplo acima, usamos reduce para reduzir um array de números até a soma de todos eles, começando a contagem em 0 e somando os parâmetros da função callback a cada iteração (valor acumulado + valor atual).

Porém, o reduce também tem muitos usos mais complexos para arrays de objetos e pode nos ajudar a resolver o problema dos objetos vazios.

Observe abaixo uma versão mais curta da solução feita com filter e map:
```js
const paragrafos = ["código", "js", "", "web", "", "array"];

const result = paragrafos
 .filter((paragrafo) => paragrafo)
 .map((paragrafo) => {
   if (paragrafo) return paragrafo;
 });
console.log(result);
```

Agora, vamos analisar uma abordagem utilizando reduce:
```js
const paragrafos = ["código", "js", "", "web", "", "array"];

const result = paragrafos.reduce((acum, paragrafo) => {
 if (paragrafo) {
   return [...acum, paragrafo];
 }
 return acum;
}, []);

console.log(result);
```

Acompanhe os passos de desenvolvimento do código acima:
1. Queremos “reduzir” o array atual a um outro array, então iniciamos reduce com um valor atual de [] (um array vazio).
2. Os parâmetros da função callback são acum (em que são armazenados os valores já processados) e paragrafo, que se refere ao parágrafo sendo processado a cada iteração.
3. A condicional if (paragrafo) avalia a string paragrafo em termos booleanos (lembrando de valores truthy e falsy) e apenas entra no if caso paragrafo não seja uma string vazia.
4. Caso não seja uma string vazia, o código dentro do bloco if utiliza o spread operator (operador de espalhamento) para retornar um array composto dos valores anteriores (acum) “espalhados” em um novo array com o conteúdo do parágrafo atual.
5. Caso seja uma string vazia, o código do bloco if não será executado, e o loop do reduce irá passar direto para o próximo elemento do array, ignorando a string vazia e a deixando de fora do array final.
6. Após percorrer todos os elementos, o resultado final de acum será um array composto apenas de strings “não vazias” (avaliadas como truthy na condicional if).

Qual método utilizar? Apesar de o método reduce construir um novo array a cada iteração, a não ser que se trate de textos e arrays muito grandes, não deve haver muita diferença de performance entre os métodos.

É comum existir mais de uma forma de resolver problemas de lógica de programação! Faça os testes em seu projeto!

# <span style="color: #87BBA2">Tratamento de erros</span>

## IDENTIFICANDO TIPOS DE ERROS
Agora vamos identificar alguns pontos de falha que podem ocorrer no nosso programa.

Um ponto de falha que pode ocorrer, e talvez tenha ocorrido enquanto você estava praticando, é quando nos distraímos e, ao passar o endereço do arquivo que queremos converter ou processar, não passamos um pedaço do endereço e ocorre um erro genérico, um TypeError dizendo que não consegue ler propriedades de undefined. Esse é um exemplo de um erro que pode acontecer.
```bash
TypeError: Cannot read properties of undefined (reading 'toLowerCase')
    at quebraEmParagrafos (/home/juliana/Documents/nodejs-lib/src/index.js:23:28)
    at ReadFileContext.callback (/home/juliana/Documents/nodejs-lib/src/index.js:7:3)
    at FSReqCallback.readFileAfterOpen [as oncomplete] (node:fs:306:13)
```

Normalmente, começamos a mapear pontos onde pode ocorrer algum tipo de erro e o capturaremos para tratá-los e, então, indicamos o que queremos fazer quando capturamos o erro: Se queremos enviar uma mensagem ou fazer qualquer outra coisa no lugar.

### Refatorando
Agora, criaremos uma função de ponto de entrada, chamado `contaPalavras` e ajustamos algumas responsabilidade de funções
```js
fs.readFile(link, 'utf-8', (erro, texto) => {
    contaPalavras(texto);
    if (erro) console.log(erro);
});

function contaPalavras(texto) {
    // Passaremos todo o conteúdo de querbaParagrafo aqui, com execção da quebra de palavras
    const paragrafos = extraiParagrafos(texto);
    const contagem = paragrafos.flatMap(( paragrafo ) => {
        if (!paragrafo) return [];
        return verificaPalavrasDuplicadas(paragrafo);
    })
    console.log(contagem);
}

function extraiParagrafos(texto) {
    return texto.toLowerCase().split(/\n|\r/);
}
```

### Marcações de erro
O primeiro ponto de erro que dá para identificar é justamente dentro do `readFile`, que, por sinal, o callback do `readFile` já vem por si com um parâmetro de função do callback `erro`, só esperando para ser chamado, porque justamente esse é um ponto crítico de falha.

Ao darmos um `console.log` no parametro de erro e chamar o programa sem passar a extensão do arquivo (ou seja, forçando um erro), é printado na tela o erro que ocorre, sendo um `ENOENT`, que trata-se de um erro em função de não encontrar uma entidade.

Agora, utilizaremos um `if` para verificar a existencia deste erro:
```js
fs.readFile(link, 'utf-8', (erro, texto) => {
   if (erro) {
    console.log('qual é o erro?', erro);
    return
   }
   contaPalavras(texto);
})
```
- A utilização do `return` dentro de uma função o encerra. `return` deste modo, talvez, podem ser chamados de `early return`.
- Neste caso, estamos verificando a existência de erro e, caso encontrado, printamos e encerramos a função.
- Isso é possivel pois o parametro callback **retorna um erro** ao invés de **lançar um erro**. Quando lançamos um erro, a execução é redirecionada para o primeiro catch.

Os `erros` são objetos que podemos acessar suas propriedades, como, neste caso, o `erro.code`, onde podemos acessar diretamente o código deste erro e criar validações para tal, como, "se o erro for ENOENT, faça X".

## ENTENDENDO A STACK TRACE
Uma das primeiras coisas que percebemos ao começarmos a programar é que praticamente qualquer aviso de erro será acompanhado de uma longa sequência de texto difícil de compreender.

Por exemplo, se tentarmos usar console.log() em alguma variável que não existe em nosso código:
```bash
node teste.js

file:///home/juliana/Documents/nodejs-lib/teste.js:3
console.log(nome);
            ^

ReferenceError: nome is not defined
    at file:///home/juliana/Documents/nodejs-lib/teste.js:3:13
    at ModuleJob.run (node:internal/modules/esm/module_job:218:25)
    at async ModuleLoader.import (node:internal/modules/esm/loader:329:24)
    at async loadESM (node:internal/process/esm_loader:28:7)
    at async handleMainPromise (node:internal/modules/run_main:113:12)

Node.js v20.11.0
```

Boa parte de todo esse texto é representado pela stack trace, ou seja, pelo “rastro” de comandos executados pelo interpretador ao enviarmos o comando node teste.js.

No caso, para que o Node.js execute corretamente o código dentro de um arquivo .js de nosso projeto, ele utiliza por sua vez diversos códigos (funções) que estão dentro de seu próprio código-fonte. Cada parte do código necessário para que o Node.js interprete corretamente o nosso próprio código pode se encontrar em arquivos ou módulos diferentes, e cada comando executado “guarda” este caminho desde o ponto inicial até o último.

Podemos analisar qualquer linha do erro acima e acompanhar este processo:
```bash
at file:///home/juliana/Documents/nodejs-lib/teste.js:3:13
```

O ponto inicial de chamada do código problemático: arquivo teste.js que está dentro da nossa pasta de projeto, na linha 3 e coluna 13.
```bash
at ModuleJob.run (node:internal/modules/esm/module_job:218:25)
```

Este erro se “propagou” para o método ModuleJob.run interno do Node.js. Podemos saber que já não estamos mais na pasta do nosso projeto pois a stack trace fornece exatamente o módulo, linha e coluna para onde o erro se propagou.

Assim continua até o último ponto, a função interna do Node.js handleMainPromise.

Quando um erro ocorre, todo esse caminho percorrido pelo comando é passado para dentro de um objeto Error para que possa ser acessado e consultado de alguma forma, por exemplo, exibido no terminal. Dessa forma, podemos usar esse “mapa” para entender o caminho que o processamento percorreu.

Nem todos os avisos de erro são gerados da mesma forma: dependendo da origem, alguns erros são devolvidos pelo sistema operacional, outros pelo Node.js, outros podem ser gerados a partir de alguma biblioteca que estamos usando em nosso projeto. Porém, quase sempre eles seguem o mesmo padrão, apresentando o nome do erro, a descrição do erro e a stack trace.

O Node.js tem uma lista de erros próprios. Confira como Error se comporta no Node.js, uma descrição de cada erro e motivos comuns para acontecerem neste [artigo da Alura sobre erros do Node.js](https://www.alura.com.br/artigos/lidando-com-erros-node-js).