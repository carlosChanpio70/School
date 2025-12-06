package com.example;

public final class Genero {
  private String sgenero;
  private double[] imclista;

  public Genero(String genero) {
    setGenero(genero);
    setIMCLista();
  }

  public String getGenero() { return sgenero; }

  public double[] getIMCLista() { return imclista; }

  public void setGenero(String genero) {
    this.sgenero = genero.toUpperCase().trim();
  }

  public void setIMCLista() {
    switch (this.sgenero) {
    case "M":
      this.imclista = new double[] {20.7, 26.4, 27.8, 31.1};
      break;
    case "F":
      this.imclista = new double[] {19.1, 25.8, 27.3, 32.3};
      break;
    default:
      throw new IllegalArgumentException("Genero inválido");
    }
  }
}
