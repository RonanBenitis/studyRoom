namespace Desafio1.model
{
    internal class Carro
    {
        public string Marca;
        public string Modelo;
        public int Velocidade = 0;

        public Carro(string marca, string modelo)
        {
            Marca = marca;
            Modelo = modelo;
        }

        public void Acelerar()
        {
            Console.WriteLine("Acelerando...");
            if (Velocidade < 100)
            {
                Velocidade = Velocidade + 5;
            }
            Console.WriteLine($"Velocidade: {Velocidade}");
        }

        public void Frear()
        {
            Console.WriteLine("Freando...");
            if (Velocidade > 0)
            {
                Velocidade = Velocidade - 5;
            }
            Console.WriteLine($"Velocidade: {Velocidade}");
        }

        public void Buzinar()
        {
            Console.WriteLine("Beeep BEEEEP!");
        }
    }
}
