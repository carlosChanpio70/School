package com.example;

public class Exame {
  double volume;

  Exame(double volume) { setVolume(volume); }

  Exame() {}

  public double getVolume() { return volume; }

  public void setVolume(double volume) { this.volume = volume; }

  public String Triglicerides() {
    String result;
    if (this.volume < 150) {
      result = "Nivel desejável";
    } else if (150 <= this.volume & this.volume < 200) {
      result = "Nivel limitrofe";
    } else if (200 <= this.volume & this.volume < 500) {
      result = "Nivel alto";
    } else {
      result = "Nivel muito alto";
    }
    return result;
  }

  public String Colesterol_Total() {
    String result;
    if (this.volume < 200) {
      result = "Desejável";
    } else if (200 <= this.volume & this.volume < 240) {
      result = "Limitrofe";
    } else {
      result = "Nivel alto";
    }
    return result;
  }

  public String Colesterol_HDL() {
    String result;
    if (this.volume < 40) {
      result = "Baixo";
    } else if (40 <= this.volume & this.volume <= 60) {
      result = "Normal";
    } else {
      result = "Desejável";
    }
    return result;
  }

  public String Colesterol_LDL() {
    String result;
    if (volume < 100) {
      result = "Ótimo";
    } else if (100 <= this.volume & this.volume < 130) {
      result = "Desejável";
    } else if (130 <= this.volume & this.volume < 160) {
      result = "Limitrofe";
    } else if (160 <= this.volume & this.volume < 190) {
      result = "Alto";
    } else {
      result = "Muito alto";
    }
    return result;
  }

  public String Colesterol_VLDL() {
    String result;
    if (this.volume < 30) {
      result = "Nivel desejável";
    } else if (30 <= this.volume & this.volume <= 40) {
      result = "Nivel limítrofe";
    } else {
      result = "Nivel elevado";
    }
    return result;
  }

  public String Glicose() {
    String result;
    if (this.volume < 60) {
      result = "Hipoglicemia";
    } else if (60 <= this.volume & this.volume < 100) {
      result = "Desejável";
    } else if (100 <= this.volume & this.volume <= 125) {
      result = "Glicemia de jejum inapropriada";
    } else {
      result = "Diabetes";
    }
    return result;
  }
}
