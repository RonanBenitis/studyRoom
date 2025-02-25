namespace Desafio.model
{
    class Titular
    {
        public string Nome { get; set; }

        public void ShowDetails()
        {
            Console.WriteLine(
                $"Nome: {this.Nome}"
                );
        }
    }
}