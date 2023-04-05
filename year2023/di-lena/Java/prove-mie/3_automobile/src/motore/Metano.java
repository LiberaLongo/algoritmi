package motore;

public class Metano extends Motore {

    public Metano(int cilindrata, int n_cilindri) {
        super(cilindrata, n_cilindri);
    }

    @Override
    public double getPotenza() {
        return ((cilindrata * 0.8) / n_cilindri) * 0.25;
    }

    @Override
    public String toString() {
        return "Metano: " + super.toString() + ", potenza: " + this.getPotenza();
    }
}
