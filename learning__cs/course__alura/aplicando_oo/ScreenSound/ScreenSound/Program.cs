Banda queen = new("Queen");

Album albumQueen = new("A night at the opera");

Musica musica1 = new(queen, "Love of my life")
{
    // Inicializando propriedades opcionais de forma simplificada
    Duracao = 213,
    Disponivel = true,
};

Musica musica2 = new(queen, "Bohemian Rhapsody")
{
    // Inicializando propriedades opcionais de forma simplificada
    Duracao = 354,
    Disponivel = false,
};

albumQueen.AdicionarMusica(musica1);
albumQueen.AdicionarMusica(musica2);

musica1.ExibirFichaTecnica();
musica2.ExibirFichaTecnica();

albumQueen.ExibirMusicas();

queen.AddAlbum(albumQueen);
queen.ExibirDiscografia();


// Resolução do desafio
Podcast podcast = new("Jorge Benjor", "De Ben com a vida");
podcast.AdicionarEpisodio("Musica boa 1", 1);
podcast.AdicionarEpisodio("Musica boa 5", 5);
podcast.AdicionarEpisodio("Musica boa 3", 3);
podcast.AdicionarEpisodio("Musica boa 2", 2);
podcast.AdicionarEpisodio("Musica boa 4", 4);
podcast.ExibirDetalhes();

var listaEpisodios = podcast.TotalEpisodios;
listaEpisodios[0].Duracao = 31;
listaEpisodios[0].AdicionarConvidado("Caetano Veloso");
Console.WriteLine(listaEpisodios[0].Resumo);
