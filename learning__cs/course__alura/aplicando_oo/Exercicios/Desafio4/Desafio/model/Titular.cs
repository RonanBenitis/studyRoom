namespace Desafio.model
{
    class Titular
    {
        public Titular(string nome, string cpf, string endereco)
        {
            Nome = nome;
            Cpf = cpf;
            Endereco = endereco;
        }

        public string Nome { get; set; }
        public string Cpf { get; set; }
        public string Endereco { get; set; }

        public void ShowDetails()
        {
            Console.WriteLine(
                $"Nome: {this.Nome}"
                );
        }
    }
}