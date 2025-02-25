namespace Desafio.Veiculo;

internal class Veiculo : IPilotavel, IVoavel
{
    public void Pilotar()
    {
        Console.WriteLine("Veículo está pilotando");
    }

    public void Voar()
    {
        Console.WriteLine("Veículo está voando");
    }
}
