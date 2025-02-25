namespace Desafio.model
{
    class Conta
    {
        public Titular Titular { get; set; }
        public int Agencia { get; set; }
        public int Numero { get; set; }
        public double Saldo { get; set; }
        public double Limite { get; set; }
        // Pode-se fazer assim também
        // public string Informacoes => $"Conta nº {this.Numero}, Agência {this.Agencia}, Titular: {this.Titular.Nome} - Saldo: {this.Saldo}";

    public void ShowDetails()
        {
            Console.WriteLine("Informações do Titular:");
            this.Titular.ShowDetails();

            Console.WriteLine("\nInformações da Conta");
            Console.WriteLine(
                $"Agencia: {this.Agencia}\n" +
                $"Numero: {this.Numero}\n" +
                $"Saldo: R${this.Saldo}\n" +
                $"Limite: R${this.Limite}\n"
            );
        }

    }
}