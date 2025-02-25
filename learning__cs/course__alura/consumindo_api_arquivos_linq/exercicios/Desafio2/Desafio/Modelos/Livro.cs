using System.Text.Json.Serialization;

namespace Desafio.Modelos;

internal class Livro
{
    [JsonPropertyName("titulo")]
    public string? Titulo { get; set; }
    [JsonPropertyName("autor")]
    public string? Autor { get; set; }
    [JsonPropertyName("ano_publicacao")]
    public int? Ano { get; set; }
    [JsonPropertyName("genero")]
    public string? Genero { get; set; }

    public string FichaTecnica => $"Titulo: {Titulo}\nAutor: {Autor}\nAno: {Ano}\nGenero: {Genero}\n\n";
}
