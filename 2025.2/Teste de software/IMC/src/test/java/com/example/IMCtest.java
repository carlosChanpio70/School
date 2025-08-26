package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class IMCtest {
    
  private void testIMC(String gender, double weight, String expectedCategory) {
        double height = 1.0; // Height = 1m simplifies BMI to weight
        String result = IMC.main(gender, weight, height);
        assertEquals(expectedCategory + ", com IMC de " + weight, result);
    }

    @Test
    public void testMaleBMICategories() {
        double[] lista_peso_m = { 20.6, 26.3, 27.7, 31.0, 31.1 };
        testIMC("m", lista_peso_m[0], "Abaixo do peso");
        testIMC("m", lista_peso_m[1], "No peso normal");
        testIMC("m", lista_peso_m[2], "Marginalmente acima do peso");
        testIMC("m", lista_peso_m[3], "Acima do peso ideal");
        testIMC("m", lista_peso_m[4], "Obeso");
    }

    @Test
    public void testFemaleBMICategories() {
        double[] lista_peso_f = {19.0, 25.7, 27.2, 32.2, 32.3};
        testIMC("f", lista_peso_f[0], "Abaixo do peso"); // BMI < 19.1
        testIMC("f", lista_peso_f[1], "No peso normal"); // 19.1 ≤ BMI < 25.8
        testIMC("f", lista_peso_f[2], "Marginalmente acima do peso"); // 25.8 ≤ BMI < 27.3
        testIMC("f", lista_peso_f[3], "Acima do peso ideal"); // 27.3 ≤ BMI < 32.3
        testIMC("f", lista_peso_f[4], "Obeso"); // BMI ≥ 32.3
    }
}
