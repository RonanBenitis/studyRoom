using System.Text.Json;
using ScreenSound04.Controlador;
using ScreenSound04.Modelos;

using (HttpClient client = new HttpClient())
{
    try
    {
        string resposta = await client.GetStringAsync("https://guilhermeonrails.github.io/api-csharp-songs/songs.json");

        var musicas = JsonSerializer.Deserialize<List<Musica>>(resposta)!;
        ControladorMusica musicasController = new(musicas);

        int c = 0;
        foreach (var genero in musicasController.Generos)
        {
            Console.WriteLine($"{c} - {genero}");
            c++;
        }

        Console.WriteLine();

        //musicasController.GetArtistasOrdenadoPorNome(descendente: false)
        //    .ForEach(m => Console.WriteLine(m));

        int indiceGenero = 8;
        Console.WriteLine($"=== Musicas do genero {musicasController.Generos.ToList()[indiceGenero]} ===");
        musicasController.GetArtistasByGenero(indiceGenero)
            .ForEach(a => Console.WriteLine(a));

        string artista = "The Offspring";
        Console.WriteLine($"\n=== Musicas de {artista} ===");
        musicasController.GetSongByArtists("The Offspring")
            .ForEach(m => Console.WriteLine(m));

    }
    catch(Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }
}
