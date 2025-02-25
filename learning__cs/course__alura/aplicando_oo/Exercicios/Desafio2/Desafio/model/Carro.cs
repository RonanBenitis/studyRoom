namespace Desafio.model
{
    internal class Carro(string marca, string modelo)
    {
        public string Marca { get; set; } = marca;
        public string Modelo { get; set; } = modelo;
        private int _ano;
        public int Ano {
            get => _ano;
            set => _ano = (value >= 1960 && value <= 2023) ? 
                value :
                throw new ArgumentOutOfRangeException(nameof(value), "O ano deve estar entre 1960 e 2023");
        }
        public string DescricaoDetalhada =>
            $"Fabricante: {Marca} | Modelo: {Modelo} | Ano: {Ano}";
        private int Velocidade { get; set; } = 0;

        public void Acelerar()
        {
            Console.WriteLine("Acelerando...");
            if (Velocidade < 100)
            {
                Velocidade += 5;
            }
            Console.WriteLine($"Velocidade: {Velocidade}");
        }

        public void Frear()
        {
            Console.WriteLine("Freando...");
            if (Velocidade > 0)
            {
                Velocidade -= 5;
            }
            Console.WriteLine($"Velocidade: {Velocidade}");
        }

        public void Buzinar()
        {
            Console.WriteLine("Beeep BEEEEP!");
        }
    }
}
