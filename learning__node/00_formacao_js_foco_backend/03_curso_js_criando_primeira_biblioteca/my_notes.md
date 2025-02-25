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

