package com.example.controller;

import java.lang.reflect.Method;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class IMCControllerTest {

  private final ImcController controller = new ImcController();

  private String classificar(String genero, double peso) throws Exception {
    Method method = ImcController.class.getDeclaredMethod(
        "classificarIMC", String.class, double.class);
    method.setAccessible(true);
    return (String)method.invoke(controller, genero, peso);
  }

  @Test
  void T1_M_20_6_AbaixoDoPeso() throws Exception {
    assertEquals("Abaixo do peso", classificar("M", 20.6));
  }
  @Test
  void T2_M_20_7_PesoNormal() throws Exception {
    assertEquals("No peso normal", classificar("M", 20.7));
  }
  @Test
  void T3_M_26_3_PesoNormal() throws Exception {
    assertEquals("No peso normal", classificar("M", 26.3));
  }
  @Test
  void T4_M_26_4_MarginalmenteAcima() throws Exception {
    assertEquals("Marginalmente acima do peso", classificar("M", 26.4));
  }
  @Test
  void T5_M_27_7_MarginalmenteAcima() throws Exception {
    assertEquals("Marginalmente acima do peso", classificar("M", 27.7));
  }
  @Test
  void T6_M_27_8_AcimaDoPesoIdeal() throws Exception {
    assertEquals("Acima do peso ideal", classificar("M", 27.8));
  }
  @Test
  void T7_M_31_0_AcimaDoPesoIdeal() throws Exception {
    assertEquals("Acima do peso ideal", classificar("M", 31.0));
  }
  @Test
  void T8_M_31_1_Obeso() throws Exception {
    assertEquals("Obeso", classificar("M", 31.1));
  }
  @Test
  void T9_M_19_0_AbaixoDoPeso() throws Exception {
    assertEquals("Abaixo do peso", classificar("M", 19.0));
  }

  @Test
  void T10_F_19_1_PesoNormal() throws Exception {
    assertEquals("No peso normal", classificar("F", 19.1));
  }
  @Test
  void T11_F_25_7_PesoNormal() throws Exception {
    assertEquals("No peso normal", classificar("F", 25.7));
  }
  @Test
  void T12_F_25_8_MarginalmenteAcima() throws Exception {
    assertEquals("Marginalmente acima do peso", classificar("F", 25.8));
  }
  @Test
  void T13_F_27_2_MarginalmenteAcima() throws Exception {
    assertEquals("Marginalmente acima do peso", classificar("F", 27.2));
  }
  @Test
  void T14_F_27_3_AcimaDoPesoIdeal() throws Exception {
    assertEquals("Acima do peso ideal", classificar("F", 27.3));
  }
  @Test
  void T15_F_32_2_AcimaDoPesoIdeal() throws Exception {
    assertEquals("Acima do peso ideal", classificar("F", 32.2));
  }
  @Test
  void T16_F_32_3_Obeso() throws Exception {
    assertEquals("Obeso", classificar("F", 32.3));
  }
  @Test
  void T17_X_1_Invalido() throws Exception {
    assertEquals("Gênero inválido", classificar("X", 1.0));
  }
}