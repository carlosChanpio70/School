package com.example;

public final class IMC {

    private String genero;
    private double peso;
    private double altura;
    private double[] lista_imc = new double[4];

    public IMC(String genero, double peso, double altura) {
        setGenero(genero);
        setPeso(peso);
        setAltura(altura);
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        genero = genero.toUpperCase().trim();
        switch (genero) {
            case "M":
                this.lista_imc = new double[]{20.7, 26.4, 27.8, 31.1};
                break;
            case "F":
                this.lista_imc = new double[]{19.1, 25.8, 27.3, 32.3};
                break;
            default:
                throw new IllegalArgumentException("Genero inválido");
        }
        this.genero = genero;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        if (peso > 0) {
            this.peso = peso;
        } else {
            throw new IllegalArgumentException("Peso inválido");
        }
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        if (altura > 0) {
            this.altura = altura;
        } else {
            throw new IllegalArgumentException("Altura inválida");
        }
    }

    public String calculate() {
        double imc = this.peso / (this.altura * this.altura);
        String results;
        if (imc < this.lista_imc[0]) {
            results = String.format("Abaixo do peso, com IMC de %.2f", imc);
        } else if (imc < this.lista_imc[1]) {
            results = String.format("No peso normal, com IMC de %.2f", imc);
        } else if (imc < this.lista_imc[2]) {
            results = String.format("Marginalmente acima do peso, com IMC de %.2f", imc);
        } else if (imc < this.lista_imc[3]) {
            results = String.format("Acima do peso ideal, com IMC de %.2f", imc);
        } else {
            results = String.format("Obeso, com IMC de %.2f", imc);
        }
        return results;
    }
}
