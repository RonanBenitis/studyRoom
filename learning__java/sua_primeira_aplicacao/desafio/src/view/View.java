package view;

import model.Cliente;
import service.Account;

import java.sql.SQLOutput;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class View {
    public static void menu (Scanner sc, Cliente cliente) {
        View.clearConsole();
        View.screenInfo(cliente);
        View.subMenu(sc, cliente);
    }

    public static Cliente login (Scanner sc) {
        System.out.print("""
        Bem vindo(a)!
        
        Por gentileza, informe seu nome:
        """);

        // Leitura
        String nome = sc.nextLine();

        String opcoesConta = """
        Qual conta gostaria de criar:
        1. Conta Corrente
        2. Conta Poupança
        """;

        System.out.print(opcoesConta);

        // Leitura
        int escolha = sc.nextInt();
        sc.nextLine();

        // Criando HashMap
        HashMap<Integer, String> tiposConta = new HashMap<>();
        tiposConta.put(1, "Conta Corrente");
        tiposConta.put(2, "Conta Poupança");

        while (!tiposConta.containsKey(escolha)) {
            System.out.println("Escolha invalida");
            System.out.print(opcoesConta);
            escolha = sc.nextInt();
        }

        return new Cliente(0, tiposConta.get(escolha), nome);
    }

    private static void screenInfo(Cliente cliente) {
        System.out.println("*".repeat(10));
        System.out.println("Dados inicias do cliente:\n");
        View.printScreenDetail(15, "Nome:", cliente.getNome());
        View.printScreenDetail(15, "Tipo conta:", cliente.getTipoConta());
        View.printScreenDetail(15, "Saldo Inicial:", String.valueOf(cliente.getValor()));
        System.out.println("*".repeat(10));
    }


    private static void subMenu(Scanner sc, Cliente cliente) {
        Map<Integer, Runnable> opcoes = new HashMap<>();

        opcoes.put(1, () -> Account.getAmount(cliente));
        opcoes.put(2, () -> {
            System.out.println("Informe o valor para deposito: ");
            double depositAmount = sc.nextDouble();
            sc.nextLine();
            Account.deposit(cliente, depositAmount);
            System.out.println("Valor depositado com sucesso!");
        });
        opcoes.put(3, () -> {
            System.out.println("Informe o valor a ser sacado: ");
            double withdrawAmount = sc.nextDouble();
            sc.nextLine();

            try{
                Account.withdraw(cliente, withdrawAmount);
                System.out.println("Valor sacaado com suceso!");
            } catch (IllegalArgumentException e) {
                System.out.println("Erro: " + e.getMessage());
            }
        });
        opcoes.put(4, () -> {
            System.out.println("Saindo...");
            System.exit(0);
        });

        while (true) {
            System.out.println("""
                    Escolha uma opção
                    1. Consultar valor
                    2. Receber valor
                    3. Sacar valor
                    4. Sair
                    """);

            int opcao = sc.nextInt();
            opcoes.getOrDefault(opcao, () -> System.out.println("opção inválida")).run();
        }
    }

    // FUNÇÕES AUXILIARES
    private static void clearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static void printScreenDetail(int larguraMax, String titulo, String valor) {
        System.out.printf("%-" + larguraMax + "s %s%n", titulo, valor);
    }
}
