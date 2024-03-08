package br.edu.uniacademia.TodoApi.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper=false)
public class Administrador extends Usuario {
 
    private Etipo tipoAdmin;


    public Administrador(String nome, String login, String senha) {
        setNome(nome);
        setLogin(login);
        setSenha(senha);
        this.saldo = 0;
    }

}
