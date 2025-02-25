using ScreenSound.Modelos;

namespace ScreenSound.Menus;
internal class MenuRegistrarBandas : Menu
{
    public override void Executar(Dictionary<string, Banda> bandasRegistradas)
    {
        base.Executar(bandasRegistradas);
        ExibirTituloOpcao("Registro de bandas");
        Console.Write("Digite o nome da banda que deseja registrar: ");
        string nomeBanda = Console.ReadLine()!;
        Banda banda = new(nomeBanda);
        bandasRegistradas.Add(nomeBanda, banda);
        Console.WriteLine($"A banda {nomeBanda} foi registrada com sucesso!");
        Thread.Sleep(2000); // Número representado em ms (milisegundo)
        Console.Clear();
    }
}