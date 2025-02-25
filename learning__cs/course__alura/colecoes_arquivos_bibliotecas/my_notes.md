# <span style="color: #87BBA2">===   C# e Orientação a Objetos: coleções, arquivos e bibliotecas   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">ARRAY</span>

## PRIMEIRO ARRAY

Queremos calcular média de idades e perceba o seguinte cenário:
```cs
int idade0 = 30;
int idade1 = 40;
int idade2 = 17;
int idade3 = 21;
int idade4 = 18;

int media = (idade0 + idade1 + idade2 + idade3 + idade4) / 5;

Console.WriteLine(media);
```
O resultado da média séra printado, mas veja o trabalho e a repetição de código, não sendo uma solução, também escalável. E se fossem 1000 idades?
- Ideal é ter uma variável que armazene todas as idades

### Utilizando arrays
Variável especial que aceita mais de um valor de mesmo tipo

Sintaxe
```cs
// tipo[] nomeVariavel = new tipo[tamanhoArray]
int[] idades = new int[5];
```
- Lembrando: Utilizamos o new para armazenar uma instancia de um objeto na memória do computador. Ou seja, a variável `idades` é do tipo array de inteiro (`int[]`) e tem como valor uma nova instancia do objeto de array de inteiro `new int[]` com o tamanho de 5 objetos internos `new int[5]`

### Trabalhando com indices
Para trabalhar com arrays, utilizamos os **indices**

**Realizando a mesma estrutura inicial, mas agora com arrays**
```cs
int[] idades = new int[5];
idades[0] = 30;
idades[1] = 40;
idades[2] = 17;
idades[3] = 21;
idades[4] = 18;
```
- Lembrando que o indice inicia com 0

### Printando conteudo de array
Criaremos o método `TestaArrayInt()` para criar a estrutura, dar seu tamanho e printar seu conteudo. Aparentemente, utilizando o método mais braçal:

```cs
TestaArrayInt();

void TestaArrayInt()
{
    int[] idades = new int[5];
    idades[0] = 30;
    idades[1] = 40;
    idades[2] = 17;
    idades[3] = 21;
    idades[4] = 18;

    Console.WriteLine($"Tamanho do Array {idades.Length}");

    for ( int i = 0; i < idades.Length; i++)
    {
        int idade = idades[i];
        Console.WriteLine($"Indice [{i}] = {idade}");
    }
}
```

### Calculando média
Para isso, ainda no modo braçal, criaremos uma variavel externamente chama "acumulador" para armazenar o valor total de nossa array, incrementando o valor a cada repetição:

```cs
TestaArrayInt();

void TestaArrayInt()
{
    int[] idades = new int[5];
    idades[0] = 30;
    idades[1] = 40;
    idades[2] = 17;
    idades[3] = 21;
    idades[4] = 18;

    Console.WriteLine($"Tamanho do Array {idades.Length}");

    int acumulador = 0;
    for ( int i = 0; i < idades.Length; i++)
    {
        int idade = idades[i];
        Console.WriteLine($"Indice [{i}] = {idade}");
        acumulador += idade;
    }

    int media = acumulador / idades.Length;
    Console.WriteLine($"Média de idades = {media}");
}
```

## PERCORRENDO UM ARRAY
Criando o método TestaBuscarPalavra agora, que fará o armazenamento de 5 palavras digitadas por um usuário.

Uma outra estrutura para percorrer uma coleçaõ seria o **foreach**, onde percorre toda a lista indo de item a item. É uma estrutura mais simples e mais legível, ideal para percorrer uma coleção **quando não precisamos da utilização de indices**. Caso o indice que estamos percorrendo é importante, então, utilize o **for**.

```cs
TestaBuscarPalavra();

void TestaBuscarPalavra()
{
    string[] arrayDePalavras = new string[5];

    for (int i = 0; i < arrayDePalavras.Length; i++)
    {
        Console.Write($"Digite {i+1}ª Palavra: ");
        arrayDePalavras[i] = Console.ReadLine();
    }

    Console.Write($"Digite palavra a ser encontrada: ");
    /* 
     * Aqui var será automaticamente atribuido como string
     * pois o retorno de ReadLine é uma string
     */
    var busca = Console.ReadLine();

    foreach (string palavra in arrayDePalavras)
    {
        if (palavra.Equals(busca))
        {
            Console.WriteLine($"Palavra encontrada = {palavra}");
            break; // sai do laço
        }
    }
}
```

## A CLASSE ARRAY
Um outro método para criar array, utilizando diretamente sua classe. Um ponto interessante é que todas as arrays herdam dessa classe, sendo, então `Array` a classe base (ancestral) de todas as arrays.

```cs
// Array nomeVariavel = Array.métodoParaCriarInstancia(tipoDaArray, tamanhoDaArray);
Array amostra = Array.CreateInstance(typeof(double), 5);
// Atribuindo valores ao array
// nomeVariavel.SetValue(valor, indice);
amostra.SetValue(5.9, 0);
amostra.SetValue(1.8, 1);
amostra.SetValue(7.1, 2);
amostra.SetValue(10, 3);
amostra.SetValue(6.9, 4);
```

### Calculando mediana
Mediana indica qual é o valor que está exatamente no meio de um conjunto de dados

```cs
void TestaMediana(Array array)
{
    if((array == null) || (array.Length == 0))
    {
        Console.WriteLine("Array para calculo da mediana está vazio ou nulo");
        return;
    }

    double[] numerosOrdenados = (double[]) array.Clone();
    Array.Sort(numerosOrdenados);

    int tamanho = numerosOrdenados.Length;
    int meio = tamanho / 2;
    double mediana = (tamanho % 2 != 0) ? numerosOrdenados[meio] :
        (numerosOrdenados[meio] + numerosOrdenados[meio - 1]) / 2.0;

    Console.WriteLine($"Com base na amostra a é mediana = {mediana}");
}
```
**Observações:**
- `Array array.Clone:` copia um array evitando referenciamento ao mesmo endereço
  - Acredito que se fizessemos uma atribuição, e não clone, nós atribuiriamos seu endereço e não criaremos um novo elemento, pois, ao criar uma array, atribui-la em outra variável acredito que só apontariamos para o mesmo espaço de memória da array inicialmente criada, por isso a necessidade de Array.Clone
- Método Clone retorna um object
  - Object é a superclasse que todas as classes dotnet derivam
- `(double[]):` Casting explicito, pois o programa não consegue implicitamente usar "casting" entre object e double[]
- `Array.Sort`: Método de classe para ordenar uma coleção

**Lógica da mediana**
- meio = tamanho / 2: Ou seja, se for impar, terá um resultado como 2,5
- mediana com tamanho impar = numerosOrdenados[meio], como o número será truncado, ficará, para um tamanho de array em 5, numerosOrdenados[2], que é justamente o meio
- mediana com tamanho par = Agora faz o calculo da média entre os valores centrais, que é exatamente a mediana da lista

### Equivalencia de construção
A construção com a classe Array e com o tipo array[] é equivalente. Além de, conseguimos também inicializar a array já com valores.

```cs
// Todas funcionam igualmente
double[] amostra = new double[5];

Array amostra = Array.CreateInstance(typeof(double), 5);

Array amostra = new double[5];

// Caso queiramos inicializar já com valores
double[] amostra = { 5.9, 1.8, 7.1, 10, 6.9 }
```

### Atenção com o número de loops

Esse código, looparemos com uma variavel flexível no tamanho desta array
```cs
int[] valores = { 10, 58, 36, 47 };

for (int i = 0; i < valores.Length; i++)
{
    Console.WriteLine(valores[i]);
}
```

Já nesse código, fixamos o número de loops
```cs
int[] valores = { 10, 58, 36, 47 };

for (int i = 0; i < 4; i++)
{
    Console.WriteLine(valores[i]);
}
```
- Aqui que mora a atenção. Caso colocarmos para loopar 5 vezes (mais do que o número de elementos na array), receberemos uma exceção.

# <span style="color: #87BBA2">ARRAY DE CONTAS CORRENTES</span>

## ARRAY DE CONTAS
```cs
void TestaArrayDeContasCorrentes()
{
    ContaCorrente[] listaDeContas = new ContaCorrente[]
    {
        new(874),
        new(874),
        new(874)
    };

    for (int i = 0; i < listaDeContas.Length; i++)
    {
        ContaCorrente contaAtual = listaDeContas[i];
        Console.WriteLine($"Indice {i} - Conta: {contaAtual.Conta}");
    }
}
```

## CLASSE LISTA DE CONTAS
```cs
// Classe ListaDeContasCorrentes
using bytebank.Modelos.Conta;

namespace bytebank_ATENDIMENTO.bytebank.Util;

public class ListaDeContasCorrentes
{
    public ContaCorrente[] itens;
    private int _proximaPosicao = 0;

    /*
     * int tamanhoInicial=5 é um valor defeault, ou seja,
     * se nada for passado no construtor, o valor será 5.
     * Caso for passado um valor diferente, será atribuido o
     * valor diferente
     */
    public ListaDeContasCorrentes(int tamanhoInicial=5)
    {
        itens = new ContaCorrente[tamanhoInicial];
    }

    public void Adicionar(ContaCorrente item)
    {
        Console.WriteLine($"Adicionando item na posição {_proximaPosicao}");
        itens[_proximaPosicao] = item;
        _proximaPosicao++;
    }
}
```

### Reestruturando Program.cs
```cs
void TestaArrayDeContasCorrentes()
{
    ListaDeContasCorrentes listaDeContas = new();
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    
    foreach (ContaCorrente conta in listaDeContas.itens)
    {
        Console.WriteLine(conta.Conta);
    }
}
```
- Percebemos que funciona normalmente com 3 valores. Mas e se passarmos mais do que 5 valores sem indicar um número máximo no construtor?
  - Recebemos um `Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.`

### Resolvendo problema de IndexOutOfRangeException
Para isso, criaremos um método que verifica e acrescenta mais capacidade à array caso note que o número de adições superará o limite da array, tornando-a mais flexivel. Ou seja, percebeu que tá vindo um elemento acima em um indice acima do tamanho maximo da array?
- Cria uma nova array
- Passa-se os valores da array antiga para a nova
- Substitui o caminho da array antiga pela nova. E por assim vai a cada iteração
```cs
public class ListaDeContasCorrentes
{
    public ContaCorrente[] itens;
    private int _proximaPosicao = 0;

    public ListaDeContasCorrentes(int tamanhoInicial=5)
    {
        itens = new ContaCorrente[tamanhoInicial];
    }

    public void Adicionar(ContaCorrente item)
    {
        Console.WriteLine($"Adicionando item na posição {_proximaPosicao}");
        VerificarCapacidade(_proximaPosicao + 1);
        itens[_proximaPosicao] = item;
        _proximaPosicao++;
    }

    private void VerificarCapacidade(int tamanhoNecessario)
    {
        if (itens.Length >= tamanhoNecessario)
        {
            return;
        }
        else
        {
            Console.WriteLine("Aumentando a capacidade da lista!");
            ContaCorrente[] novoArray = new ContaCorrente[tamanhoNecessario];

            // Coletando os valores do array antigo para o novo array
            for (int i = 0; i < itens.Length; i++)
            {
                novoArray[i] = itens[i];
            }

            itens = novoArray;
        }
    }
}
```

## REMOVENDO ITENS

### Método Remover
Método para remover conta de um objeto de ListaDeContasCorrentes
```cs
    public void Remover (ContaCorrente conta)
    {
        int indiceItem = -1; // Apenas para incializar

        /*
         * DESCRIÇÃO
         * Identifica indice da conta desejada
         * 
         * EXEMPLO
         * Suponhamos que nossa array está da seguinte forma
         * [conta1] [conta2] [conta3] [conta4] [conta5]
         * 
         * Suponhamos que passamos no parametro a conta3
         */
        for (int i = 0; i < _proximaPosicao; i++)
        {
            ContaCorrente contaAtual = itens[i];

            if (contaAtual == conta)
            {
                indiceItem = i;
                break;
            }
        }

        // A saída será i = 2 (pois é o indice 2)

        /*
         * DESCRIÇÃO
         * Substitui o valor atual do indice encontrado pelo indice
         * seguinte, e assim suscetivamente
         * 
         * EXEMPLO
         * Os valores estão da seguinte forma
         * itens = [conta1] [conta2] [conta3] [conta4] [conta5]
         * indiceItem = 2
         */
        for (int i = indiceItem; i < _proximaPosicao - 1; i++)
        {
            itens[i] = itens[i + 1];
        }

        /*
         * A saida será:
         * itens = [conta1] [conta2] [conta4] [conta5] [conta5]
         */

        /*
         * DESCRIÇÃO
         * Decremento, para reduzir uma posição
         */
        _proximaPosicao--;

        /*
         * DESCRIÇÃO
         * Limpa a ultima posição, sendo que já movemos os valores desejados
         * uma indice para trás
         * 
         * EXEMPLO:
         * itens = [conta1] [conta2] [conta4] [conta5] [conta5]
         */
        itens[_proximaPosicao] = null;

        /*
         * A saida será:
         * itens = [conta1] [conta2] [conta4] [conta5] [null]
         */
    }
```

### Método ExibirLista
Método para ExibirLista de um objeto de ListaDeContaCorrentes:
```cs
public void ExibeLista()
{
    if (_proximaPosicao == 0)
    {
        Console.WriteLine("Lista vazia!");
        return;
    }

    for (int i = 0; i < _proximaPosicao; i++)
    {
        var conta = itens[i];
        Console.WriteLine($"Indice[{i}] = Conta:{conta.Conta} - Nº da Agencia: {conta.Numero_agencia}");
    }
}
```

### Chamada no Program.cs
```cs
TestaArrayDeContasCorrentes();

void TestaArrayDeContasCorrentes()
{
    ListaDeContasCorrentes listaDeContas = new();
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));
    listaDeContas.Adicionar(new ContaCorrente(874));

    var contaNova = new ContaCorrente(963);
    listaDeContas.Adicionar(contaNova);

    listaDeContas.Remover(listaDeContas.itens[2]);

    listaDeContas.ExibeLista();
}
```

## INDEXADORES
Agora, aprenderemos a configurar uma classe em uma **classe indexável**.

Inicialmente, criamos um método que permite validar e acessar itens ao passarmos um indice, observe:
```cs
// No LisaDeContasCorrentes.cs
public ContaCorrente RecuperarContaPorIndice(int indice)
{
    if(indice < 0 || indice >= _proximaPosicao)
    {
        throw new ArgumentOutOfRangeException(nameof(indice));
    }

    return itens[indice];
}

// No Program.cs
// Recuperando e mostrando conta
Console.WriteLine("Recuperando com indice:");
for (int i = 0; i < listaDeContas.Tamanho; i++)
{
    ContaCorrente conta = listaDeContas.RecuperarContaPorIndice(i);
    Console.WriteLine($"Indice [{i}] = {conta.Conta}/{conta.Numero_agencia}");
}
```

Apesar de estarmos recuperando o elemento, não temos ainda uma **classe indexável**, ou seja, que não necessite de um método explicito para recuperação de seus dados internos. Queremos chegar em um ponto que ao chamarmos `listaDeContas[1]` acessemos o primeiro elemento da lista, sem precisar acessar sua lista interna ou criar m método para isso.

## ARRAYLIST
Para enveloparmos o nosso código de teste para deixar o `Program.cs` mais légivel, utilizamos a função da IDE chamada `region`.
- No inicio do trecho a ser envelopado, colocamos:
  - `#region nome_da_region_caso_queira_colocar_algo`
- No fim do trecho a ser envelopado, colocamos:
  - `#endregion`

Com isso, habilitará a opção de colapsar e exibir o código envelopado. Mas, importante:
- Apesar de envelopado, quando rodarmos a aplicação, esse código ainda é considerado
- O nome que escolhemos para region, caso escolhemos algum, substituirá o termo `#region` quando trecho colapsado.

### Utilizando ArrayList
No DotNet existem bibliotecas nativas para vincular coleções de objetos. Uma delas é o `ArrayList`, o qual disponibiliza por padrão métodos para manipulação de listas (como adicionar, remover, consultar), sem a necessidade de criarmos estes métodos.

No caso, agora, para adicionarmos um elemento em uma lista do tipo `ArrayList` é só chamarmos seu método `Add()`, passando o elemento a ser adicionado

```cs
// Instanciando nova ArrayList
ArrayList _listaDeContas = new();
```

### Estrutura do código neste momento
- Note que criamos um loop onde só saimos de `AtendimentoCliente` caso opcao for diferente de `6`

```cs
ArrayList _listaDeContas = new();

AtendimentoCliente();

void AtendimentoCliente()
{
    char opcao = '0'; // Variável de controle

    // Note que configuramos um loop, onde a aplicação só para
    // se a opção é 6
    while (opcao!='6')
    {
        Console.WriteLine("=============================");
        Console.WriteLine("===      Atendimento      ===");
        Console.WriteLine("=== 1 - Cadastrar Conta   ===");
        Console.WriteLine("=== 2 - Listar Contas     ===");
        Console.WriteLine("=== 3 - Remover Conta     ===");
        Console.WriteLine("=== 4 - Ordenar Contas    ===");
        Console.WriteLine("=== 5 - Pesquisar Conta   ===");
        Console.WriteLine("=== 6 - Sair do Sistema   ===");
        Console.WriteLine("=============================");
        Console.WriteLine("\n\n");
        Console.Write("Digite a opção desejada: ");
        
        // Console.ReadLine retorna string, que é um array de caracteres
        // Por isso pegamos seu primeiro valor, pois ele virá como string
        opcao = Console.ReadLine()[0];

        switch (opcao)
        {
            case '1':
                CadastarConta();
                break;
            case '2':
                ListarContas();
                break;
            case '6':
                Console.WriteLine("Encerrando aplicação. Até logo!");
                break;
            default:
                Console.WriteLine("Opção não implementada.");
                break;

        }
    }
}
void CadastarConta()
{
    Console.Clear();
    Console.WriteLine("==============================");
    Console.WriteLine("===   CADASTRO DE CONTAS   ===");
    Console.WriteLine("==============================");
    Console.WriteLine("\n");
    Console.WriteLine("=== Informe dados da conta ===");
    Console.Write("Numero da conta: ");
    string numeroConta = Console.ReadLine();

    Console.Write("Número de Agência: ");
    int numeroAgencia = int.Parse(Console.ReadLine());

    ContaCorrente conta = new(numeroAgencia);

    Console.Write("Informe o saldo inicial: ");
    conta.Saldo = double.Parse(Console.ReadLine());

    Console.Write("Informe nome do Titular: ");
    conta.Titular.Nome = Console.ReadLine();

    Console.Write("Informe CPF do Titular: ");
    conta.Titular.Cpf = Console.ReadLine();

    Console.Write("Informe Profissão do Titular: ");
    conta.Titular.Profissao = Console.ReadLine();

    _listaDeContas.Add(conta);
    Console.WriteLine("... Conta cadastrada com sucesso! ...");
    Console.ReadKey();
}
void ListarContas()
{
    Console.Clear();
    Console.WriteLine("=============================");
    Console.WriteLine("===    LISTA DE CONTAS    ===");
    Console.WriteLine("=============================");
    Console.WriteLine("\n");

    if(_listaDeContas.Count <= 0)
    {
        Console.WriteLine("... Não há contas cadastradas! ...");
        Console.ReadKey();
        return;
    }

    foreach (ContaCorrente conta in _listaDeContas)
    {
        Console.WriteLine("=== Dados da Conta ===");
        Console.WriteLine($"Numero da Conta: {conta.Conta}");
        Console.WriteLine($"Saldo da Conta: {conta.Saldo}");
        Console.WriteLine($"Titular da Conta: {conta.Titular.Nome}");
        Console.WriteLine($"CPF do Titular: {conta.Titular.Cpf}");
        Console.WriteLine($"Profissão do Titular: {conta.Titular.Profissao}");
        Console.WriteLine($">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Console.ReadKey();
    }
}
```

### Mais sobre ArrayList
A classe de biblioteca do .NET ArrayList é uma implementação evoluída de um array, a classe ArrayList faz parte do namespace System.Collections, e dentre as características desta classe temos:

- A possibilidade de expandir seus limites por meio da propriedade Capacity.
- A classe Array já disponibiliza operações de adição, inserção e exclusão de elementos.
- Como os arrays também tem disponível os métodos de ordenação de elementos Sort e de inversão da ordem por meio do Reverse.

Uma característica importante da classe ArrayList é a possibilidade de se adicionar qualquer tipo de elemento, uma vez que ela trabalha com tipo da superclasse object da qual todos os tipos do C# derivam.

Para saber mais sobre as possibilidade de utilização e métodos da classe ArrayList deixamos a recomendação de acesso a documentação da Microsoft [ArrayList Classe](https://learn.microsoft.com/pt-br/dotnet/api/system.collections.arraylist?view=net-6.0).

# <span style="color: #87BBA2">LISTT</span>

## GENERIC E LIST
Iniciamos a seção definindo elementos de inicialização de `_listaDeContas`
```cs
ArrayList _listaDeContas = new()
{
    new ContaCorrente(95){Saldo=100},
    new ContaCorrente(95){Saldo=200},
    new ContaCorrente(95){Saldo=300},
};
```
- Um ponto muito interessante é o `{Saldo=100}`, perceba que estamos instanciando uma `ArrayList` inicializada com 3 itens, e cada um destes itens terão a propriedade Saldo inicializadas com os valores definidos.
  - Ou seja, estamos definindo um método de inicialização dentro de uma inicialização

### _listaDeContas tendo mais do que contas
Simulamos um bug ao acrescentar um comando de adição para acrescentar a seguinte informação:
```cs
// No método CadastrarConta
_listaDeContas.Add(conta);
_listaDeContas.Add("Hello World!");
```

O que acontece:
- Cada vez que cadastrarmos uma conta, a string `"Hello World"` também será cadastrada
- Quando formos listar as contas com o nosso `foreach(ContaCorrente conta in _listaDeContas)` receberemos uma exceção, pois, quando chegar no valor que é uma string, o sistema indicará que "não consegue converter uma string em ContaCorrente".
  - Além de estarmos acessando elementos internos de um objeto de ContaCorrente.

Ou seja:
- **ArrayList é uma lista que aceita multiplos tipos em uma mesma lista**
- Vemos esse comportamento no método **Add**, já que o método Add de ArrayList pede como um parametro um valor do tipo **object**, ou seja, a **superclasse de todos os tipos**, indicando que **ArrayList aceita adicionar qualquer tipo em uma mesma lista**

### Classe genérica
Em C#, generics (genéricos) são um recurso que permite a criação de classes, métodos, interfaces e delegados que trabalham com tipos de dados especificados apenas no momento de uso.

Uma classe genérica é justamente a que utiliza desta ferramenta, passando o tipo desejado entre as chaves da chamada dessa classe. Ou seja, uma classe generica é aquela que pede o tipo desejado entre sinais de maior e menor, realizando o comportamento específico a este tipo sem a necessidade de casting

Exemplo:
- Criamos uma classe genérica chamada `Caixa`
  - `public class Caixa<T>`
  - O `<T>` significa que pedirá um tipo específico na hora de sua chamada. A classe é chamada genérica pois só terá uma ação específica no momento de sua chamada.
- Nesta classe, existem métodos como Guardar e Pegar
- Queremos, então, ter uma caixa de apenas valores inteiros e guardar o número 5
  - `Caixa<int> caixaDeInteiros = new();`
  - `caixaDeInteiros.Guardar(5);`
- Agora, fazendo o mesmo para strings
  - `Caixa<string> caixaDeTexto = new();`
  - `caixaDeTexto.Guardar("Hello World!")`
- Se tentarmos guardar uma string em uma caixaDeInteiros ou o contrário, o sistema retornará erro.


### Usando List, uma classe genérica
Ajustando nossa _listaDeContas:
```cs
List<ContaCorrente> _listaDeContas = new()
{
    new ContaCorrente(95){Saldo=100},
    new ContaCorrente(95){Saldo=200},
    new ContaCorrente(95){Saldo=300},
};
```
- Agora, conseguimos garantir que **todos os itens desta lista são ContaCorrente**
- Agora, se deixarmos o mouse sob o método **Add** do objeto **_listaDeContas**, onde antes aparecia aceitar parametros do tipo **object**, agora mostra que aceita parametros do tipo **ContaCorrente**

## MÉTODOS DISPONÍVEIS

### AddRange
Adiciona os elementos de uma lista no final de outra lista

Exemplo:
- Suponhamos que Lista2 tem 3 elementos e Lista1 tem 3 elementos
- Damos o comando `Lista2.AddRange(Lista1)`
- Lista2 passará a ter 6 elementos com os 3 ultimos elementos sendo correspondentes a Lista1

### GetRange
Cria uma nova lista com o recorte desejado

Exemplo:
- Suponhamos que Lista1 tem 3 elementos
- Lista1.Range(indiceInicio, contagemElementos)
- `var range = Lista1.Range(0, 2)`
- range tornar-se-á uma Lista com 2 elementos iniciando do indice 0 da Lista1, ou seja, o elemento de indice 0 e 1.
- range será uma Lista Genérica de mesmo tipo da lista que se está copiando, ou seja, se Lista1 é um List<int>, range será um List<int> também.

### Reverse
Inverte a ordem da lista
- Suponhamos que Lista1 está em ordem alfabética
- Damos o comando Lista1.Reverse
- List1 passará a ter a ordem alfabética invertida

### Clear
Limpa completamente a lista desejada
- Suponhamos que Lista1 tem 3 elementos
- Damos o comando `Lista1.Clear`
- Lista1 passará a ter 0 elementos

# <span style="color: #87BBA2">MANIPULANDO A LISTA</span>

# <span style="color: #87BBA2">LINQ</span>
