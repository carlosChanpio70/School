package br.edu.uniacademia.TodoApi.model;

import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Data
public class Tarefa {
    
    private String descrição;
    private LocalDateTime dataCriacao, dataPrevisao, dataEncerramento;
    private Usuario responsavel;
    private ECategoria categoria;

}
