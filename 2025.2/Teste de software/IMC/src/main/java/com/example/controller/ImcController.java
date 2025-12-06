package com.example.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.ClassificacaoIMC;
import com.example.IMC;
import com.example.Pessoa;
import com.example.ValidadorDados;

@Controller
public class ImcController {
  private static final String ABAIXO_DO_PESO = "Abaixo do peso";
  private static final String PESO_NORMAL = "No peso normal";
  private static final String MARGINALMENTE_ACIMA ="Marginalmente acima do peso";
  private static final String ACIMA_DO_PESO_IDEAL = "Acima do peso ideal";
  private static final String OBESO = "Obeso";

  @GetMapping("/")
  public String index() {
    // redirect to static index.html so no view resolver is required
    return "redirect:/index.html";
  }

  @PostMapping("/calcular")
  @ResponseBody
  public ImcResponse calcularImc(@RequestParam String genero,
                                 @RequestParam double peso,
                                 @RequestParam double altura) {

    try {
      // Validate input
      if (!ValidadorDados.validarGenero(genero)) {
        return new ImcResponse(false, 0, null, "Gênero inválido");
      }
      if (!ValidadorDados.validarPeso(peso)) {
        return new ImcResponse(false, 0, null,
                               "Peso deve estar entre 0 e 500 kg");
      }
      if (!ValidadorDados.validarAltura(altura)) {
        return new ImcResponse(false, 0, null,
                               "Altura deve estar entre 0 e 3 metros");
      }

      IMC imc = new IMC(genero, peso, altura);
      double imcValue = imc.getIMC();
      String classification = classificarIMC(genero, imcValue);

      return new ImcResponse(true, imcValue, classification, null);
    } catch (IllegalArgumentException e) {
      return new ImcResponse(false, 0, null, e.getMessage());
    }
  }

  @PostMapping("/validar-pessoa")
  @ResponseBody
  public ValidationResponse
  validarPessoa(@RequestParam String nome, @RequestParam int idade,
                @RequestParam String genero, @RequestParam double peso,
                @RequestParam double altura) {
    try {
      String erro =
          ValidadorDados.validarPessoa(nome, idade, genero, peso, altura);
      if (erro != null) {
        return new ValidationResponse(false, erro);
      }

      // Create Pessoa object if validation passes
      Pessoa pessoa = new Pessoa(nome, idade, genero, peso, altura);
      return new ValidationResponse(true, "Dados válidos: " + pessoa.getNome());
    } catch (IllegalArgumentException e) {
      return new ValidationResponse(false, e.getMessage());
    }
  }

  @GetMapping("/classificacoes")
  @ResponseBody
  public ClassificacaoResponse obterClassificacoes() {
    ClassificacaoIMC[] masculino = {
        new ClassificacaoIMC(ABAIXO_DO_PESO, 0, 20.7),
        new ClassificacaoIMC(PESO_NORMAL, 20.7, 26.4),
        new ClassificacaoIMC(MARGINALMENTE_ACIMA, 26.4, 27.8),
        new ClassificacaoIMC(ACIMA_DO_PESO_IDEAL, 27.8, 31.1),
        new ClassificacaoIMC(OBESO, 31.1, 100)};

    ClassificacaoIMC[] feminino = {
        new ClassificacaoIMC(ABAIXO_DO_PESO, 0, 19.1),
        new ClassificacaoIMC(PESO_NORMAL, 19.1, 25.8),
        new ClassificacaoIMC(MARGINALMENTE_ACIMA, 25.8, 27.3),
        new ClassificacaoIMC(ACIMA_DO_PESO_IDEAL, 27.3, 32.3),
        new ClassificacaoIMC(OBESO, 32.3, 100)};

    return new ClassificacaoResponse(masculino, feminino);
  }

  private String classificarIMC(String genero, double imc) {
    double[] ranges;

    if ("M".equalsIgnoreCase(genero)) {
      ranges = new double[] {20.7, 26.4, 27.8, 31.1};
    } else if ("F".equalsIgnoreCase(genero)) {
      ranges = new double[] {19.1, 25.8, 27.3, 32.3};
    } else {
      return "Gênero inválido";
    }

    if (imc < ranges[0]) {
      return ABAIXO_DO_PESO;
    } else if (imc < ranges[1]) {
      return PESO_NORMAL;
    } else if (imc < ranges[2]) {
      return MARGINALMENTE_ACIMA;
    } else if (imc < ranges[3]) {
      return ACIMA_DO_PESO_IDEAL;
    } else {
      return OBESO;
    }
  }
}