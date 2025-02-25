namespace Desafio.Pagamento;

internal class Produto : IPagavel
{
    public string Nome { get; set; }
    public int Quantidade { get; set; }
    public decimal Preco { get; set; }

    public decimal CalcularPagamento()
    {
        return Quantidade * Preco;
    }
}
