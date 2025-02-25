namespace Desafio.Funcionarios;

internal class Analista(string nome, double salario, string areaAtuacao)
    : Funcionario(nome, salario)
{
    public string AreaAtuacao { get; } = areaAtuacao;
}
