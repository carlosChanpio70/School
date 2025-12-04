package com.example;

public final class Genero {
    private String genero;
    private double[] lista_imc;

    public Genero(String genero){
        setGenero(genero);
        setLista_IMC();
    }

    public String getGenero() {
        return genero;
    }

    public double[] getLista_imc() {
        return lista_imc;
    }

    public void setGenero(String genero) {
        this.genero = genero.toUpperCase().trim();
    }

    public void setLista_IMC() {
        switch (this.genero) {
            case "M":
                this.lista_imc = new double[]{20.7, 26.4, 27.8, 31.1};
                break;
            case "F":
                this.lista_imc = new double[]{19.1, 25.8, 27.3, 32.3};
                break;
            default:
                throw new IllegalArgumentException("Genero inválido");
        }
    }
}
