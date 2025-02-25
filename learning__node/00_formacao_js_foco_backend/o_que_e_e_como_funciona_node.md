# <span style="color: #87BBA2">===   O QUE É E COMO FUNCIONA O NODE   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">Alura explica</span>

- [Link da explicação](https://cursos.alura.com.br/extra/alura-mais/nodejs-o-que-e-e-como-funciona-c1414)

## Engine
Node funciona na Engine V8, a mesma Engine desenvolvida pelo Google e que roda no Google Chrome.
- Firefox utiliza a engine SpiderMonkey
- Edge utiliza a engine Chromium

## Runtime Environment
Porém, Node é desenvolvimento em ambiente RunTime, ou seja, em um ambiente próprio de interpretação da linguagem ao lado do servidor, sem a necessidade de rodar em um navegador. Por isso, Node é dito como um ambiente JavaScript runtime de código aberto e multiplataforma que possibilita executar códigos JavaScript forma de um Navegador.

## Diferenças de Node e JavaScript
Node é uma tecnologia que contém API's e bibliotecas especificas que o JavaScript para navegador não possui, e vice e versa.
- Node, por exemplo, não possui as bibliotecas para manipulação de DOM que o JavaScript para navegador tem, justamente pelo Node não necessitar operar DOM por estarmos trabalhando com o servidor
- Por outro lado, Node possui bibliotecas de HTTP e afins que JavaScript de navegador não possuem, pelos mesmos motivos.

## Roda em todos os navegadores, mas Engines influenciam
Node roda em todos os navegadores, porém, a diferença de engines tem uma influencia na execução do código. Por exemplo o método `.sort()`. Este método, executado na engine `V8` é feito de maneiras distintas de quando este for executado no `SpiderMonkey` ou no `Chromium`. Ou seja, o método será executado, mas com diferenças em sua execução (e muito provavelmente chegando em implementações e resultados similares)

## Package.json
Após iniciar um projeto Node, nos depararemos com o package.json. Recomenda-se, por exemplo, ser o primeiro arquivo a olharmos para termosu ma ideia do projeto.

Chamado, também, de arquivo manifesto, é onde teremos diversas informações cruciais de um projeto existente:
- A autoria do código
- A qual repositório no GitHub ele pertence
- Quais bibliotecas e as versões delas são as dependencias desse código
  - Todos os pacotes externos que estão sendo utilizados em um projeto

## NPM e YARN
São gerenciadores de pacote (Package manager) mais utilizados.
- São repositórios, como gitHub pro código, voltados para pacotes de códigos Node
- NPM é nativo, já vem com a instalação do Node, e com o NPM pode-se instalar o YARN.

## NODE MODULES
Aqui é o diretório onde o Gerenciador de Pacote baixará a dependencia do repositório.
- A partir daí, as ferramentas ficam disponibilizadas para utilização no projeto.
- Esse processo também atualiza o package.json
- O NPM, ao instalar uma biblioteca, coloca um  `^` antes do número da versão dela para indicar que atualizações automaticas de "subversão" podem ser feitas.
  - "subversão", que digo, são as atualizações que não interferirão pesadamente com a sua atualização, indicado após o primeiro ponto no número da versão.
  - Quando muda-se o número à esquerda do primeiro ponto, aí sim é um indicativo de uma nova Versão que pode (e muito provavalmente irá) interferir em ferramentas pré existentes ou criar novas ferramentas não suportadas pela versão anterior.
  - O que será atualizado automaticamente serão todas as versões que mantém a versão indicada antes da pontuação, atualizando somente as versões posteriores a pontuação: 3.10.1 para 3.15.0 atualiza. 3.10.1 para 4.0 não atualiza.

Lembrando que uma biblioteca também contém suas prórprias dependencias que não aparecerão no node_modules (provavelmente apareça mais no package lock). Ao instalarmos **apenas** a biblioteca express, veremos que será necessário utilizar aproximadamente outros 50 pacotes.

## PACKAGE LOCK
Administra de forma mais detalhada o versionamento das dependencias.

## E onde entra o Node nisso?
Ao escrevermos um código JavaScript (ou TypeScript) e, na linha de comando, escrevermos `node` e o nome do arquivo do código escrito, estamos dizendo:

```bash
node index.js
```
- Use o Node para executar o código que está dentro deste arquivo (index.js)
- Uma vez que é um arquivo JavaScript, todas as bibliotecas estão indexadas direitinho e o Node consegue encontrar tudo o que ele precisa, o Node executa o código indicado **fora do navegador sendo INTERPRETADO PELO NODE**.

## E porque linguagem Frontend necessita de Node e sua estrutura?
Ao trabalharmos com React, Angular, Vue, nos deparamos com a necessidade de ter o Node e sua estrutura de package.json, node modules e afins.

Apesar de estarmos desenvolvendo para um navegador e este navegador ser capaz de interpretar o código desejado, **necessitaremos de recursos externos a ele**, como exemplo:
- Bibliotecas de sevidor local para emular um site
- Bibliotecas de teste

Além disso, npm e node é utilizado para gerenciar os pacotes de instalação tanto das próprias ferramentas de Frontend (como React e afins) e gerenciar os seus pacotes.

## Antes do gerenciador de pacote
Antes de existir o gerenciador de pacote NPM, as instalações de bibliotecas eram mais artesanais. Com o exemplo do **JQuery**.

Para utilizar bibliotecas externas, era necessário baixar o código minificado (código compactado) e adicionava em um arquivo `.js` como parte de nosso projeto.

Outra alternativa era acessar a biblioteca a partir de uma `cdn`, que era um link de servidor de conteúdo estático.

Com a vinda no Node, conseguimos, então, centralizar e gerenciar as dependencias de bibliotecas externas através do package.json.

# Outro tema muito importante a ser estudado é o EVENT LOOP e o DENO, que por si só geram conteúdos unicos para serem explicados.