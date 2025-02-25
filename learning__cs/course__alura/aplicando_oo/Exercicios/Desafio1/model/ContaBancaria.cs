namespace Desafio1.model
{
    class ContaBancaria
    {
        public string Id;
        public string Titular;
        public float Saldo;
        public string Senha;

        public ContaBancaria(string id, string titular, float saldo,
            string senha)
        {
            Id = id;
            Titular = titular;
            Saldo = saldo;
            Senha = senha;
        }
        public void ExibirInformacoes()
        {
            Console.WriteLine($"Titula: {Titular}");
            Console.WriteLine($"Saldo: R${Saldo}");
        }
    }
}