package persona;

import java.time.LocalDate; // import the LocalDate class

public class Persona {

    private String nome;
    LocalDate nascita;

    public Persona(String nome, LocalDate nascita) {
        this.nome = nome;
        this.nascita = nascita;
    }    

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public LocalDate getNascita() {
        return nascita;
    }
    public void setNascita(LocalDate nascita) {
        this.nascita = nascita;
    }

    public String toString() {
        return nome + " " + nascita;
    }    

    public int compareTo(Persona p) {
        return this.nascita.compareTo(p.getNascita());
    }
}
