using Desafio.model;
using Desafio.model.Jogos;

Titular titular = new("Jorge Benjor", "1231231", "Av. Fulano");

Conta conta = new(titular, 123, 123123, 3000);
conta.ShowDetails();

Catalogo catalogo = new();
catalogo.AddGame("Stardew Valley", "Exploração", "ConcernedApe");
catalogo.AddGame("Minecraft", "Exploração", "Mojang");
catalogo.ShowCatalog();
