namespace Desafio.model.Jogos;

class Catalogo
{
    private List<Jogo> Jogos { get; set; }

    public bool CatalogoVazio => Jogos.Count == 0;
    public Catalogo()
    {
        Jogos = [];
    }
    public void AddGame(string nome, string genero, string desenvolvedora)
    {
        Jogo jogo = new(nome, genero, desenvolvedora);
        Jogos.Add(jogo);
        // \" para possibilitar aspas
        Console.WriteLine($"Jogo \"{nome}\" adicionado ao catalogo");
    }

    public void ShowCatalog()
    {
        if(CatalogoVazio)
        {
            Console.WriteLine("O catálogo de jogos está vazio.");
        }
        else
        {
            Console.WriteLine($"=== Catalogo de jogos ===");
            foreach (Jogo jogo in Jogos)
            {
                Console.WriteLine($"Jogo: {jogo.Nome} | Genero: {jogo.Genero} | Dev: {jogo.Desenvolvedora}");
            }
        }
    }
}