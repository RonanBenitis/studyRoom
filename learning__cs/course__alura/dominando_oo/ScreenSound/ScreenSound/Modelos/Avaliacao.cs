namespace ScreenSound.Modelos;

internal class Avaliacao
{
    public int Nota { get; }

    public Avaliacao(int nota)
    {
        if (nota <= 0) Nota = 0;
        if (nota >= 10) Nota = 10;
        Nota = nota;
    }

    public static Avaliacao Parse(string texto)
    {
        int nota = int.Parse(texto);
        return new(nota);
    }
}
