using System.Reflection.Metadata.Ecma335;
using System.Text.Json.Serialization;

namespace ScreenSound04.Modelos;

internal class Musica
{
    private readonly string[] _tonalidades = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A%", "B" ];
    
    [JsonPropertyName("song")]
    public string? Nome { get; set; }

    [JsonPropertyName("artist")]
    public string? Artista { get; set; }

    [JsonPropertyName("duration_ms")]
    public int Duracao { get; set; }

    [JsonPropertyName("genre")]
    public string? Genero { get; set; }

    [JsonPropertyName("key")]
    public int Key { get; set; }
    public string? Tonalidade => _tonalidades[Key];

    public void ExibirDetalhesDaMusica()
    {
        Console.WriteLine($"Artista: {Artista}");
        Console.WriteLine($"Musica: {Nome}");
        Console.WriteLine($"Duração em segundos: {Duracao / 100}");
        Console.WriteLine($"Gênero Musical: {Genero}");
        Console.WriteLine($"Tonalidade: {Tonalidade}");
    }
}
