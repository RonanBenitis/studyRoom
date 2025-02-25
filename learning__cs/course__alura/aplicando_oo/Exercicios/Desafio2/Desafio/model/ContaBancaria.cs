namespace Desafio.model
{
    class ContaBancaria(string id, string titular, float saldo,
        string senha)
    {
        public string Id { get; set; } = id;
        public string Titular { get; set; } = titular;
        public float Saldo { get; set; } = saldo;
        public string Senha { get; set; } = senha;

        public void ExibirInformacoes()
        {
            Console.WriteLine($"Titular: {Titular}");
            Console.WriteLine($"Saldo: R${Saldo}");
        }
    }
}