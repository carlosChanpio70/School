package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import java.lang.reflect.Method;
import org.junit.jupiter.api.Test;

class ValidarPessoaTest {

  private final ValidadorDados validador = new ValidadorDados();

  private String classificar(String nome, int idade, String genero,
                              double peso, double altura) throws Exception {
    Method method = ValidadorDados.class.getDeclaredMethod(
        "validarPessoa", String.class, int.class, String.class, double.class,
        double.class);
    method.setAccessible(true);
    return (String)method.invoke(validador, nome, idade, genero, peso, altura);
  }

  @Test
  void Teste01_Idade_Menos1_Invalida() throws Exception {
    assertEquals("Idade inválida", classificar("x", -1, "M", 1.0, 1.0));
  }

  @Test
  void Teste02_Idade_Zero_Invalida() throws Exception {
    assertEquals("Idade inválida", classificar("x", 0, "M", 1.0, 1.0));
  }

  @Test
  void Teste03_Idade_150_Invalida() throws Exception {
    assertEquals("Idade inválida", classificar("x", 150, "M", 1.0, 1.0));
  }

  @Test
  void Teste04_Idade_151_Invalida() throws Exception {
    assertEquals("Idade inválida", classificar("x", 151, "M", 1.0, 1.0));
  }

  @Test
  void Teste05_Peso_Menos0_1_Invalido() throws Exception {
    assertEquals("Peso deve estar entre 0 e 500 kg", classificar("x", 1, "M", -0.1, 1.0));
  }

  @Test
  void Teste06_Peso_Zero_Valido() throws Exception {
    assertEquals("Peso deve estar entre 0 e 500 kg", classificar("x", 1, "M", 0.0, 1.0));
  }

  @Test
  void Teste07_Peso_500_Invalido() throws Exception {
    assertEquals("Peso deve estar entre 0 e 500 kg", classificar("x", 1, "M", 500.0, 1.0));
  }

  @Test
  void Teste08_Peso_500_1_Invalido() throws Exception {
    assertEquals("Peso deve estar entre 0 e 500 kg", classificar("x", 1, "M", 500.1, 1.0));
  }

  @Test
  void Teste09_Altura_Zero_Invalida() throws Exception {
    assertEquals("Altura deve estar entre 0 e 3 metros", classificar("x", 1, "M", 1.0, 0.0));
  }

  @Test
  void Teste10_Altura_0_01_Valida() throws Exception {
    assertNull(classificar("x", 1, "M", 1.0, 0.01));
  }

  @Test
  void Teste11_Altura_2_99_Valida() throws Exception {
    assertNull(classificar("x", 1, "M", 1.0, 2.99));
  }

  @Test
  void Teste12_Altura_3_Invalida() throws Exception {
    assertEquals("Altura deve estar entre 0 e 3 metros", classificar("x", 1, "M", 1.0, 3.0));
  }

  @Test
  void Teste13_Genero_M_Valido() throws Exception {
    assertNull(classificar("x", 1, "M", 1.0, 1.0) );
  }

  @Test
  void Teste14_Genero_F_Valido() throws Exception {
    assertNull(classificar("x", 1, "F", 1.0, 1.0) );
  }

  @Test
  void Teste15_Genero_X_Invalido() throws Exception {
    assertEquals("Gênero deve ser M ou F", classificar("x", 1, "X", 1.0, 1.0));
  }

  @Test
  void Teste16_Nome_Valido() throws Exception {
    assertNull(classificar("Name", 1, "M", 1.0, 1.0) );
  }

  @Test
  void Teste17_Nome_Nulo_Invalido() throws Exception {
    assertEquals("Nome inválido", classificar(null, 1, "M", 1.0, 1.0));
  }

  @Test
  void Teste18_Nome_Vazio_Invalido() throws Exception {
    assertEquals("Nome inválido", classificar("", 1, "M", 1.0, 1.0));
  }

  @Test
  void Teste19_Nome_101_Caracteres_Invalido() throws Exception {
    assertEquals("Nome inválido", classificar("x".repeat(101), 1, "M", 1.0, 1.0));
  }

  @Test
  void Teste20_Nome_100_Caracteres_Valido() throws Exception {
    assertEquals(null, classificar("x".repeat(100), 1, "M", 1.0, 1.0));
  }
}