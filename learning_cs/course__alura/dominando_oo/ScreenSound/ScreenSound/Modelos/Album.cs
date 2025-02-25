namespace ScreenSound.Modelos;

internal class Album : IAvaliavel
{
    // Atributos, na notação C#, é chamado de Campo
    private List<Musica> _musicas = [];
    private List<Avaliacao> _notas = [];

    // Método construtor
    public Album(string nome)
    {
        Nome = nome;
    }

    // Essas são chamadas de propriedades
    public string Nome { get; }


    public int DuracaoTotal => _musicas.Sum(m => m.Duracao);
    public IEnumerable<Musica> Musicas => _musicas;

    public double Media => _notas.Count == 0 ? 0 : _notas.Average(a => a.Nota);

    public void AddNota(Avaliacao nota)
    {
        _notas.Add(nota);
    }

    // Estabelecendo relação de musicas dentro de albuns
    public void AdicionarMusica(Musica musica)
    {
        _musicas.Add(musica);
    }

    public void ExibirMusicas()
    {
        Console.WriteLine($"Lista de músicas do álbum {this.Nome}:\n");
        foreach (var musica in this._musicas)
        {
            Console.WriteLine($"Musica: {musica.Nome}");
        }
        Console.WriteLine($"Este álbum tem {this.DuracaoTotal} segundos");
    }
}