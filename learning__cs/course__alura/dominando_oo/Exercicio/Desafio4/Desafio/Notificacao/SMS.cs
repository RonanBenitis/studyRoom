namespace Desafio.Notificacao;

internal class SMS : INotificavel
{
    public string NumeroTelefone { get; set; }
    public void EnviarNotificação()
    {
        Console.WriteLine($"Enviando SMS para {NumeroTelefone}: Notificação importante!");
    }
}
