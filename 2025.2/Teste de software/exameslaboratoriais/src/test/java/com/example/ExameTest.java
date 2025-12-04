package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class ExameTest {
@SuppressWarnings("unused")
@BeforeEach
  public void setUp() {
    Exame exame = new Exame();
  }

  @Test
  public void testTriglicerides() {
    Exame exame = new Exame();
    exame.setVolume(149);
    assertEquals("Nivel desejável", exame.Triglicerides());
    exame.setVolume(150);
    assertEquals("Nivel limitrofe", exame.Triglicerides());
    exame.setVolume(199);
    assertEquals("Nivel limitrofe", exame.Triglicerides());
    exame.setVolume(200);
    assertEquals("Nivel alto", exame.Triglicerides());
    exame.setVolume(499);
    assertEquals("Nivel alto", exame.Triglicerides());
    exame.setVolume(500);
    assertEquals("Nivel muito alto", exame.Triglicerides());
  }

  @Test
  public void testColesterol_Total() {
    Exame exame = new Exame();
    exame.setVolume(199);
    assertEquals("Desejável", exame.Colesterol_Total());
    exame.setVolume(200);
    assertEquals("Limitrofe", exame.Colesterol_Total());
    exame.setVolume(239);
    assertEquals("Limitrofe", exame.Colesterol_Total());
    exame.setVolume(240);
    assertEquals("Nivel alto", exame.Colesterol_Total());
  }

  @Test
  public void testColesterol_HDL() {
    Exame exame = new Exame();
    exame.setVolume(39);
    assertEquals("Baixo", exame.Colesterol_HDL());
    exame.setVolume(40);
    assertEquals("Normal", exame.Colesterol_HDL());
    exame.setVolume(60);
    assertEquals("Normal", exame.Colesterol_HDL());
    exame.setVolume(61);
    assertEquals("Desejável", exame.Colesterol_HDL());
  }

  @Test
  public void testColesterol_LDL() {
    Exame exame = new Exame();
    exame.setVolume(99);
    assertEquals("Ótimo", exame.Colesterol_LDL());
    exame.setVolume(100);
    assertEquals("Desejável", exame.Colesterol_LDL());
    exame.setVolume(129);
    assertEquals("Desejável", exame.Colesterol_LDL());
    exame.setVolume(130);
    assertEquals("Limitrofe", exame.Colesterol_LDL());
    exame.setVolume(159);
    assertEquals("Limitrofe", exame.Colesterol_LDL());
    exame.setVolume(160);
    assertEquals("Alto", exame.Colesterol_LDL());
    exame.setVolume(189);
    assertEquals("Alto", exame.Colesterol_LDL());
    exame.setVolume(190);
    assertEquals("Muito alto", exame.Colesterol_LDL());
  }

  @Test
  public void testColesterol_VLDL() {
    Exame exame = new Exame();
    exame.setVolume(29);
    assertEquals("Nivel desejável", exame.Colesterol_VLDL());
    exame.setVolume(30);
    assertEquals("Nivel limítrofe", exame.Colesterol_VLDL());
    exame.setVolume(40);
    assertEquals("Nivel limítrofe", exame.Colesterol_VLDL());
    exame.setVolume(41);
    assertEquals("Nivel elevado", exame.Colesterol_VLDL());
  }

  @Test
  public void testGlicose() {
    Exame exame = new Exame();
    exame.setVolume(59);
    assertEquals("Hipoglicemia", exame.Glicose());
    exame.setVolume(60);
    assertEquals("Desejável", exame.Glicose());
    exame.setVolume(99);
    assertEquals("Desejável", exame.Glicose());
    exame.setVolume(100);
    assertEquals("Glicemia de jejum inapropriada", exame.Glicose());
    exame.setVolume(125);
    assertEquals("Glicemia de jejum inapropriada", exame.Glicose());
    exame.setVolume(126);
    assertEquals("Diabetes", exame.Glicose());
  }
}
