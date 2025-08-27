package com.example;

public class IMC {

    private String genero;
    private double peso;
    private double altura;

    public void Imc(String genero,double peso,double altura){
        this.setGenero(genero);
        this.setPeso(peso);
        this.setAltura(altura);
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        if (genero!="M" || genero!="F"){
            this.genero = genero;
        } else {
            throw new IllegalArgumentException("Genero inválido");
        }
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        if (peso>0) {
            this.peso = peso;
        } else {
            throw new IllegalArgumentException("Peso inválido");
        }
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        if (altura>0) {
            this.altura = altura;
        } else {
            throw new IllegalArgumentException("Altura inválida");
        }
    }

    public String Calculate() {
        double[] lista_imc;
        if (this.genero.equals("m")) {
            lista_imc = new double[] { 20.7, 26.4, 27.8, 31.1 };
        } else {
            lista_imc = new double[] { 19.1, 25.8, 27.3, 32.3 };
        }
        double imc = this.peso / (this.altura * this.altura);
        String results;
        if (imc < lista_imc[0]) {
            results = "Abaixo do peso, com IMC de " + imc;
        } else {
            if (imc < lista_imc[1]) {
                results = "No peso normal, com IMC de " + imc;
            } else {
                if (imc < lista_imc[2]) {
                    results = "Marginalmente acima do peso, com IMC de " + imc;
                } else {
                    if (imc < lista_imc[3]) {
                        results = "Acima do peso ideal, com IMC de " + imc;
                    } else {
                        results = "Obeso, com IMC de " + imc;
                    }
                }
            }
        }
        return results;
    }
}