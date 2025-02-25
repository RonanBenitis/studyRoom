using System.Text.Json;

namespace Desafio.Model;

internal class Pessoa
{
    public string? Nome { get; set; }
    public int Idade { get; set; }
    public string? Email { get; set; }
    public string? Detalhes => $"{Nome} | Idade: {Idade} | E-mail: {Email}";
    public Pessoa(string? nome, int idade, string? email)
    {
        Nome = nome;
        Idade = idade;
        Email = email;
    }

    public void Serializar()
    {
        Console.WriteLine($"Serializando as informações de {Nome}");
        string json = JsonSerializer.Serialize(this);
        File.WriteAllText($"{Nome}.json", json);
        Console.WriteLine("Arquivo JSON criado com sucesso!");
    }
}
