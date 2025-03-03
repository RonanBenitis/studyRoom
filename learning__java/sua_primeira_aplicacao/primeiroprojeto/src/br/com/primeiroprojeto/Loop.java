package br.com.primeiroprojeto;

import java.util.Scanner;

public class Loop {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);
        double somaAvaliacao = 0;
        double nota = 0;
        int numeroDeNotas = 3;
//        double mediaAvaliacao = somaAvaliacao / numeroDeNotas;

        for (int i = 0; i < numeroDeNotas; i++) {
            System.out.println("Diga sua avaliação para o filme");
            nota = leitura.nextDouble();
            somaAvaliacao += nota;
        }

        double mediaAvaliacao = somaAvaliacao / numeroDeNotas;

        System.out.printf("Media de avaliações: %.2f.%n", mediaAvaliacao);
    }
}
