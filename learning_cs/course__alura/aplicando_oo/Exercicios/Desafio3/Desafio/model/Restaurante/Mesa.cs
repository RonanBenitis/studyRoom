namespace Desafio.model.Restaurante;

class Mesa
{
    public int Numero { get; set; }
    public List<Pedido> Pedidos { get; set; } = [];
}