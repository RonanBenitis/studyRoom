namespace Desafio.Notificacao;

internal class Email : INotificavel
{
    public string EnderecoEmail { get; set; }

    public void EnviarNotificação()
    {
        Console.WriteLine($"Enviando e-mail para {EnderecoEmail}: Notificação importante!");
    }
}
