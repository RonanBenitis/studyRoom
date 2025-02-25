namespace ScreenSound.Modelos;

internal class Banda : IAvaliavel
{
    private List<Album> _albuns = [];
    private List<Avaliacao> _notas = [];
    public Banda(string nome)
    {
        this.Nome = nome;
    }
    public string Nome { get; }
    public double Media => _notas.Count == 0? 0 : _notas.Average(a => a.Nota);
    public IEnumerable<Album> Albuns => _albuns;

    public void AddAlbum(Album album)
    {
        _albuns.Add(album);
    }

    public void AddNota(Avaliacao nota)
    {
        _notas.Add(nota);
    }

    public void ExibirDiscografia()
    {
        Console.WriteLine($"Discografia da banda {Nome}");
        foreach (Album album in _albuns)
        {
            Console.WriteLine($"Álbum: {album.Nome} ({album.DuracaoTotal})");
        }

    }
}