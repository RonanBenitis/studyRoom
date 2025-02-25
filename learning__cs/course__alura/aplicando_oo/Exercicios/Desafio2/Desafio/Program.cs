using Desafio.model;

ContaBancaria conta1 = new("123", "Jorge Benjor", 123123123, "Aaaahey123");
conta1.ExibirInformacoes();

Carro carro1 = new("Wolskvagen", "Gol");
carro1.Ano = 2023;
carro1.Acelerar();
carro1.Frear();
carro1.Buzinar();
Console.WriteLine(carro1.DescricaoDetalhada);

Produto produto1 = new();
produto1.Nome = "Café";
produto1.Marca = "Melita";
produto1.Preco = 10.90;
produto1.Estoque = 5;
Console.WriteLine(produto1.showDetails);