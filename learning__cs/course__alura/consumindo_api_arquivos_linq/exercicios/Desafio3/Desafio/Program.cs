using Desafio;

// Exercicio 1
List<int> lista1 = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 9, 1];

var numerosUnicos = lista1
    .Distinct();

Console.WriteLine("=== Listando apenas valores únicos, não considerando valores repetidos ===");
foreach (var num in numerosUnicos)
{
    Console.Write($"{num} ");
}

// Exercicio 2
List<int> lista2 = [1, 2, 3, 4, 5];
List<int> lista3 = [3, 4, 5, 6, 7];

var numerosComuns = lista2
    .Intersect(lista3);

Console.WriteLine("\n\n=== Valores iguais entre duas listas ===");
foreach (var num in numerosComuns)
{
    Console.Write($"{num} ");
}

// Exercicio 3
List<Livro> livros = 
[
    new Livro { Titulo = "Aprendendo LINQ", Autor = "João Silva", AnoPublicacao = 2005 },
    new Livro { Titulo = "Programação em C#", Autor = "Ana Oliveira", AnoPublicacao = 2010 },
    new Livro { Titulo = "Algoritmos e Estruturas de Dados", Autor = "Carlos Santos", AnoPublicacao = 1998 },
    new Livro { Titulo = "Introdução à Inteligência Artificial", Autor = "Mariana Costa", AnoPublicacao = 2021 },
    new Livro { Titulo = "Design Patterns", Autor = "Paulo Rocha", AnoPublicacao = 2002 }
];

var listaLivrosOrdenada = livros
    .Where(l => l.AnoPublicacao > 2000)
    .OrderBy(l => l.Titulo)
    .Select(l => l.Titulo);

Console.WriteLine("\n\n=== Livros lançados depois de 2000 ===");
foreach (var livro in listaLivrosOrdenada)
{
    Console.WriteLine(livro);
}

// Exercicio 4
List<Produto> produtos =
[
        new Produto { Nome = "Laptop", Preco = 1200 },
        new Produto { Nome = "Smartphone", Preco = 800 },
        new Produto { Nome = "Tablet", Preco = 500 },
        new Produto { Nome = "Câmera", Preco = 300 }
];

var mediaProdutos = produtos
    .Average(p => p.Preco);

Console.WriteLine("\n=== Média dos Produtos ===");
Console.WriteLine($"{mediaProdutos:c}");

// Exercicio 5
List<string> palavras = [ "cachorro", "gato", "elefante", "leão", "cobra" ];

var palavrasFiltradas = palavras
    .Where(p => p.Length > 3)
    .OrderBy(p => p.Length);

Console.WriteLine("\n=== Palavras com mais de 3 caracteres, ordenados por comprimento ===");
foreach (var palavra in palavrasFiltradas)
{
    Console.Write($"{palavra} ");
}

// Exercicio 6
List<int> lista4 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];

var numerosPares = lista4
    .Where(n => n % 2 == 0);

Console.WriteLine("\n\n== Numeros pares ===");
foreach (var num in numerosPares)
{
    Console.WriteLine(num);
}