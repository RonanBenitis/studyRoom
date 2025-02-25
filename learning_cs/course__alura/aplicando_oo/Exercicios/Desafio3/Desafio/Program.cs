using Desafio.model;

// Exercicio 1 e 2
Titular titular = new();
titular.Nome = "Jorge Benjor";

Conta conta = new();
conta.Titular = titular;
conta.Saldo = 150;
conta.Numero = 123;
conta.Agencia = 123123;
conta.Limite = 3000;
conta.ShowDetails();

// Exercicio 3
Produto produto = new();
produto.Nome = "Café";
produto.Marca = "Melita";

Estoque estoque = new();
estoque.Add(produto);
estoque.Add(produto);
estoque.Add(produto);
estoque.Add(produto);
estoque.Add(produto);
estoque.ShowList();

// Exercicio 4
