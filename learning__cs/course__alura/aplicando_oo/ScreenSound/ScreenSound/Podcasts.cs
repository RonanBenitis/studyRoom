class Podcast
{
    public string Host { get; set; }
    public string Nome { get; set; }
    public List<Episodio> TotalEpisodios { get; }

    public Podcast(string host, string nome)
    {
        Host = host;
        Nome = nome;
        TotalEpisodios = [];
    }

    public void AdicionarEpisodio(string titulo, int numero)
    {
        Episodio episodio = new(titulo, numero);
        TotalEpisodios.Add(episodio);
        Console.WriteLine($"Episodio {episodio.Numero} - {episodio.Titulo} adicionado com sucesso a lista!");
    }

    public void ExibirDetalhes()
    {
        Console.WriteLine($"=== Episódios do podcast de {Nome} | Host: {Host} ===");
        
        if (TotalEpisodios.Count > 0)
        {
            TotalEpisodios.Sort((x, y) => x.Numero.CompareTo(y.Numero));

            foreach (var episodio in TotalEpisodios)
            {
                Console.WriteLine($"{episodio.Numero} - {episodio.Titulo}");
            }
            Console.WriteLine($"Total de episódios: {TotalEpisodios.Count}\n");
        }
        else
        {
            Console.WriteLine("A lista está vazia!");
        }
    }
}