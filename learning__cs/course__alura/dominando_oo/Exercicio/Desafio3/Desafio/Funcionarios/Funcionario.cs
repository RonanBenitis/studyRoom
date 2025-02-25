namespace Desafio.Funcionarios
{
    internal class Funcionario(string nome, double salario)
    {
        public string Nome { get; set; } = nome;
        public double Salario { get; set; } = salario;
    }
}
