package br.edu.uniacademia.TodoApi.model;

import java.time.LocalDateTime;
import lombok.NoArgsConstructor;

@NoArgsConstructor
public class Usuario {
    
    //Atributes
    private String nome, login, senha, email;
    protected double saldo;
    private LocalDateTime dataUltimoAcesso;

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    
    public String GetNome() {
        return this.nome;
    }

    public String getLogin() {
        return this.login;
    }

    public String getSenha() {
        return this.senha;
    }

    public String getEmail() {
        return this.email;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public LocalDateTime getDataUltimoAcesso() {
        return this.dataUltimoAcesso;
    }
    

}
