class Album
{
    // Atributos, na notação C#, é chamado de Campo
    private List<Musica> musicas = [];

    // Método construtor
    public Album(string nome)
    {
        Nome = nome;
    }

    // Essas são chamadas de propriedades
    public string Nome { get; }


    public int DuracaoTotal => musicas.Sum(m => m.Duracao);

    // Estabelecendo relação de musicas dentro de albuns
    public void AdicionarMusica(Musica musica)
    {
        musicas.Add(musica);
    }

    public void ExibirMusicas()
    {
        Console.WriteLine($"Lista de músicas do álbum {this.Nome}:\n");
        foreach (var musica in this.musicas)
        {
            Console.WriteLine($"Musica: {musica.Nome}");
        }
        Console.WriteLine($"Este álbum tem {this.DuracaoTotal} segundos");
    }
}