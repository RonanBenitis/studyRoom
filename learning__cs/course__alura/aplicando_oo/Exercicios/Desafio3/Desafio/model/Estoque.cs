namespace Desafio.model;

class Estoque
{
    private List<Produto> produtos = [];

    public void Add(Produto produto)
    {
        this.produtos.Add(produto);
        Console.WriteLine($"Produto {produto.Nome} acrescentado com sucesso!");
    }

    public void ShowList()
    {
        Console.WriteLine("=== Lista de produtos ===");
        foreach (Produto produto in this.produtos)
        {
            Console.WriteLine($"Produto: {produto.Nome} | Marca: {produto.Marca}");
        }
        Console.WriteLine($"No total, o estoque possui {this.produtos.Count} itens na lista");
    }
}