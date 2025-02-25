using Desafio.Modelo;

// Lista filmes, adiciona e mostra filmes
List<Filme> filmes = [];

filmes.Add(new Filme("Filme1", 123));
filmes.Add(new Filme("Filme2", 1234));
filmes.Add(new Filme("Filme3", 123413));
filmes.Add(new Filme("Filme4", 1234231));
filmes.Add(new Filme("Filme5", 213124213));

filmes.ForEach(f => Console.WriteLine(f.Titulo));

// Operações com filme da 2º posição
filmes[1].AdicionarElenco(new Artista("Fulano", 32));
filmes[1].AdicionarElenco(new Artista("Fulano1", 33));
filmes[1].AdicionarElenco(new Artista("Fulano2", 34));

filmes[1].ListarElenco();

// Operações com um artista
List<Artista> listaElenco = filmes[1].Elenco;
listaElenco[0].AdicionarFilme(filmes[3]);
listaElenco[0].MostrarFilmes();

// Operações com a 4º posição
filmes[3].ListarElenco();