package br.com.primeiroprojeto;

public class Main {
    public static void main(String[] args) {
        System.out.println("Esse é o Screen Match!");
        System.out.println("Filme: Top Gun: Maverick");

        int anoDeLancamento = 2022;
        String sinopse;
        sinopse = """
                Filme Top Gun
                Filme de aventura com galã dos anos 80
                Muito bom!
                """ + anoDeLancamento;

        System.out.println(sinopse);


        double media = 8.9;
        int classificacao;
        classificacao = (int) (media);
        System.out.println(classificacao);
    }
}