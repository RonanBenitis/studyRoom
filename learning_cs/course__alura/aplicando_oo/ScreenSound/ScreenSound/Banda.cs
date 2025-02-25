class Banda
{
    private List<Album> albuns = [];
    public Banda(string nome)
    {
        this.Nome = nome;
    }
    public string Nome { get; }

    public void AddAlbum(Album album)
    {
        albuns.Add(album);
    }

    public void ExibirDiscografia()
    {
        Console.WriteLine($"Discografia da banda {Nome}");
        foreach (Album album in albuns)
        {
            Console.WriteLine($"Álbum: {album.Nome} ({album.DuracaoTotal})");
        }

    }
}