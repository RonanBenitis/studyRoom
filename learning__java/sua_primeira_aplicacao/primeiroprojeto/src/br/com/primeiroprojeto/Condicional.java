package br.com.primeiroprojeto;

public class Condicional {
    public static void main(String[] args) {
        int anoDeLancamento = 2022;
        boolean incluidoNoPlano = true;
        double notaDOFilme = 8.1;
        String tipoPlano = "plus";

        if (anoDeLancamento > 2022) {
            System.out.println("Lançamento que os clientes estão curtindo");
        }

        if (anoDeLancamento >= 2022) {
            System.out.println("Lançamento que os clientes estão curtindo, incluindo 2022");
        }

        if (incluidoNoPlano || tipoPlano.equals("plus")) {
            System.out.println("Aqui passou");
        }
    }
}
