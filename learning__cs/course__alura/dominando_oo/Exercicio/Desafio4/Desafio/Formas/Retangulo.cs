namespace Desafio.Formas;

internal class Retangulo(double ladoA, double ladoB) : FormasGeometricas
{
    public double LadoA { get; } = ladoA;
    public double LadoB { get; } = ladoB;

    public double GetArea()
    {
        return LadoA * LadoB;
    }

    public double GetPerimetro()
    {
        return 2 * (LadoA + LadoB);
    }
}
