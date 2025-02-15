# <span style="color: #87BBA2">===   JAVA: CRIANDO A SUA PRIMEIRA APLICAÇÃO   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">PRIMEIRO PROGRAMA EM JAVA</span>

## PREPARANDO AMBIENTE
Para iniciarmos o desenvolvimento em Java, é necessária a instalação do Kit de desenvolvimento, o JDK (Java Development Kit).

### Onde encontrar?
No site da Oracle, sendo, atualmente, a empresa detentora da tecnologia.

Podemos ir direto na pagina de downloads buscando por "java download oracle"

### JRE ou JDK?
Ao entrar no site da Oracle, nos deparamos com uma quantidade de informações, como JRE, JDK, mas afinal, qual devemos baixar?
- JRE: **Java Runtime Environment**, ou seja, é a tecnologia necessária para rodar uma aplicação Java, o qual conta com a existencia de uma JVM (Java Virtual Machine), o qual fará a tradução do código em bytecode possibilitando ela ser multiplataforma.
  - JRE é recomendado para o **consumidor final**
- JDK: **Java Development Kit**, ou seja, é um conjunto de ferramentas em Java para desenvolvimento de uma aplicação, como compilador, depurador e etc.
  - JDK é o que será utilizado pelos **desenvolvedores**
> O JDK (Java Development Kit) é um conjunto de ferramentas e bibliotecas de software que permite o desenvolvimento de aplicativos Java.

### Escolha do JDK
É ideal escolher a versão do Java que esteja em LTS, ou seja, Long Term Support. Atualmente temos o seguinte informativo:

```plaintext
JDK 23 is the latest release of the Java SE Platform.

JDK 21 is the latest Long-Term Support (LTS) release of the Java SE Platform.

Earlier JDK versions are available below.
```

Ou seja, JDK21 é o LTS, então, optaremos por ele.

### Qual IDE utilizar?
Recomendou-se a utilização de **IntelliJ**, feita pela JetBrains, para o desenvolvimento em Java.

[O download pode ser feito aqui](https://www.jetbrains.com/idea/download/?section=windows)

Utilizaremos a **IntelliJ IDEA Community Edition** por ser Gratuito. A versão Ultimate tem mais funcionalidades mas ela é paga. A Community nos atenderá perfeitamente também.

## O PRIMEIRO PROGRAMA
Agora, para criar o primeiro programa, vamos:
1. Abrir o IntelliJ e clicar em **New Project**
2. Indicar o local que salvaremos o programa
3. Indicaremos a lingua desejada, no caso, Java
4. Indicaremos o sistema de Build, no caso, IntelliJ nesse momento (tem o Maven e o Gradle que é interessante futuramente)
5. JDK a ser utilizado
6. **Create**

### Informações interessantes
- As pastas onde se encontram os projetos geralmente tem como padrão estarem dentro de uma pasta chamada "src", sendo o "código fonte", ou seja, "source code".

## ATALHOS, TEMPLATES, NAVEGAÇÃO (ATÉ O MOMENTO)
**IMPORTANTE:** Os atalhos se alteram conforme o preset que utilizamos. Como instalamos o IntelliJ pegando as configurações do VsCode, importou-se também os atalhos do VsCode (preservando os atalhos unicos do IntelliJ).

Caso queiramos seguir o padrão do IntelliJ, devemos alterar para "Windows" no preset do Keymap. 

### Atalhos
- Alt + 1 (VsCode: CTRL + B para fechar, CTRL + E para abrir): Abre e fecha a aba lateral de projetos (aumenta a tela de código)
- Ctrl + F5: Roda o código
- F5: Roda em debugger
- IMPORTANTE: Alt + Insert sobre um diretório: Mostra a aba "New" com opções pré definidades de criação, como um package (aquele onde deixamos estruturados conforme o endereço de trás para frente o dominínio que estamos trabalhando).
  - Por exemplo, **alt + shift + E** para abrir a aba lateral, **navegue com as setas do teclado**, na pasta desejada dê o comendo **alt + insert**, escreva a letra **P** e aparecerá a função "Pakcage". Crie uma com o nome do dominio de trás pra frente, como "br.com.primeiroprojeto".

### Templates
- `psvm` dentro da classe: Gera a estrutura de public static void main()
- `sout` dentro de um método: Gera um System.out.Print já com o cursor dentro dos parenteses
  - Descrição: Prints a string to System.out

### Navegação
- `alt + Shift + Insert` - Ativa o modo coluna. É possivel ver o modo coluna ativado/desativado no canto inferior direito
  - Com este modo ativado, ao clicar com o mouse e arrastar, podemos selecionar multiplas linhas ao mesmo tempo (inclusive as em branco, como se fossem uma coluna)
  - O mesmo efeito ocorre quando este modo está ativado e clicamos `seta + shift` para cima ou para baixo
- **Importantissimo**: Esse modo é DIFERENTE de fazer `alt + ctrl + shift + seta` para cima ou para baixo. **O funcionamento no IntelliJ é igual ao VsCode**, mas o modo coluna é literalmente uma seleção em coluna vertical, o qual mantém-se vertical mesmo em linhas vazias. O multiseleção com o `alt + ctrl + shift + seta` se reajusta à linhas vazias.

### Shortcut para criar uma classe
- Caso tentarmos instanciar uma classe inexistente, podemos utilizar as **sugestões do IntelliJ** como corta caminho:
  - Primeiro, tentamos instanciar uma classe inexistente, como `new Teste`
  - Clicamos ***alt + enter** e abrirá a tela de sugestões do IntelliJ
  - Selecionamos **Create class 'Teste'**
  - Dado enter, surgirá a opção de criar um pacote para esta classe. Sugerimos dar o nome como algo parecido com `br.com.teste.model`, caso essa classe for um modelo para o sistema. Aí, podemos trocar o ultimo dado (que no caso está como model) dependendo da natureza da classe.

Para conferir dicas para utilização do IntelliJ, [verifique este artigo da Alura.](https://www.alura.com.br/artigos/intellij-idea-dicas-truques-usar-no-dia-a-dia)
- Nosso IntelliJ, por exemplo, pegou as configurações de nosso VsCode, então, ele tem alguns atalhos iguais ao VsCode!
- Outras facilidades, como o "psvm" que gerará a estrutura do "public static void main" automaticamente

### Code Generate
Podemos utilizar o gerador de código que já realiza operações comuns para nós quando o chamamos, como gerar getter e setter de atributos que indicamos.

Para acessar o Generate, clice **Alt + Insert**.

Por exemplo, em uma classe que criamos, podemos clicar **Alt + insert** na linha que queremos gerar este código e, ao selecionar **getter and setter**, indicar as atributos que desejamos e imediatamente esses métodos serão criados.

> Porque utilizamos Getter e Setter?
>
> De acordo com o princípio da orientação a objetos devemos de fato fazer com que os atributos das classes sejam encapsulados (deixá-las private ou protected), evitando o acesso direto. Dessa forma evitamos comportamentos indesejados.

#### Gerando construtores
Podemos gerar um construtor de duas formas:
- Dentro da propria classe, podemos utilizar o Code Generator (`alt + insert`) e indicar quais propriedades gerar o construtor
- Dentro da função que o está instanciando, utilizando a sugestão do IntelliJ (`alt + start / VsCode: ctrl + .`).

```java
// Para realizar a segunda opção, precisamos passar os parametros antes
Estudante joao = new Estudante("joao", 22, 123);
```

#### Gerando o override de toString
Assim como visto no getter e setter, podemos fazer com o caso do toString()
- Override no toString() faz a mesma ação de quando damos instruções ao `__str__` em uma classe Python, que seria alterar o que será retornado ao printar diretamente um objeto.

Para realizar essa ação, utilize a ferramenta de Generate Code (`alt + insert`) e selecione a opção toString().

### Muito e muito mais dicas de IntelliJ
[Para ver mais operações interessantes com IntelliJ, veja este artigo](https://www.alura.com.br/artigos/intellij-idea-dicas-truques-usar-no-dia-a-dia)