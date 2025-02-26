package br.com.primeiroprojeto;

import java.util.Scanner;

public class Leitura {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        // Coletando String
        System.out.println("Digite seu filme favorito");
        String filme = leitura.nextLine();
        System.out.println(filme);

        // Coletando int
        System.out.println("Qual o ano de lançamento? ");
        int anoDeLancamento = leitura.nextInt();
        System.out.println(anoDeLancamento);

        // Coletando double
        System.out.println("Diga sua avaliação para o filme: ");
        double avaliacao = leitura.nextDouble(); // No momento da coleta, separador por "." ou "," dependerá da região do programa
        System.out.println(avaliacao);
    }
}
