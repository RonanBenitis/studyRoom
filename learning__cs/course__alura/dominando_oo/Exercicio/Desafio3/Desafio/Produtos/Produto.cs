namespace Desafio.Produtos;

internal class Produto
{
    public string Modelo { get; set; }
    public double Preco { get; set; }

    public virtual string ExibirInformacoes()
    {
        // Preço:C = Formatar o número Preço como Currency
        return $"Modelo {Modelo} | Preço {Preco:C}";
    }
}
