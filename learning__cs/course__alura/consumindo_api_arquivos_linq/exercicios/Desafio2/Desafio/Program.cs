using Desafio.Modelos;
using System.Text.Json;

using (HttpClient client = new HttpClient())
{
    try
    {
        string resposta = await client.GetStringAsync("https://raw.githubusercontent.com/ArthurOcFernandes/Exerc-cios-C-/curso-4-aula-2/Jsons/TopMovies.json");

        var filmes = JsonSerializer.Deserialize<List<Filme>>(resposta);
        foreach (var filme in filmes)
        {
            Console.WriteLine(filme.FichaTecnica);
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }

    try
    {
        string resposta = await client.GetStringAsync("https://raw.githubusercontent.com/ArthurOcFernandes/Exerc-cios-C-/curso-4-aula-2/Jsons/Paises.json");
        //Console.WriteLine(resposta);
        var paises = JsonSerializer.Deserialize<List<Pais>>(resposta);
        foreach (var pais in paises)
        {
            Console.WriteLine(pais.Informacoes);
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }

    try
    {
        string resposta = await client.GetStringAsync("https://github.com/ArthurOcFernandes/Exerc-cios-C-/raw/curso-4-aula-2/Jsons/Carros.json");

        var carros = JsonSerializer.Deserialize<List<Carro>>(resposta);
        foreach (var carro in carros)
        {
            Console.WriteLine(carro.Informacoes);
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }

    try
    {
        string resposta = await client.GetStringAsync("https://github.com/ArthurOcFernandes/Exerc-cios-C-/raw/curso-4-aula-2/Jsons/Livros.json");

        var livros = JsonSerializer.Deserialize<List<Livro>>(resposta);
        foreach (var livro in livros)
        {
            Console.WriteLine(livro.FichaTecnica);
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }
}