namespace Desafio.Modelo;

class Filme
{
    public List<Artista> Elenco { get; }
    public string Titulo { get; }
    public int Duracao { get; }

    // Construtor
    public Filme(string titulo, int duracao, List<Artista>? elenco = null)
    {
        Titulo = titulo;
        Duracao = duracao;
        Elenco = elenco ?? [];
        // Se a lista for vazia, não inicia ForEach
        // this = instancia atual da classe Filme, ou seja, o objeto
        Elenco.ForEach(a => a.AdicionarFilme(this));
    }

    // Métodos
    public void AdicionarElenco(Artista artista)
    {
        Elenco.Add(artista);

        if (!artista.Filmes.Contains(this))
            artista.AdicionarFilme(this);

        Console.WriteLine($"{artista.Nome} adicionado/a ao elenco.");
    }

    public void ListarElenco()
    {
        if (Elenco.Count == 0)
        {
            Console.WriteLine("Elenco vazio.");
        }
        else
        {
            Console.WriteLine("Elenco... ");
            Elenco.ForEach(a => Console.WriteLine(a.Nome));
        }
    }
}