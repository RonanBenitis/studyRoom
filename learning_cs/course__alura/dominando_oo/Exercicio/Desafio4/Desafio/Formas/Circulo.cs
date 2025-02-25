namespace Desafio.Formas;

class Circulo(double raio) : FormasGeometricas
{
    public double Raio { get; } = raio;

    public double GetArea()
    {
        return Math.PI * Math.Pow(Raio, 2);
    }

    public double GetPerimetro()
    {
        return 2 * Math.PI * Raio;
    }
}