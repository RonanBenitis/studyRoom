using Desafio.Model;
using System.Text.Json;

// Exercicio 1
Pessoa gilmar = new("Gilmar", 52, "gilmar@hotmail.com");
gilmar.Serializar();

// Exercicio 2
string jsonContent = File.ReadAllText($"{gilmar.Nome}.json");
Pessoa jsonDesserializado = JsonSerializer.Deserialize<Pessoa>(jsonContent)!;

Console.WriteLine(jsonDesserializado.Detalhes);

// Exercicio 3
List<Pessoa> listaPessoas =
[
    new("Fulano1", 31, "fulano1@hotmail.com"),
    new("Fulano2", 32, "fulano2@hotmail.com"),
    new("Fulano3", 33, "fulano3@hotmail.com"),
    new("Fulano4", 34, "fulano4@hotmail.com"),
    new("Fulano5", 35, "fulano5@hotmail.com"),
];

string json = JsonSerializer.Serialize(listaPessoas);
File.WriteAllText("lista_pessoas.json", json);

// Exercicio 4
string jsonContentList = File.ReadAllText("lista_pessoas.json");
var jsonListDesserializado = JsonSerializer.Deserialize<List<Pessoa>>(jsonContentList)!;

Console.WriteLine();
jsonListDesserializado.ForEach(p => Console.WriteLine(p.Detalhes));

// Exercicio 5
Console.WriteLine("\nInforme a idade para pesquisa");
int idade = int.Parse(Console.ReadLine()!);

var listFilter = jsonListDesserializado
    .Where(p => p.Idade == idade)
    .ToList();

if (listFilter.Count != 0)
{
    listFilter.ForEach(p => Console.WriteLine($"{p.Nome} tem essa idade"));
} else
{
    Console.WriteLine("Nenhuma pessoa com esta idade encontrada na lista");
}