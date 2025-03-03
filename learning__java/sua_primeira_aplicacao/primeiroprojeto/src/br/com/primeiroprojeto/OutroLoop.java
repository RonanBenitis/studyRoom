package br.com.primeiroprojeto;

import java.util.Scanner;

public class OutroLoop {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);
        double somaAvaliacao = 0;
        double nota = 0;
        int totalDeNotas = 0;

        while (nota != -1) {
            System.out.println("Diga sua avaliação para filme ou -1 para encerrar: ");
            nota = leitura.nextDouble();

            // Condição para não atribuir -1 à variável e ser considera na média por engano
            if (nota != -1) {
                somaAvaliacao += nota;
                totalDeNotas++; // Pós incremento
            }
        }

        double mediaAvaliacao = somaAvaliacao / totalDeNotas; // 0 dividido por 0 terá retorno de NaN, ou seja, Not A Number

        System.out.printf("Media de avaliações: %.2f.%n", mediaAvaliacao);
    }
}
