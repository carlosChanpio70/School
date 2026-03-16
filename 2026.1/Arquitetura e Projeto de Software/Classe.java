package inicio;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Classe {

    public double sorteio(List<Integer> numeros_sorteados, double valor_aposta) {
        List<Integer> lista_sorteados = new ArrayList<>();
        /*Checks if num is between 1 and 60*/
        for (Integer n: numeros_sorteados){
            if (n < 1 || n > 60){
                return 0.0;
            }
            lista_sorteados.add(n);
        }
        if (lista_sorteados.size() >= 6 && lista_sorteados.size() <= 15) {
            List<Integer> list_random = new ArrayList<>();
            int int_random;
            /* Creates a random_int of random ints between 1 and 60 with a size of 6*/
            while (list_random.size() < 6) {
                int_random = new Random().nextInt(59) + 1;
                if (!list_random.contains(int_random)) {
                    list_random.add(int_random);
                }
            }
            int total =0;
            /* For each num in random_int add 1 to total */
            for (Integer i: numeros_sorteados){
                if (list_random.contains(i)){
                    total++;
                }
            }
            switch (total) {
                case 6 -> {
                    return valor_aposta;
                }
                case 5 -> { 
                    return valor_aposta * 0.2;
                }
                case 4 -> {
                    return valor_aposta * 0.05;
                }
                default -> {      
                    break;
                }
            }
        }
        return 0.0;
    }
}
