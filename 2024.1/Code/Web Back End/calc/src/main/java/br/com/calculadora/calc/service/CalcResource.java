package br.com.calculadora.calc.service;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/calc")
public class CalcResource {

    @GetMapping("/imc")
    public double imc(
        @RequestHeader double peso,
        @RequestHeader double altura
    ) {
        return peso / (altura*altura);
    }

    @GetMapping("/equacao/{a}/{b}")
    public double calculaequacao1Grau(
        @PathVariable(required = true) double a,
        @PathVariable(required = true) double b,
        @RequestParam(required = true) double c) {
        return (c+b)/a;
    }

    @PostMapping("/soma")
    public String testaPost(@RequestBody(required = true) double v1) {
        return "Salvou no Banco " + v1;
    }

    @PostMapping("/soma/{v2}")
    public String testaPost( @RequestBody(required = true) double v1,
            @PathVariable double v2) {
        return "Salvou no Banco" + (v1 + v2);
    }

    @DeleteMapping("/soma/{id}")
    public String apagarQC(@PathVariable double id) {
        return id + "apagado";
    }

    @PutMapping("/soma/{id}")
    public String putting(@PathVariable double id) {
        return "alterando mais de um campo" + id;
    }
    
    @PatchMapping("/soma/{id}")
    public String patch(@PathVariable double id) {
        return "alterando um campo" + id ;
    }

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