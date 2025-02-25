using bytebank.Modelos.Conta;

namespace bytebank_ATENDIMENTO.bytebank.Util;

public class ListaDeContasCorrentes
{
    public ContaCorrente[] itens;
    private int _proximaPosicao = 0;

    public int Tamanho
    {
        get
        {
            return _proximaPosicao;
        }
    }

    // Criamos um indexador
    /*
     * Ou seja, return algo caso passemos um indice
     * neste objeto
     */
    public ContaCorrente this[int indice]
    {
        get
        {
            /*
             * É a mesma coisa qu return itens[indice]
             * mas, com validações
             */
            return RecuperarContaPorIndice(indice);
        }
    }

    // CONSTRUTOR
    /*
     * int tamanhoInicial=5 é um valor defeault, ou seja,
     * se nada for passado no construtor, o valor será 5.
     * Caso for passado um valor diferente, será atribuido o
     * valor diferente
     */
    public ListaDeContasCorrentes(int tamanhoInicial=5)
    {
        itens = new ContaCorrente[tamanhoInicial];
    }

    public void Adicionar(ContaCorrente item)
    {
        Console.WriteLine($"Adicionando item na posição {_proximaPosicao}");
        VerificarCapacidade(_proximaPosicao + 1);
        itens[_proximaPosicao] = item;
        _proximaPosicao++;
    }

    private void VerificarCapacidade(int tamanhoNecessario)
    {
        if (itens.Length >= tamanhoNecessario)
        {
            return;
        }
        else
        {
            Console.WriteLine("Aumentando a capacidade da lista!");
            ContaCorrente[] novoArray = new ContaCorrente[tamanhoNecessario];

            // Coletando os valores do array antigo para o novo array
            for (int i = 0; i < itens.Length; i++)
            {
                novoArray[i] = itens[i];
            }

            itens = novoArray;
        }
    }

    public void Remover (ContaCorrente conta)
    {
        int indiceItem = -1; // Apenas para incializar

        /*
         * DESCRIÇÃO
         * Identifica indice da conta desejada
         * 
         * EXEMPLO
         * Suponhamos que nossa array está da seguinte forma
         * [conta1] [conta2] [conta3] [conta4] [conta5]
         * 
         * Suponhamos que passamos no parametro a conta3
         */
        for (int i = 0; i < _proximaPosicao; i++)
        {
            ContaCorrente contaAtual = itens[i];

            if (contaAtual == conta)
            {
                indiceItem = i;
                break;
            }
        }

        // A saída será i = 2 (pois é o indice 2)

        /*
         * DESCRIÇÃO
         * Substitui o valor atual do indice encontrado pelo indice
         * seguinte, e assim suscetivamente
         * 
         * EXEMPLO
         * Os valores estão da seguinte forma
         * itens = [conta1] [conta2] [conta3] [conta4] [conta5]
         * i = 2
         */
        for (int i = indiceItem; i < _proximaPosicao - 1; i++)
        {
            itens[i] = itens[i + 1];
        }

        /*
         * A saida será:
         * itens = [conta1] [conta2] [conta4] [conta5] [conta5]
         */

        /*
         * DESCRIÇÃO
         * Decremento, para reduzir uma posição
         */
        _proximaPosicao--;

        /*
         * DESCRIÇÃO
         * Limpa a ultima posição, sendo que já movemos os valores desejados
         * uma indice para trás
         * 
         * EXEMPLO:
         * itens = [conta1] [conta2] [conta4] [conta5] [conta5]
         */
        itens[_proximaPosicao] = null;

        /*
         * A saida será:
         * itens = [conta1] [conta2] [conta4] [conta5] [null]
         */
    }

    public void ExibeLista()
    {
        if (_proximaPosicao == 0)
        {
            Console.WriteLine("Lista vazia!");
            return;
        }

        for (int i = 0; i < _proximaPosicao; i++)
        {
            var conta = itens[i];
            Console.WriteLine($"Indice[{i}] = Conta:{conta.Conta} - Nº da Agencia: {conta.Numero_agencia}");
        }
    }

    public ContaCorrente ContaDeMaiorSaldo()
    {
        ContaCorrente? conta = null;
        double maiorValor = 0;

        for (int i = 0; i < itens.Length; i++)
        {
            if (itens[i] != null)
            {
                if (maiorValor < itens[i].Saldo)
                {
                    maiorValor = itens[i].Saldo;
                    conta = itens[i];
                }
            }
        }

        return conta!;
    }

    public ContaCorrente RecuperarContaPorIndice(int indice)
    {
        if(indice < 0 || indice >= _proximaPosicao)
        {
            throw new ArgumentOutOfRangeException(nameof(indice));
        }

        return itens[indice];
    }

}
