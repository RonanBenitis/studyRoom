using ScreenSound04.Modelos;

namespace ScreenSound04.Filtros;

internal class LinqFilter
{
    public static void FiltrarTodosOsGenerosMusicais(List<Musica> musicas)
    {
        var todosOsGenerosMusicais = musicas
            .Select(generos => generos.Genero)
            .Distinct()
            .ToList();

        todosOsGenerosMusicais.ForEach(g => Console.WriteLine($"- {g}"));
    }

    public static void FiltrarArtistasPorGeneroMusical(List<Musica> musicas, string genero)
    {
        var artistasPorGeneroMusical = musicas
            .Where(musica => musica.Genero!.Contains(genero))
            .Select(musica => musica.Artista)
            .Distinct()
            .ToList();

        Console.WriteLine($"Exibindo os artistas por gênero musical >>> {genero}");
        artistasPorGeneroMusical.ForEach(a => Console.WriteLine($"- {a}"));
    }

    public static void FiltrarMusicasDeUmArtista(List<Musica> musicas, string nomeDoArtista)
    {
        var musicasDoArtistas = musicas
            .Where(musica => musica.Artista!.Equals(nomeDoArtista))
            .ToList();

        Console.WriteLine(nomeDoArtista);
        musicasDoArtistas.ForEach(m => Console.WriteLine($"- {m.Nome}"));
    }

    public static void FiltarMusicasPorTonalidade(List<Musica> musicas, int keyId)
    {
        var musicasPorTonalidade = musicas
            .Where(m => m.Key == keyId)
            .ToList();

        Console.WriteLine($"Musicas na tonalidade de {musicasPorTonalidade[0].Tonalidade}");
        musicasPorTonalidade.ForEach(m => Console.WriteLine($"- {m.Nome}"));
    }
}
