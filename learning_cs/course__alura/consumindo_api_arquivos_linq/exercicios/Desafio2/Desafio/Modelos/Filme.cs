using System.Text.Json.Serialization;

namespace Desafio.Modelos;

internal class Filme
{
    [JsonPropertyName("title")]
    public string? Titulo { get; set; }
    [JsonPropertyName("year")]
    public string? Ano { get; set; }
    [JsonPropertyName("crew")]
    public string? Elenco { get; set; }
    [JsonPropertyName("imDbRating")]
    public string? Nota { get; set; }
    public string FichaTecnica => $"\n\nTitulo: {Titulo} ({Ano}) - Nota: {Nota}\nElenco: [{Elenco}]\n\n";
}
