public class IMC(string genero,int peso,int altura){
    if (genero == "m"){
        list lista_imc = {20.7,26.4,27.8,31.1};
    }else{
        list lista_imc = {19.1,25.8,27.3,32.3};
    }
    float imc = Math.pow(peso/altura,2);
    if (imc<lista_imc[0]){
        return string "Abaixo do peso, com IMC de "+imc;
    }
    if (imc<lista_imc[1]){
        return string "No peso normal, com IMC de "+imc;
    }
    if (imc<lista_imc[2]){
        return string "Marginalmente acima do peso, com IMC de "+imc;
    }
    if (imc<lista_imc[3]){
        return string "Acima do peso ideal, com IMC de "+imc;
    }else{
        return string "Obeso, com IMC de "+imc;
    }
}

public static void main(String[] args) {
    System.out.println(IMC("m",80,180));
}
