package animale;

public class Gatto extends Animale{

    public Gatto(String nome, int anno_nascita) {
        super(nome, anno_nascita);
        this.verso = "miagola";
        this.zampe = 4;
    }

    @Override
    public String toString() {
        return "Gatto:\t" + super.toString();
    }
}
