namespace Desafio.model.Jogos;

class Jogo
{
    public Jogo(string nome, string genero, string desenvolvedora)
    {
        Nome = nome;
        Genero = genero;
        Desenvolvedora = desenvolvedora;
    }

    public string Nome { get; set; }
    public string Genero { get; set; }
    public string Desenvolvedora { get; set; }
}