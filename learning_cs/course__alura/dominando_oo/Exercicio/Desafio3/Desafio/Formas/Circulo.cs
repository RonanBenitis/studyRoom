namespace Desafio.Formas;

class Circulo(double raio) : FormasGeometricas
{
    public double Raio { get; } = raio;

    public override double GetArea()
    {
        return Math.PI * Math.Pow(Raio, 2);
    }

    public override double GetPerimetro()
    {
        return 2 * Math.PI * Raio;
    }
}