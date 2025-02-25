using bytebank.Modelos.Conta;
using bytebank_ATENDIMENTO.bytebank.Util;

Console.WriteLine("Boas Vindas ao ByteBank, Atendimento.");

#region Exemplos Arrays em C#
Array amostra = Array.CreateInstance(typeof(double), 5);
amostra.SetValue(5.9, 0);
amostra.SetValue(1.8, 1);
amostra.SetValue(7.1, 2);
amostra.SetValue(10, 3);
amostra.SetValue(6.9, 4);

//TestaMediana(amostra);
//TestaArrayInt();
//TestaBuscarPalavra();
//TestaArrayDeContasCorrentes();
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

    // Exibindo lista
    Console.WriteLine("Exibindo lista:");
    listaDeContas.ExibeLista();

    // Mostrando como recuperar com indice
    // SEM INDEXADOR
    Console.WriteLine("===============================================");
    Console.WriteLine("Recuperando com indice em uma classe padrão:");
    for (int i = 0; i < listaDeContas.Tamanho; i++)
    {
        ContaCorrente conta = listaDeContas.RecuperarContaPorIndice(i);
        Console.WriteLine($"Indice [{i}] = {conta.Conta}/{conta.Numero_agencia}");
    }

    // Mostrando como recuperar com índice
    // COM INDEXADOR
    Console.WriteLine("===============================================");
    Console.WriteLine("Recuperando com indice em uma classe indexável:");
    for (int i = 0; i < listaDeContas.Tamanho; i++)
    {
        ContaCorrente conta = listaDeContas[i];
        Console.WriteLine($"Indice [{i}] = {conta.Conta}/{conta.Numero_agencia}");
    }
}
#endregion

#region Manipulando lista genérica
List<ContaCorrente> _listaDeContas = new()
{
    new ContaCorrente(95){Saldo=100},
    new ContaCorrente(95){Saldo=200},
    new ContaCorrente(95){Saldo=300},
};

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

#endregion

List<ContaCorrente> _listaDeContas2 = new()
{
    new ContaCorrente(874),
    new ContaCorrente(874),
    new ContaCorrente(874),
};

List<ContaCorrente> _listaDeContas3 = new()
{
    new ContaCorrente(951),
    new ContaCorrente(951),
    new ContaCorrente(951),
};

_listaDeContas2.AddRange(_listaDeContas3);

var range = _listaDeContas2.GetRange(0, 2);