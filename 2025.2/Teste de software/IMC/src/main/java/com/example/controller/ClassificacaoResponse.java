package com.example.controller;

import com.example.ClassificacaoIMC;

public class ClassificacaoResponse {
  private ClassificacaoIMC[] masculino;
  private ClassificacaoIMC[] feminino;

  public ClassificacaoResponse(ClassificacaoIMC[] masculino,
                               ClassificacaoIMC[] feminino) {
    this.masculino = masculino;
    this.feminino = feminino;
  }

  public ClassificacaoIMC[] getMasculino() { return masculino; }

  public void setMasculino(ClassificacaoIMC[] masculino) {
    this.masculino = masculino;
  }

  public ClassificacaoIMC[] getFeminino() { return feminino; }

  public void setFeminino(ClassificacaoIMC[] feminino) {
    this.feminino = feminino;
  }
}
