namespace Desafio.Funcionarios;

internal class Programador(string nome, double salario, string linguagemProgramacao)
    : Funcionario(nome, salario)
{
    public string LinaguagemProgramacao { get; } = linguagemProgramacao;
}
