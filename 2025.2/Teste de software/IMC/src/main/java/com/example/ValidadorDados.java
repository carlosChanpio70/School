package com.example;

public final class ValidadorDados {

  ValidadorDados() {
    // Classe utilitária - não instancia
  }

  public static boolean validarPeso(double peso) {
    return peso > 0 && peso < 500;
  }

  public static boolean validarAltura(double altura) {
    return altura > 0 && altura < 3;
  }

  public static boolean validarIdade(int idade) {
    return idade > 0 && idade < 150;
  }

  public static boolean validarNome(String nome) {
    return nome != null && !nome.trim().isEmpty() && nome.length() <= 100;
  }

  public static boolean validarGenero(String genero) {
    return genero != null &&
        (genero.equalsIgnoreCase("M") || genero.equalsIgnoreCase("F"));
  }

  public static boolean validarIMC(double imc) { return imc >= 0 && imc < 100; }

  public static String validarPessoa(String nome, int idade, String genero,
                                     double peso, double altura) {
    if (!validarNome(nome)) {
      return "Nome inválido";
    }
    if (!validarIdade(idade)) {
      return "Idade inválida";
    }
    if (!validarGenero(genero)) {
      return "Gênero deve ser M ou F";
    }
    if (!validarPeso(peso)) {
      return "Peso deve estar entre 0 e 500 kg";
    }
    if (!validarAltura(altura)) {
      return "Altura deve estar entre 0 e 3 metros";
    }
    return null;
  }

  public static double limitarCasasDecimais(double valor, int casas) {
    if (casas < 0) {
      throw new IllegalArgumentException(
          "Número de casas decimais não pode ser negativo");
    }
    double multiplicador = Math.pow(10, casas);
    return Math.round(valor * multiplicador) / multiplicador;
  }
}
