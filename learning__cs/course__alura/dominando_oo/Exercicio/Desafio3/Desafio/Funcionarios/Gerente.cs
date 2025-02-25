namespace Desafio.Funcionarios;

internal class Gerente(string nome, double salario, string setor)
    : Funcionario(nome, salario)
{
    public string Setor { get; } = setor;
}
