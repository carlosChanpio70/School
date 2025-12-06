package com.example;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public final class HistoricoCalculos {
  private String idPessoa;
  private final List<RegistroCalculo> registros;

  public HistoricoCalculos(String idPessoa) {
    setIdPessoa(idPessoa);
    this.registros = new ArrayList<>();
  }

  public HistoricoCalculos() { this.registros = new ArrayList<>(); }

  public String getIdPessoa() { return idPessoa; }

  public void setIdPessoa(String idPessoa) {
    if (idPessoa != null && !idPessoa.trim().isEmpty()) {
      this.idPessoa = idPessoa;
    } else {
      throw new IllegalArgumentException("ID da pessoa não pode ser vazio");
    }
  }

  public List<RegistroCalculo> getRegistros() {
    return new ArrayList<>(registros);
  }

  public void adicionarRegistro(double peso, double altura, double imc,
                                String classificacao) {
    RegistroCalculo registro =
        new RegistroCalculo(peso, altura, imc, classificacao);
    registros.add(registro);
  }

  public int getTotalCalculos() { return registros.size(); }

  public RegistroCalculo getUltimoCalculo() {
    if (registros.isEmpty()) {
      return null;
    }
    return registros.get(registros.size() - 1);
  }

  public double getImcMedio() {
    if (registros.isEmpty()) {
      return 0;
    }
    double soma = 0;
    for (RegistroCalculo registro : registros) {
      soma += registro.getImc();
    }
    return soma / registros.size();
  }

  public void limparHistorico() { registros.clear(); }

  @Override
  public String toString() {
    return "HistoricoCalculos{"
        + "idPessoa='" + idPessoa + '\'' +
        ", totalRegistros=" + registros.size() + '}';
  }

  // Classe interna para representar um registro de cálculo
  public static final class RegistroCalculo {
    private final double peso;
    private final double altura;
    private final double imc;
    private final String classificacao;
    private final LocalDateTime dataHora;

    public RegistroCalculo(double peso, double altura, double imc,
                           String classificacao) {
      this.peso = peso;
      this.altura = altura;
      this.imc = imc;
      this.classificacao = classificacao;
      this.dataHora = LocalDateTime.now();
    }

    public double getPeso() { return peso; }

    public double getAltura() { return altura; }

    public double getImc() { return imc; }

    public String getClassificacao() { return classificacao; }

    public LocalDateTime getDataHora() { return dataHora; }

    @Override
    public String toString() {
      return "RegistroCalculo{"
          + "peso=" + peso + ", altura=" + altura + ", imc=" + imc +
          ", classificacao='" + classificacao + '\'' +
          ", dataHora=" + dataHora + '}';
    }
  }
}
