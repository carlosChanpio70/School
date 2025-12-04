package com.example;

public final class Calculo {
    private double peso;
    private double altura;
    private double imc;

    public Calculo(double peso,double altura){
        setPeso(peso);
        setAltura(altura);
        setCalculo();
    }

    public Calculo()
    {}

    public double getCalculo() {
        return imc;
    }

    public void setPeso(double peso) {
        if (peso > 0) {
            this.peso = peso;
        } else {
            throw new IllegalArgumentException("Peso inválido");
        }
    }

    public void setAltura(double altura) {
        if (altura > 0) {
            this.altura = altura;
        } else {
            throw new IllegalArgumentException("Altura inválida");
        }
    }

    public void setCalculo(){
        if (this.peso != 0) {
            if (this.altura != 0) {
                this.imc = this.peso / (this.altura * this.altura);
            }else{
                throw new IllegalArgumentException("Altura inválida");
            }
        } else {
            throw new IllegalArgumentException("Peso inválido");
        }
    }

}