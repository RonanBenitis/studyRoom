package service;

import model.Cliente;

public class Account {
    public static void getAmount(Cliente cliente) {
        System.out.printf("O saldo atual é R$ %.2f\n\n", cliente.getValor());
    }

    public static void deposit(Cliente cliente, double depositAmout) {
        double actualValue = cliente.getValor();
        cliente.setValor(actualValue + depositAmout);
    }

    public static void withdraw(Cliente cliente, double withdrawAmount) {
        double actualValue = cliente.getValor();
        double balance = actualValue - withdrawAmount;

        if (balance >= 0) {
            cliente.setValor(balance);
        } else {
            throw new IllegalArgumentException("Saldo insuficiente para realizar o saque");
        }
    }
}
