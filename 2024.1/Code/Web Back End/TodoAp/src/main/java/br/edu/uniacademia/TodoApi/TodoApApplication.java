package br.edu.uniacademia.TodoApi;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import br.edu.uniacademia.TodoApi.model.Administrador;
import br.edu.uniacademia.TodoApi.model.Etipo;

@SpringBootApplication
public class TodoApApplication implements CommandLineRunner{

	public static void main(String[] args) {
		SpringApplication.run(TodoApApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("Bem vindo ao Spring!");
		Administrador adm = new Administrador("Carlos","cs","123");
		adm.setTipoAdmin(Etipo.AdminFull);
		adm.setEmail("ze@ze");
		adm.setSaldo(100);
		System.out.println("Olá "+adm.GetNome());
	}

}
