# Para saber mais: Generics

O Generics é um recurso da linguagem que permite que possamos personalizar métodos, classes, interfaces e estruturas, podendo inclusive diminuir retrabalho e maximizar o desempenho de uma aplicação proporcionando uma segurança de tipos.

Desde a versão 2.0 do .NET Framework a plataforma traz esta feature, usando generics conseguimos deixar a definição do tipo para o momento que precisamos de determinado elemento no nosso código, o que em resumo é dizer que a classe ou método possa trabalhar com qualquer tipo. Ok, mas como é isso na prática? Vamos a um exemplo:

```cs
  public class MinhaClasseGenerica<T>
    {
        public T PropriedadeGenerica { get; set; }
        public void ExibirDados(T t)
        {
            Console.WriteLine($"Dado Informado = {t.ToString()}");
            Console.WriteLine($"Tipo = {t.GetType()}");
        }  

    }
```

Note que a classe possui um parâmetro <T> que será substituído pela tipo de quando criamos um objeto desta classe, veja:

```cs
MinhaClasseGenerica<string> objGenerico = new MinhaClasseGenerica<string>();
objGenerico.ExibirDados("Olá mundo!");


MinhaClasseGenerica<int> objGenerico2 = new MinhaClasseGenerica<int>();
objGenerico2.ExibirDados(3);


Pessoa andre = new Pessoa() { Idade = 18, Nome = "André" };
MinhaClasseGenerica<Pessoa> objGenerico3 = new MinhaClasseGenerica<Pessoa>();
objGenerico3.ExibirDados(andre);


public class Pessoa
{
    public string Nome { get; set; }
    public int Idade { get; set; }

    public override string ToString()
    {
        return $"Nome = {this.Nome} com Idade = {this.Idade}";
    }
}
```

Vamos executar e teremos a seguinte saída no console:
```bash
Dado Informado = Olá mundo!
Tipo = System.String
Dado Informado = 3
Tipo = System.Int32
Dado Informado = Nome = André com Idade = 18
Tipo = Pessoa
```

Os genéricos oferecem uma série de vantagens como:

- Diminuição de ocorrer erros de conversão de tipos em tempo de execução.
- Melhora no desempenho, os tipos de coleções que usam generics geralmente executam melhor para armazenar e manipular tipos de valor.
- Redução do consumo de memória pois não executam operação de Boxing (converter explicitamente um tipo de valor em um objeto).

Para saber ainda mais sobre os recursos e vantagens na utilização de generics fica a recomendação da documentação oficial da Microsoft [Generics in .NET](https://learn.microsoft.com/pt-br/dotnet/standard/generics/).