namespace ScreenSound.Modelos;

internal interface IAvaliavel
{
    void AddNota(Avaliacao nota);
    double Media { get; }
}
