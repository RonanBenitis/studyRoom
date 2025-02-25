namespace Desafio.Armazenamento;

internal class Arquivo : IArmazenavel
{
    public string NomeArquivo { get; set; }

    public void Recuperar()
    {
        Console.WriteLine($"Recuperando dados do arquivo {NomeArquivo}.");
    }

    public void Salvar()
    {
        Console.WriteLine($"Salvando dados no arquivo {NomeArquivo}.");
    }
}
