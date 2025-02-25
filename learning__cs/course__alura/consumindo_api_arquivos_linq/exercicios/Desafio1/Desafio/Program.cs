// Consumindo API cheapshark
using (HttpClient client = new())
{
    try
    {
        string resposta = await client.GetStringAsync("https://www.cheapshark.com/api/1.0/deals");

        Console.WriteLine(resposta);
    }
    catch(Exception ex)
    {
        Console.WriteLine($"Erro inesperado: {ex}");
    }
}

// Exercicio 2
try
{
    Console.Write("Digite o numerador: ");
    int numerador = int.Parse(Console.ReadLine());

    Console.Write("Digite o denominador: ");
    int denominador = int.Parse(Console.ReadLine());

    int resultado = numerador / denominador;
    Console.WriteLine($"Resultado: {resultado}");
}
catch (DivideByZeroException ex)
{
    Console.WriteLine($"Erro: na matemática não é permitida a divisão por 0.");
}

// Exercicio 3
try
{
    List<int> numeros = new List<int> { 1, 2, 3 };
    Console.WriteLine($"Elemento no índice 5: {numeros[5]}");
}
catch (ArgumentOutOfRangeException ex)
{
    Console.WriteLine($"Erro: {ex.Message}");
}

// Exercicio 4
try
{
    MinhaClasse objetoNulo = null;
    objetoNulo.Meumetodo();
}
catch (NullReferenceException ex)
{
    Console.WriteLine($"Erro: {ex.Message}");
}