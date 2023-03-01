package animale;

public class Cane extends Animale {

    public Cane(String nome, int anno_nascita) {
        super(nome, anno_nascita);
        this.verso = "abbaia";
        this.zampe = 4;
    }

    @Override
    public String toString() {
        return "Cane:\t" + super.toString();
    }
}
