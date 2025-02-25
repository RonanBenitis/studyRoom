namespace Desafio.Modelo;

class Artista
{
    public List<Filme> Filmes { get; }
    public string Nome { get; }
    public int Idade { get; }

    // Construtor
    public Artista(string nome, int idade)
    {
        Nome = nome;
        Idade = idade;
        Filmes = [];
    }

    // Métodos
    public void AdicionarFilme(Filme filme)
    {
        Filmes.Add(filme);
        if (!filme.Elenco.Contains(this))
            filme.AdicionarElenco(this);
    }

    public void MostrarFilmes()
    {
        if (Filmes.Count == 0)
        {
            Console.WriteLine($"Nenhum filme encontrado na base para {Nome}");
            return;
        }

        Console.WriteLine($"Filmes de {Nome}...");
        Filmes.ForEach(f => Console.WriteLine($"Filme: {f.Titulo}"));
    }
}