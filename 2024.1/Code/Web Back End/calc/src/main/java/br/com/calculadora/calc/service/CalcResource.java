package br.com.calculadora.calc.service;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/calc")
public class CalcResource {

    @GetMapping("/soma/{valor1}/{valor2}")
    public double soma(@PathVariable double valor1, @PathVariable double valor2) {
        return valor1 + valor2;
    }
    
    @GetMapping("/soma")
    public double somaQP(@RequestParam(name = "v1", required = true) double valor1,
            @RequestParam(name = "v2", required = true) double valor2) {
        return valor1 + valor2;
    }

    @GetMapping("/soma/v2")
    public double somaBP(@RequestBody(required = true) double valor1, @RequestBody(required = true) double valor2) {
        return valor1 + valor2;
    }
    
    @GetMapping("/soma/v1")
    public double somaHP(@RequestHeader(required = true) double valor1, @RequestHeader(required = true) double valor2) {
        return valor1 + valor2;
    }

    @GetMapping({"/nome",""})
    public String retornaNome(){
        return "Serviço rest de calculadora";
    }

}