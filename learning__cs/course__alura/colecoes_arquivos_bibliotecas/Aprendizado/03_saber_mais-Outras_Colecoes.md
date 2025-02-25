# Para saber mais: outras Coleções
Na biblioteca de classes do .NET para trabalharmos com coleções além das já mencionadas Array, ArrayList e List temos uma série de collection igualmente interessante para usarmos no desenvolvimento de nossas aplicações. Abaixo vamos listar mais algumas:

## SortedList
Nesta coleção trabalhamos com itens ordenados por um conjunto de chave-valor. Algumas características:
- Utilizada para ordenarmos itens sem muito esforço.
- Podemos procurar por uma chave específica.

A classe SortedList também possui uma versão que aceita generics e fica no namespace System.Collections.Generic. Um exemplo:
```cs
SortedList<int,string> times = new SortedList<int,string>();
times.Add(0, "Flamengo");
times.Add(1, "Santos");
times.Add(2, "Juventus");

foreach (var item in times.Values)
{
    Console.WriteLine(item);
}
```

## Stack
Esta coleção implementa o conceito de pilha, onde os elementos mais novos são adicionados no topo da pilha, e devem ser retirados nesta ordem. Esta classe também possui uma versão genérica. Exemplo de utilização:
```cs
Stack<string> minhaPilhaDeLivros = new Stack<string>();
minhaPilhaDeLivros.Push("Harry Porter e a Ordem da Fênix");
minhaPilhaDeLivros.Push("A Guerra do Velho.");
minhaPilhaDeLivros.Push("Protocolo Bluehand");
minhaPilhaDeLivros.Push("Crise nas Infinitas Terras.");
```

Para encontrarmos o livro que está no topo da pilha usando o método `Peek`, para remove-lo usamos o método `Pop`:
```cs
Console.WriteLine(minhaPilhaDeLivros.Peek());// Retorna o elemento do topo.
Console.WriteLine(minhaPilhaDeLivros.Pop()); //Remove o elemento do topo
```

## Queue
Esta coleção por sua vez implementa o conceito de fila, onde os elementos mais antigos são os primeiros a serem removidos. Para adicionar um elemento na fila usamos o método `Enqueue`:
```cs
Queue<string> filaAtenndimento = new Queue<string>();
filaAtendimento.Enqueue("André Silva");
filaAtendimento.Enqueue("Lou Ferrigno");
filaAtendimento.Enqueue("Gal Gadot");
```

Similar ao método `Pop` para a fila temos o método `Dequeue` para remover um objeto da fila. Exemplo:
```cs
filaAtendimento.Dequeue();//Remove o primeiro elemento da fila.
```

## HashSet
Focado em alta performance esta coleção não aceita valores duplicados, para adicionar elementos temos também disponível o método `Add`:
```cs
HashSet<int> _numeros = new HashSet<int>();
_numeros.Add(0);
_numeros.Add(1);
_numeros.Add(1);
_numeros.Add(1);
```

Para saber quantos elementos a coleção _numeros possui podemos usar a propriedade `Count`:
```cs
Console.WriteLine(_numeros.Count);// a saída é 2.
```

Para exibirmos o conteúdo podemos percorrer a coleção usando um foreach:
```cs
foreach (var item in _numeros)
{
    Console.WriteLine(item);
}
```

Para saber mais sobre as outras coleções do .NET deixamos a recomendação de acesso a documentação da Microsoft [Coleções (C#)](https://learn.microsoft.com/pt-br/dotnet/csharp/language-reference/builtin-types/collections)