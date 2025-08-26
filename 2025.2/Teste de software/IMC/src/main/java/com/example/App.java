package com.example;

public class App {
  public static void main(String[] args) {
    double altura = 1.0;
    double[] lista_peso_m = { 20.6, 26.3, 27.7, 31.0, 31.1 };
    double[] lista_peso_f = {19.0, 25.7, 27.2, 32.2, 32.3};
    for (int i = 0; i < lista_peso_m.length; i++) {
      String resultadoM = IMC.main("m", lista_peso_m[i], altura);
      String resultadoF = IMC.main("f", lista_peso_f[i], altura);
      System.out.println("Peso M: " + lista_peso_m[i] + " - " + resultadoM);
      System.out.println("Peso F: " + lista_peso_f[i] + " - " + resultadoF);
    }
  }
}