using System.Text.Json.Serialization;

namespace Desafio.Modelos;

internal class Pais
{
    [JsonPropertyName("nome")]
    public string? Nome { get; set; }
    [JsonPropertyName("capital")]
    public string? Capital { get; set; }
    [JsonPropertyName("populacao")]
    public int? Populacao { get; set; }
    [JsonPropertyName("continente")]
    public string? Continente { get; set; }
    [JsonPropertyName("idioma")]
    public string? Idioma { get; set; }
    public string Informacoes => $"Pais: {Nome} - Capital: {Capital} - Populacao: {Populacao}";
}
