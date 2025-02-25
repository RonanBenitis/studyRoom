using ScreenSound04.Modelos;

namespace ScreenSound04.Controlador;

internal class ControladorMusica
{
    private List<string> _generos = [];
    private List<string> _artistas = [];
    public IEnumerable<Musica> Musicas { get; }

    public IEnumerable<string> Generos => _generos;
    public IEnumerable<string> Artistas => _artistas;

    public ControladorMusica (List<Musica> musicas)
    {
        Musicas = musicas;

        musicas.ForEach(m =>
        {
            string[] generoSplit = m.Genero!.Split(",")
                                            .Select(n => n.Trim())
                                            .ToArray();

            foreach (string genero in generoSplit)
            {
                if (!_generos.Contains(genero))
                    _generos.Add(genero);
            }

            if (!_artistas.Contains(m.Artista!))
                _artistas.Add(m.Artista!);
        });
    }

    public List<string> GetArtistasOrdenadoPorNome(bool descendente)
    {
        List<string> artistasOrdenado = descendente == false ?
            _artistas.OrderBy(a => a).ToList() :
            _artistas.OrderByDescending(a => a).ToList();

        return artistasOrdenado;
    }

    public List<string> GetArtistasByGenero(int indiceGenero)
    {
        if (indiceGenero < 0 || indiceGenero >= _generos.Count)
            throw new ArgumentOutOfRangeException(nameof(indiceGenero), "Índice inválido!");

        // Filtrando musicas por gênero
        List<Musica> musicasFiltradas = Musicas
            .Where(m => m.Genero != null && m.Genero.Contains(_generos[indiceGenero]))
            .ToList();

        // Pegando artistas com LINQ (mais eficiente que foreach)
        List<string> artistasFiltrados = musicasFiltradas
            .Select(m => m.Artista) // Seleciona artistas
            .Where(a => a != null)  // Garante que não tenha nulo
            .Select(a => a!)        // Usa o operador '!' para garantir que não seja null
            .Distinct()             // Remove duplicatas
            .ToList();              // Transforma em lista

        return artistasFiltrados;
    }

    public List<string> GetSongByArtists(string artista)
    {
        // Filtrando musicas por gênero
        List<Musica> musicasFiltradas = Musicas
            .Where(m => m.Artista != null && m.Artista.Contains(artista))
            .ToList();

        if (musicasFiltradas.Count == 0)
            throw new ArgumentException("Artista não encontrado", nameof(artista));

        // Pegando nome da musica com LINQ (mais eficiente que foreach)
        List<string> musicasDoArtista = musicasFiltradas
            .Select(m => m.Nome)
            .Where(m => m != null)
            .Select(m => m!)
            .ToList();

        return musicasDoArtista;
    }

}
