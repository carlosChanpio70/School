package br.uni.unibet.UniBet.controller;

import java.util.ArrayList;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/desenv")
public class DesenvolvimentoController {

    static ArrayList<String> desenvolvedores;
    static {
        desenvolvedores = new ArrayList<>();
        desenvolvedores.add("Zezin da Silva");
        desenvolvedores.add("Lucas Ferreira");
        desenvolvedores.add("João Pedro");
    }
    
    @GetMapping("/time")
    public String getDesenvTime() {
        String nome = "";
        for (String n : desenvolvedores) {
            nome += n+"; ";
        }
        return nome;
    }

    @GetMapping("/time/{id}")
    public String getDesenvTime2(@PathVariable int id) {
        if (id >= 1 && id <= desenvolvedores.size()) {
            return desenvolvedores.get(id - 1);
        } else {
            return "Desenvolvedor não encontrado";
        }
    }

}