class Episodio
{
    public string Titulo { get; set; }
    public int Numero { get; set; }
    public int Duracao { get; set; }
    private List<string> _convidados;
    // Isso é um get-only property
    // Em get-only property, não é aceito bloco de código, apenas valores 
    public string Resumo =>
            $"{Numero} - {Titulo} ({Duracao} minutos)\n" +
            ExibirConvidados();

    public Episodio(string titulo, int numero)
    {
        Titulo = titulo;
        Numero = numero;
        Duracao = 0;
        _convidados = [];
    }

    public void AdicionarConvidado(string convidado)
    {
        _convidados.Add(convidado);
        Console.WriteLine($"Convidado {convidado} adicionado ao episódio {Titulo}!");
    }

    public string ExibirConvidados()
    {
        return _convidados.Count > 0 ?
            $"Convidados: {string.Join(", ", _convidados)}" :
            "Sem convidados.";
    }

}