package com.example;

public class IMC {
    public static String main(String genero, double peso, double altura) {
        double[] lista_imc;
        if (genero.equals("m")) {
            lista_imc = new double[] { 20.7, 26.4, 27.8, 31.1 };
        } else {
            lista_imc = new double[] { 19.1, 25.8, 27.3, 32.3 };
        }
        double imc = peso / (altura * altura);
        if (imc < lista_imc[0]) {
            return "Abaixo do peso, com IMC de " + imc;
        }
        if (imc < lista_imc[1]) {
            return "No peso normal, com IMC de " + imc;
        }
        if (imc < lista_imc[2]) {
            return "Marginalmente acima do peso, com IMC de " + imc;
        }
        if (imc < lista_imc[3]) {
            return "Acima do peso ideal, com IMC de " + imc;
        } else {
            return "Obeso, com IMC de " + imc;
        }
    }
}