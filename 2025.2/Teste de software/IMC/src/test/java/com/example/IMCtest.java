package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

import org.junit.jupiter.api.Test;

public class IMCtest {

	@Test
	public void testSetGeneroFail(){
		try {
			IMC imc = new IMC();
			imc.setGenero("w");
			fail();
		} catch (IllegalArgumentException e) {
			assertEquals("Genero inválido", e.getMessage());
		}
	}

	@Test
	public void testSetPesoFail(){
		try {
			IMC imc = new IMC();
			imc.setPeso(0);
			fail();
		} catch (IllegalArgumentException e) {
			assertEquals("Peso inválido", e.getMessage());
		}
	}

	@Test
	public void testSetAlturaFail(){
		try {
			IMC imc = new IMC();
			imc.setAltura(0);
			fail();
		} catch (IllegalArgumentException e) {
			assertEquals("Altura inválida", e.getMessage());
		}
	}

	@Test
	public void testSetIMCFailNoWeight(){
		try {
			IMC imc = new IMC();
			imc.setIMC();
			fail();
		} catch (IllegalArgumentException e) {
			assertEquals("Peso inválido", e.getMessage());
		}
	}

	@Test
	public void testSetIMCFailNoHeight(){
		try {
			IMC imc = new IMC();
			imc.setPeso(1);
			imc.setIMC();
			fail();
		} catch (IllegalArgumentException e) {
			assertEquals("Altura inválida", e.getMessage());
		}
	}

	private void categories(String gender, double weight, String expectedCategory) {
        double height = 1.0;
        IMC imc = new IMC(gender,weight,height);
        String result = imc.getResults();
        assertEquals(expectedCategory, result);
    }

    @Test
    public void testMaleCategories() {
        double[] lista_peso_m = { 20.6, 26.3, 27.7, 31.0, 31.1 };
        categories("m", lista_peso_m[0], "Abaixo do peso");
        categories("m", lista_peso_m[1], "No peso normal");
        categories("m", lista_peso_m[2], "Marginalmente acima do peso");
        categories("m", lista_peso_m[3], "Acima do peso ideal");
        categories("m", lista_peso_m[4], "Obeso");
    }

    @Test
    public void testFemaleCategories() {
        double[] lista_peso_f = {19.0, 25.7, 27.2, 32.2, 32.3};
        categories("f", lista_peso_f[0], "Abaixo do peso");
        categories("f", lista_peso_f[1], "No peso normal");
        categories("f", lista_peso_f[2], "Marginalmente acima do peso");
        categories("f", lista_peso_f[3], "Acima do peso ideal");
        categories("f", lista_peso_f[4], "Obeso");
    }
}
