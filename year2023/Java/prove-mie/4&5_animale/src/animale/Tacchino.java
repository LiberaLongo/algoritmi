package animale;

public class Tacchino extends Animale {

    public Tacchino(String nome, int anno_nascita) {
        super(nome, anno_nascita);
        this.verso = "goglotta";
        this.zampe = 2;
    }

    @Override
    public String toString() {
        return "Tacchino: " + super.toString();
    }    
}
