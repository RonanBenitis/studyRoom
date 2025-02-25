namespace Desafio.Armazenamento;

internal class BancoDeDados : IArmazenavel
{
    public string NomeBanco { get; set; }

    public void Recuperar()
    {
        Console.WriteLine($"Recuperando dados do arquivo {NomeBanco}.");
    }

    public void Salvar()
    {
        Console.WriteLine($"Salvando dados no arquivo {NomeBanco}.");
    }
}
