package model;

public class Cliente {

    private final String nome;
    private final String tipoConta;
    private double valor;

    public Cliente(double valor, String tipoConta, String nome) {
        this.valor = valor;
        this.tipoConta = tipoConta;
        this.nome = nome;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public String getNome() {
        return nome;
    }

    public String getTipoConta() {
        return tipoConta;
    }

    public double getValor() {
        return valor;
    }

}
