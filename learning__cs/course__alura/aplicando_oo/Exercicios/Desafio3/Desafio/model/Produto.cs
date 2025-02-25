namespace Desafio.model
{
    class Produto
    {
        private double _preco;
        private int _estoque;
        public string Nome { get; set; }
        public string Marca { get; set; }
        public double Preco {
            get => this._preco;
            set => this._preco = (value >= 0) ?
                value :
                throw new ArgumentOutOfRangeException(
                    nameof(value),
                    "Preço deve ser positivo");
        }
        public int Estoque {
            get => this._estoque;
            set => this._estoque = (value >= 0) ?
                value :
                throw new ArgumentOutOfRangeException(
                    nameof(value),
                    "Estoque deve ser positivo");
        }
        public string showDetails =>
            $"Nome: {this.Nome}\n" +
            $"Marca: {this.Marca}\n" +
            $"Preço: {this.Preco}\n" +
            $"Estoque: {this.Estoque}";
    }
}
