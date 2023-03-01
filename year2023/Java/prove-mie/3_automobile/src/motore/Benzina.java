package motore;

public class Benzina extends Motore {

    public Benzina(int cilindrata, int n_cilindri) {
        super(cilindrata, n_cilindri);
    }

    @Override
    public double getPotenza() {
        return (cilindrata / n_cilindri) * 0.1;
    }

    @Override
    public String toString() {
        return "Benzina: " + super.toString() + ", potenza: " + this.getPotenza();
    }
}
