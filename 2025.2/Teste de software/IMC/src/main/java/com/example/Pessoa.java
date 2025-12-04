package com.example;

public final class Pessoa {
  private String nome;
  private int idade;
  private String genero;
  private double peso;
  private double altura;
  private IMC imc;

  public Pessoa(String nome, int idade, String genero, double peso,
                double altura) {
    setNome(nome);
    setIdade(idade);
    setGenero(genero);
    setPeso(peso);
    setAltura(altura);
    this.imc = new IMC(genero, peso, altura);
  }

  public Pessoa() {}

  public String getNome() { return nome; }

  public void setNome(String nome) {
    if (nome != null && !nome.trim().isEmpty()) {
      this.nome = nome;
    } else {
      throw new IllegalArgumentException("Nome não pode ser vazio");
    }
  }

  public int getIdade() { return idade; }

  public void setIdade(int idade) {
    if (idade > 0 && idade < 150) {
      this.idade = idade;
    } else {
      throw new IllegalArgumentException("Idade inválida");
    }
  }

  public String getGenero() { return genero; }

  public void setGenero(String genero) {
    if (genero != null &&
        (genero.equalsIgnoreCase("M") || genero.equalsIgnoreCase("F"))) {
      this.genero = genero;
    } else {
      throw new IllegalArgumentException("Gênero deve ser M ou F");
    }
  }

  public double getPeso() { return peso; }

  public void setPeso(double peso) {
    if (peso > 0) {
      this.peso = peso;
    } else {
      throw new IllegalArgumentException("Peso inválido");
    }
  }

  public double getAltura() { return altura; }

  public void setAltura(double altura) {
    if (altura > 0) {
      this.altura = altura;
    } else {
      throw new IllegalArgumentException("Altura inválida");
    }
  }

  public IMC getImc() { return imc; }

  public void setImc(IMC imc) { this.imc = imc; }

  public double calcularIMC() { return imc.getIMC(); }

  @Override
  public String toString() {
    return "Pessoa{"
        + "nome='" + nome + '\'' + ", idade=" + idade + ", genero='" + genero +
        '\'' + ", peso=" + peso + ", altura=" + altura +
        ", imc=" + imc.getIMC() + '}';
  }
}
