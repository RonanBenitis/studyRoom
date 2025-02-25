namespace Desafio.Formas;

internal class Triangulo(double @base, double altura) : FormasGeometricas
{
    public double Base { get; } = @base;
    public double Altura { get; } = altura;

    public override double GetArea()
    {
        return (Base + Altura) / 2;
    }

    public override double GetPerimetro()
    {
        // Considerando um triangulo retangulo
        // Ou seja, base + altura + teorema de pitagoras para hipotenusa
        return Base + Altura + Math.Sqrt(Base * Base + Altura * Altura);
    }
}
