namespace Desafio.Produtos;

internal class Smartphone : Produto
{
    public string SistemaOperacional { get; set; }

    public override string ExibirInformacoes()
    {
        return $"{base.ExibirInformacoes()} | SO: {SistemaOperacional}";
    }
}
