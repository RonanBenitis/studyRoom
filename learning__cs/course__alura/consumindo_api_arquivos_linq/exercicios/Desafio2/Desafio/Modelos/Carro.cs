using System.Text.Json.Serialization;

namespace Desafio.Modelos;

internal class Carro
{
    [JsonPropertyName("marca")]
    public string? Marca { get; set; }
    [JsonPropertyName("modelo")]
    public string? Modelo { get; set; }
    [JsonPropertyName("ano")]
    public int? Ano { get; set; }
    [JsonPropertyName("tipo")]
    public string? Tipo { get; set; }

    public string Informacoes => $"Carro {Marca} {Modelo} {Ano} {Tipo}";
}
