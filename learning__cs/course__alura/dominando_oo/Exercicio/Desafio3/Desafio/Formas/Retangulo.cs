namespace Desafio.Formas;

internal class Retangulo(double ladoA, double ladoB) : FormasGeometricas
{
    public double LadoA { get; } = ladoA;
    public double LadoB { get; } = ladoB;

    public override double GetArea()
    {
        return LadoA * LadoB;
    }

    public override double GetPerimetro()
    {
        return 2 * (LadoA + LadoB);
    }
}
