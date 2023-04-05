package persona;

import java.time.LocalDate;

public class Stagista extends Impiegato {

    private int idStage;
    private int presenze;

    public Stagista(String nome, LocalDate nascita, int stipendio, int idStage, int presenze) {
        super(nome, nascita, stipendio);
        this.idStage = idStage;
        this.presenze = presenze;
    }

    public int getIdStage() {
        return idStage;
    }
    public void setIdStage(int idStage) {
        this.idStage = idStage;
    }

    public int getPresenze() {
        return presenze;
    }
    public void setPresenze(int presenze) {
        this.presenze = presenze;
    }

    @Override
    public String toString() {
        return super.toString() + ", stage = " + idStage + ", presenze = " + presenze;
    } 
    
}
