namespace Desafio.Produtos;

internal class Table : Produto
{
    public string TipoTela { get; set; }

    public override string ExibirInformacoes()
    {
        return $"{base.ExibirInformacoes()} | Tela: {TipoTela}";
    }
}
