package com.example;

public final class IMC {

    private Calculo calculo;
    private double peso;
    private double altura;
    private double imcvalor;
    private double[] imclista;

    public IMC(String genero, double peso, double altura) {
        setGenero(genero);
        this.calculo = new Calculo(peso,altura);
        setIMC();
    }

    public IMC(){
        this.calculo = new Calculo();
    }

    public double getPeso() {
        return peso;
    }

    public double getAltura() {
        return altura;
    }

    public double getIMC() {
        return imcvalor;
    }

    public Calculo getCalculo() {
        return calculo;
    }

    public void setGenero(String genero) {
        Genero generoclass = new Genero(genero);
        this.imclista = generoclass.getLista_imc();
    }

    public void setPeso(double peso) {
        this.calculo.setPeso(peso);
    }

    public void setAltura(double altura) {
        this.calculo.setAltura(altura);
    }

    public void setIMC() {
        this.imcvalor = this.calculo.getCalculo();
    }

    public void setCalculo() {
        this.calculo = new Calculo(peso, altura);
    }

    public String getResults() {
        setIMC();
        String results;
        if (this.imcvalor < this.imclista[0]) {
            results = "Abaixo do peso";
        } else if (this.imcvalor < this.imclista[1]) {
            results = "No peso normal";
        } else if (this.imcvalor < this.imclista[2]) {
            results = "Marginalmente acima do peso";
        } else if (this.imcvalor < this.imclista[3]) {
            results = "Acima do peso ideal";
        } else {
            results = "Obeso";
        }
        return results;
    }
}