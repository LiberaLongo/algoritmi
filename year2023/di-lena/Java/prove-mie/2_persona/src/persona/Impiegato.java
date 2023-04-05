package persona;

import java.time.LocalDate;

public class Impiegato extends Persona{

    private int stipendio;

    public Impiegato(String nome, LocalDate nascita, int stipendio) {
        super(nome, nascita);
        this.stipendio = stipendio;
    }

    public int getStipendio() {
        return stipendio;
    }
    public void setStipendio(int stipendio) {
        this.stipendio = stipendio;
    }

    @Override
    public String toString() {
        return super.toString() + ", stipendio = " + stipendio;
    }
    
}
