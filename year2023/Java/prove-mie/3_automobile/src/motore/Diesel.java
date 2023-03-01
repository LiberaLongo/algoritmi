package motore;

public class Diesel extends Motore {

    public Diesel(int cilindrata, int n_cilindri) {
        super(cilindrata, n_cilindri);
    }

    @Override
    public double getPotenza() {
        return (cilindrata / n_cilindri) * 0.2;
    }

    @Override
    public String toString() {
        return "Diesel: " + super.toString() + ", potenza: " + this.getPotenza();
    }
}
