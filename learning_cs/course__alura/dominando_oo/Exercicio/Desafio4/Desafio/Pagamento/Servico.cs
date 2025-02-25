namespace Desafio.Pagamento;

internal class Servico : IPagavel
{
    public string Nome { get; set; }
    public int HorasTrabalhadas { get; set; }
    public decimal TaxaHoraria { get; set; }

    public decimal CalcularPagamento()
    {
        return HorasTrabalhadas * TaxaHoraria;
    }
}
