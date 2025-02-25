namespace Desafio.Produtos;

internal class Laptop : Produto
{
    public string Processador { get; set; }

    public override string ExibirInformacoes()
    {
        return $"{base.ExibirInformacoes()} | Processador {Processador}";
    }
}
