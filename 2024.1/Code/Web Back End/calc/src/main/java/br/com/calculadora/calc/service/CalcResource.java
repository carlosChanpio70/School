package br.com.calculadora.calc.service;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/calc")
public class CalcResource {

    @GetMapping("/soma/{valor1}/{valor2}")
    public double soma(@PathVariable double valor1, @PathVariable double valor2){
        return valor1 + valor2;
    }

    @GetMapping({"/nome",""})
    public String retornaNome(){
        return "Serviço rest de calculadora";
    }

}