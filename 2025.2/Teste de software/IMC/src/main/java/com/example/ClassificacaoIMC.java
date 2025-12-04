package com.example;

public final class ClassificacaoIMC {
  private String classificacao;
  private double imcMinimo;
  private double imcMaximo;

  public ClassificacaoIMC(String classificacao, double imcMinimo,
                          double imcMaximo) {
    setClassificacao(classificacao);
    setImcMinimo(imcMinimo);
    setImcMaximo(imcMaximo);
  }

  public ClassificacaoIMC() {}

  public String getClassificacao() { return classificacao; }

  public void setClassificacao(String classificacao) {
    if (classificacao != null && !classificacao.trim().isEmpty()) {
      this.classificacao = classificacao;
    } else {
      throw new IllegalArgumentException("Classificação não pode ser vazia");
    }
  }

  public double getImcMinimo() { return imcMinimo; }

  public void setImcMinimo(double imcMinimo) {
    if (imcMinimo >= 0) {
      this.imcMinimo = imcMinimo;
    } else {
      throw new IllegalArgumentException("IMC mínimo não pode ser negativo");
    }
  }

  public double getImcMaximo() { return imcMaximo; }

  public void setImcMaximo(double imcMaximo) {
    if (imcMaximo >= 0) {
      this.imcMaximo = imcMaximo;
    } else {
      throw new IllegalArgumentException("IMC máximo não pode ser negativo");
    }
  }

  public boolean estaNoIntervalo(double imc) {
    return imc >= imcMinimo && imc < imcMaximo;
  }

  @Override
  public String toString() {
    return "ClassificacaoIMC{"
        + "classificacao='" + classificacao + '\'' +
        ", imcMinimo=" + imcMinimo + ", imcMaximo=" + imcMaximo + '}';
  }
}
