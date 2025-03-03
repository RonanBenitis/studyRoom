# <span style="color: #87BBA2">===   APLICANDO A ORIENTAÇÃO A OBJETOS   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)


# <span style="color: #87BBA2">MODELANDO O SCREENMATCH</span>

## UM MODELO PARA REPRESENTAR FILMES
No curso anterior, estávamos falando sobre regras e condicionais. Na hora de montar o Screen Match, a nossa plataforma de streaming, começamos a implementar algumas regras - por exemplo, emitindo uma mensagem se um filme foi lançado a partir de determinada data, ou se está ou não incluído no plano, tudo isso com condicionais.

Mas isso não está muito adequado. E se precisarmos usar isso em outro momento? Teríamos que copiar e colar esse código? É um tipo de programação meio estruturada ou procedural, o que não é muito adequado para modificação. Ao espalhar regras pelo código, tornamos mais difícil fazer manutenção da aplicação ou mesmo entender o que nossa aplicação faz.

### Regras de negócio
As regras sobre como funciona a nossa empresa, por exemplo, no nosso caso:
- Se for assinante recente, tem que pagar
- Caso seja **plus**, não precisa

Pode ser que amanhã mude a regra, as regras de negócio são vivas e passiveis de mudança aolongo do tempo, como foi com a Netflix e a HBO Max, por exemplo:
- Se vai ter ad ou não
- Se vai aceitar família ou não

### Coding smell
Aí que mora o grande problema de se copiar código ao longo do sistema:
- Caso a regra de negócio mude, precisará mudar em todos os lugares aos quais a regra copiada foi realizada

Por exemplo: Caso formos iniciar uma cobrança para os assinantes, mas os assinantes antes de 2011 não serão cobrados, para realizar esse ajuste à nova regra de negócio, precisaremos utilizar o **CTRL + F (O Ctrl + C e Ctrl + V também)** e esse atalho é um bom indicativo que o código não está muito bem escrito em termos de reaproveitamento de código, e a refatoração trará muito mais risco de bug.

Isso mostra que este código está **muito espalhado**, ou seja, ele **não está em uma única capsula, não está ENCAPSULADO**.

### Encapsulamento de objetos
É quando deixamos uma regra de negócio dentro de um único ponto, onde, caso precisarmos realizar alguma manutenção ou refatoração, sabemos que só há um ponto onde ela pode estar.

Isso trata-se de **boas praticas de POO**. Algumas boas praticas a serem seguidas são:
- Clean Code
- DDD (Domain-driven Design)
- Design Patterns
- SOLID

### Soluções de POO
E é por isso que o vem o POO, para solucionar o problema de código espalhado e observar as coisas como se fossem objetos mesmo, centralizado em um ponto.

Objetos tendo caracteristicas, nomes, comportamentos.

### Construindo o sistema focado em POO
Não iniciamos, então, pela construção da classe de entrada (no caso, sendo a `Main`). Já que nosso projeto continuará com a tematica de filmes, a nossa primeira criação será a classe `Filme`.

### Classe
Criamos uma classe chamada `Filme`, e pensando no **Tob Gun** por exemplo, o que a classe seria?
- A Classe especifica o conteúdo de um Objeto

Então, nossa Classe especificará o que um filme tem, qual é a abstração ali.
- Abstração: Caracteristicas em comum de todos os filmes, o que todos os filmes tem.
- Como exemplo: Todo filme tem um nome, e caracteristicas de um objeto nós chamamos de atributo. Logo, todo filme tem um atributo nome.

A sintaxe da declaração de uma classe é diferente do que foi visto até então, por exemplo, a classe de entrada tem um método (comportamento) chamado `main`, com as definições de `public static void`. Em uma classe, estamos iniciando com declarações como `String nome`, isso, na realidade, são atributos.
- Atributos não estáticos são caracteristicas de um objeto, ou seja, nesse caso estamos dizendo que todo Filme terá um nome.


Ou seja, as especificações de uma classe para seus objetos geralmente é exemplificado como a planta de uma casa: A planta da casa dirá o que a casas no geral terão, como quarto, banheiro, cozinha, mas a construção da casa (seu objeto) será distinto. Qual a metragem do banheiro, qual a metragem da cozinha, quantas paredes o quarto terá e em que cor ele será pintado, isso cabe na especificação do objeto.

#### Definindo atributos
```java
public class Filme {
    String nome;
    int anoLancamento;
    boolean incluidoNoPlano;
    double avaliacao;
    int totalDeAvaliacoes;
    int duracaoEmMinutos;
}
```

Estes atributos são os que a instrutora sente que são importantes para filmes, mas, é natural levantarmos isso através de levantamentos de requisitos, é normal, também, revisitar acrescentando ou tirando atribuos.
- Muitas vezes os questionamentos sobre atributos são nada óbvios como "Será uqe a quantidade de avaliações é relavante para o meu sistema ou não?"

Os atributos podem ser infinitos, por isso é importante realizar uma boa abstração e sempre ter em mente **o que o sistema precisa.** Se formos elecar **todos os atributos de um filme** e não apenas os que achamos importantes para o sistema, teremos atributos infinitos. A importância reside nas informaçõas que são necessárias **para o sistema**.

Com isso, nosso modelo de classe está pronto, mas, não é possivel utilizá-lo ainda.

## ATRIBUINDO VALORES AO NOSSO FILME.

### Ponto de entrada
As vezes o projeto pode vir como ponto de entrada o `Main.java`, mas, criaremos nosso ponto de entrada nomeando-o como `Principal.java`.

Ponto de entrada é onde por onde o código iniciará sua execução.

### Declarando 
A ideia é de fato usarmos a nossa classe Filme. Anteriormente, quando queríamos criar uma variável, bastava informar o tipo - por exemplo, int - seguido do nome da variável e o valor que ela receberia.
```java
int valor = 555;
```

Porém, ao criar uma classe Filme, nós também criamos um tipo propriamente nosso. Passaremos esse tipo como qualquer outro, seguido do nome da variável, nesse caso meuFilme.
```java
Filme meuFilme = new Filme();
```

### Tipo referencia
Ao trabalharmos com instanciamento de uma classe, quando a atribuimos em uma variável, ela é um **tipo referencia**, ao contrário dos tipos primitivos que são **atraibuição de valores**.

No caso, ele atribui o endereço da memória onde está alocado o objeto criado.
> Em algum lugar da memória da máquina foi criado um espaço reservado para um objeto chamado Filme
>
> Isto é, um objeto chamado Filme que está na memória e possui um "espaço" para o nome, para o ano de lançamento e cada um daqueles itens que chamamos de atributos

Agora, a variável `meuFilme` carrega o endereço do objeto criado, e, por padrão, quando printamos `meuFilme` será retornado o endereço de onde está armazenado o objeto criado.

### Sintaxe de criar uma instancia
```java
Filme meuFilme = new Filme();
```
- new Filme() = Instanciamento, aqui que criamos o espaço na memória para o objeto
- Filme meuFilme = variável, com o tipo `Filme` que está atribuindo a nova instancia criada, ou seja, fará referencia ao endereço e se comportará como `Filme`, uma vez que a tipamos como `Filme`.
  - Estamos dizendo que `meuFilme`, que tem endereço de uma instancia de Filme, é do tipo `Filme`, ou seja, conseguiremos acessar seus atributos e métodos.

Parte direita está criando mesmo o obejto, parte da esquerda está guardando-a no script.

### Sintaxe (notação) por ponto
Sintaxe muito comum que indica acessar algo de alguém, já observamos este comportamento em `System.out`, o objeto de `Scanner` com o método `.nextLine()`.

### Printando seu nome
Quando printamos o objeto, teremos seu endereço:
```java
System.out.println(meuFilme); // Retorno: Filme@5f184fc6
```

Agora, quando imprimimos uma atributo, como o nome do filme, teremos, respectivamente, o seu nome:

```java
System.out.println(meuFilme.nome); // Retorno: "O Poderoso Chefão";
```

### Sobre classe e objetos
Lembrando que Classe é um arquétipo para os objetos que representará o que todo objeto tem. Por exemplo, não é possivel fazermos isso:
```java
Filme.nome = "Um nome de filme"
```
Isso não é possivel pois a classe `Filme` foi construida sem atributos estáticos, ou seja, a classe em si, como arquétipo, não possui caracteristicas. Mas, a classe descreve atributos não-estaticos, ou seja, atributos que **todas as instancias de objetos terão**.
> Um objeto, é uma instância de uma classe, sendo por meio dele que conseguimos representar informações na aplicação, pois a classe serve apenas para padronizar os objetos, mas não para representar um objeto em si. Para criar um objeto em Java, precisamos utilizar a palavra reservada new seguida do nome da classe e de parênteses vazios. 

```java
// Ação não possível
Filme.nome = "Um nome de filme";

// Ação possivel
Filme filme = new Filme();
filme.nome = "Um nome de filme";
```
Pois, a classe não possui atributo nome, mas a classe **define que TODOS OS OBJETOS terão o atributo nome**. E, atenção a diferençar um `Filme` de um `filme`. Isso já é convenção, onde PascalCase é utilizado apra Classes e camelCase para variáveis, **como objetos**.

## DEFININDO AÇÕES PARA O FILME
A gente já viu o que um filme tem. Agora podemos falar o que um filme faz, o que ele tem de comportamentos ou método. Por exemplo, não precisamos imprimir o nome ou o anoDeLancamento "de fora", podemos pedir que o próprio Filme exiba sua ficha técnica.


### Convenção de nomes de métodos
Há duas grandes vertentes em termos de nomear métodos, há quem nomeie no Imperativo, há quem nomeie no Infitivido
- exibeFichaTecnica (imperativo)
- exibirFichaTecnica (infinitivo)

O mais utilizado, por conveção, é o **imperativo** e é o que utilizaremos.

### exibeFichaTecnica
Agora, passamos o print que estavamos fazendo na main para a responsabilidade da classe:
```java
public class Filme {
    String nome;
    int anoLancamento;
    boolean incluidoNoPlano;
    double avaliacao;
    int totalDeAvaliacoes;
    int duracaoEmMinutos;

    public void exibeFichaTecnica() {
        System.out.println("Nome do filme" + nome);
        System.out.println("Ano do lançamento" + anoLancamento);
    }
}
```
Veja que não estamos indicando `nome` e não `meuFilme.nome`, já que `meuFilme` não existe nesse contexto, e tambem não estamos utilizando `Filme.nome` pois não trata-se de atributo estático.

Quando vamos referenciar um atributo ou método de objeto, geralmente a referenciamos com `this.atributo/método`, como `this.nome`, mas, acredito que agora não seja obrigatório.

A sintaxe de um método é:
- `<visualizacao> <retorno> <nome_do_metodo>(<parametros>) { <bloco_do_código> }`
- Ou seja, `public void exibeFichaTecnica() {}` quer dizer que
  - ele é visivel a todos que o invocar (public),
  - ele retorna nada (pois é void),
  - seu nome é exibeFichaTecnica
  - Ele tem nenhum paremetro: ()
  - Estes são suas instruções {}

**Observação sobre parametros**
- Tanto na declaração quanto na invocação de um método, sempre necessitará de paranteses, mesmo quando vazios.
```java
public class Principal {
    public static void main(String[] args) {
        Filme meuFilme = new Filme();
        meuFilme.nome = "O Poderoso Chefão";
        meuFilme.anoLancamento = 1970;
        meuFilme.duracaoEmMinutos = 180;

        meuFilme.exibeFichaTecnica();
    }
}
```

### avalia(double nota)
```java
public class Filme {
    String nome;
    int anoLancamento;
    boolean incluidoNoPlano;
    double avaliacao;
    int totalDeAvaliacoes;
    int duracaoEmMinutos;

    public void exibeFichaTecnica() {
        System.out.println("Nome do filme" + nome);
        System.out.println("Ano do lançamento" + anoLancamento);
    }

    public void avalia(double nota) {
        this.avaliacao += nota;
        this.totalDeAvaliacoes++;
    }
}
```

Mas, percebemos que faz mais sentido ser chamado de `somaDasAvaliacoes` ao invés de `avaliacao`, então, utilizamos o atalho `SHIFT + F6` para renomear (similar ao F2 no VS Code)

```java
public class Filme {
    String nome;
    int anoLancamento;
    boolean incluidoNoPlano;
    double somaDasAvaliacoes;
    int totalDeAvaliacoes;
    int duracaoEmMinutos;

    public void exibeFichaTecnica() {
        System.out.println("Nome do filme" + nome);
        System.out.println("Ano do lançamento" + anoLancamento);
    }

    public void avalia(double nota) {
        this.somaDasAvaliacoes += nota;
        this.totalDeAvaliacoes++;
    }
}
```

### Refact
Outra alternativa de arrumar o nome dos atributos e variáveis e, automaticamente, aplicar em quem esteja a utilizando, é o `BOTÃO DIREITO+ SEÇÃO REFACT`, lá existem varias opções de refatoração incluindo a de renomear.

### Auto Indent Line
No menu `Code`, podemos utilizar a ferramente `Auto-Indent line` para realizar a indentação automatica, caso precisarmos. Ou o atalho `CTRL + ALT + I`

### Curiosidade: Java como uma das primeiras grandes linguagens
O Java é uma das primeiras grandes linguagens em que os sistemas começaram a envolver grandes grupos de 5, 10 ou 20 pessoas. Até então, antes da década de 90, a maioria absoluta dos sistemas era criada por uma ou duas pessoas desenvolvedoras, e equipes de desenvolvimento eram muito raras.

Quando as equipes começaram a crescer, nasceu a necessidade de escrever código mais legível, com variáveis mais óbvias e de maneira mais elegante, facilitando o trabalho de grandes times em uma mesma base de código. Está aí a importância de boas práticas, nomenclatura e orientação a objetos, e o Java foi a principal linguagem na época a receber esse cuidado. Posteriormente, o .NET e outras linguagens vêm trazer esse propósito de facilitar a complexidade.

# <span style="color: #87BBA2">CONTROLANDO O ACESSO E A ESCRITA NOS DADOS DA APLICAÇÃO</span>

## CONFIGURANDO O QUE PODE SER VISTO E MODIFICADO
Imagina que sou muito fã do "O Poderoso Chefão". Do jeito que está nossa aplicação, é possivel alterar o valor da média diretamente:
```java
meuFilme.somaDasAvaliacoes = 10;
meuFilme.totalDeAvaliacoes = 1;
// A média passará a ser 10
```

### Trocando mensagens entre objetos
Para se comunicar com um objeto, é mais interessante (e seguro) utilizar **métodos**, ao invés de atribuir diretamente no coração do objeto.

> Trocar mensagens com objetos é um termo academico para realizar essas manipulações.

Ou seja, não é uma boa pratica deixar possivel alteração de dados diretamente no coração de um objeto, e sim, utilizar métodos pois assim dá maior controle ao desenvolvedor de como, quando e de que jeito o dado será acessado ou atribuido.

Uma outra analogia é:
- Uma pessoa pedindo dinheiro empresatado para outra, ela não irá pegar diretamente da carteira da outra pessoa mas sim irá pedir emprestado.

### Encapsulamento
Não podemos deixar que acessem os atributos do objetos e alterem a vontande, de forma não prevista pelo desenvolvedor. Encapsulamento é a proteção dos objetos e estruturar como seus dados poderão (e se poderão) ser manipulados.

Outro ponto é: As classes e o código necessitar ser auto explicativo e protegido. Não é legal deixar algo do objeto exposto que não é para ser mexido e pode ser quebrado. Um bom código já protege as partes sensíveis e deixa exposto o que é para estar exposto, deixando tudo que não é exposto não visível. Ou seja, é o principio da **não visibilidade**.

### Modificadores de acesso/visibilidade
Temos palavras chaves para definir como elementos de uma Classe/Objeto podem ser acessados, como `public`, `private` e `protected`.
- `public`: Todos que importaram o módulo poderão acessar estes elementos;
- `private`: Somente a própria Classe ou o Objeto pode utilizar deste elementos, este elementos são manipulados pelo autor e somente pelo autor deste elemento.
- `protected`: Somente a própria Classe e quem a implementa pode utilizar, ou seja, somente o autor e suas filhas podem acessar estes elementos.

### Refatorando
Agora, adicionando `private` no total de notas e na soma de notas, nosso código principal começará a apresentar erro de compilação pois ele não poderá mais acessar os elementos que antes acessava. Para isso, refletiremos os elementos que de fato pode ser interessante para quem consumirá deste objeto e criaremos métodos para buscar este dado.
- Por exemplo, não tem o porque entregarmos a `somaDeNotas`, o que mais irão se interessar é na `mediaDeNotas` e no `totalDeNotas`.

## VISUALIZANDO CARACTERISTICAS PRIVADAS
Da mesma forma que criamos um método para pegar média, faremos um método para pegar atributos privados, também conhecido como **Método Acessor**. A convenção do método acessor é ter em seu nome o termo **Get** e para atribuir valor, ter o termo **Set**, também são conhecido como métodos **getters e setters**.

```java
public int getTotalDeAvaliacoes() {
    return totalDeAvaliacoes;
}
```
- Ao iniciar o método com `get`, o IntelliJ já sugere alguns atributos para realizar o get.

### Utilidade do getter
Por que ter um método que simplesmente devolve o valor de um atributo? Não seria melhor deixar como estava antes de deixar o atributo privado?

Ao longo da formação e da prática diária veremos que esse tipo de lógica começa a esconder o funcionamento interno de uma classe, deixando de expor a nossa aplicação.

O nosso total de avaliações poderia estar em um banco de dados ou ter comunicação com um site parceiro. Além disso, pode acontecer de mudarmos a regra de negócios. Nesse caso, seria necessário procurar (como utilizando CTRL + F) e alterar cada ponto onde o total de avaliações estava sendo acessado.

Conforme vamos desenvolvendo e ganhando experiência em linguagens orientadas a objetos, vamos percebendo cada vez mais vantagens em encapsular a lógica da nossa aplicação.

```java
// Filme.java
public class Filme {
    String nome;
    int anoLancamento;
    boolean incluidoNoPlano;
    private double somaDasAvaliacoes;
    private int totalDeAvaliacoes;
    int duracaoEmMinutos;

    public int getTotalDeAvaliacoes() {
        return totalDeAvaliacoes;
    }

    public void exibeFichaTecnica() {
        System.out.println("Nome do filme" + nome);
        System.out.println("Ano do lançamento" + anoLancamento);
    }

    public void avalia(double nota) {
        this.somaDasAvaliacoes += nota;
        this.totalDeAvaliacoes++;
    }

    public double pegaMedia() {
        return somaDasAvaliacoes / totalDeAvaliacoes;
    }
}

// Principal.java
public class Principal {
    public static void main(String[] args) {
        Filme meuFilme = new Filme();
        meuFilme.nome = "O Poderoso Chefão";
        meuFilme.anoLancamento = 1970;
        meuFilme.duracaoEmMinutos = 180;

        meuFilme.exibeFichaTecnica();
        meuFilme.avalia(8);
        meuFilme.avalia(5);
        meuFilme.avalia(10);
        System.out.println("Total de avaliações: " + meuFilme.getTotalDeAvaliacoes());
        System.out.println(meuFilme.pegaMedia());
    }
}
```

## PARA SABER MAIS: MODIFICADORES DE ACESSO
Em Java, os modificadores de acesso são palavras-chave que definem o nível de visibilidade de classes, atributos e métodos, sendo que eles ajudam a garantir a segurança e encapsulamento do código.

Existem quatro tipos de modificadores de acesso em Java: public, protected, private e default (também conhecido como package-private).

### Public
O modificador de acesso public é o mais permissivo de todos. Uma classe, atributo ou método declarado como public pode ser acessado por qualquer classe em qualquer pacote. Ou seja, ele possui visibilidade pública e pode ser utilizado livremente. Por exemplo:
```java
public class Conta {

  public double saldo;

  public void sacar(double valor) {
    // lógica de saque...
  }
}
```
```java
public class Principal {
    
    public static void main(String[] args) {
        Conta c1 = new Conta();
        c1.saldo = 300;
        c1.sacar(100);
    }

}
```

### Default (Package-private)
O modificador de acesso default é aquele que não especifica nenhum modificador de acesso. Quando nenhum modificador de acesso é especificado, a classe, atributo ou método pode ser acessado apenas pelas classes que estão no mesmo pacote. Por exemplo:
```java
package br.com.alura.conta;

public class Conta {

  default double saldo;

  default void sacar(double valor) {
    // lógica de saque...
  }
}
```
```java
package br.com.alura.testes;

public class Principal {
    
    public static void main(String[] args) {
        Conta c1 = new Conta();
        c1.saldo = 300;
        c1.sacar(100);
    }

}
```

No código anterior, a classe Conta está em um pacote e a classe Principal em outro pacote distinto. A classe Conta pode ser instanciada dentro da classe Principal, pois ela possui o modificador de acesso public, entretanto, o atributo saldo e o método sacar tem o modificador default e, portanto, não podem ser acessados de dentro da classe Principal, o que vai causar um erro de compilação no código anterior.

### Private
O modificador de acesso private é o mais restritivo de todos. Uma classe, atributo ou método declarado como private só pode ser acessado dentro da própria classe. Ou seja, ele possui visibilidade restrita e não pode ser utilizado por outras classes. Por exemplo:
```java
public class Conta {

  private double saldo;

  private void sacar(double valor) {
    // lógica de saque...
  }
}
```
```java
public class Principal {
    
    public static void main(String[] args) {
        Conta c1 = new Conta();
        c1.saldo = 300;
        c1.sacar(100);
    }
}
```
No código anterior, vai ocorrer erro de compilação na classe Principal, pois o atributo saldo e o método sacar foram declarados como private, não podendo com isso serem acessados de fora da própria classe Conta.

Existe ainda um último modificador de acesso, que é o protected, mas falaremos dele mais adiante no curso, após ser apresentado o conceito de herança de classes.