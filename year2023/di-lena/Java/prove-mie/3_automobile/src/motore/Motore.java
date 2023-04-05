package motore;

public abstract class Motore {
    protected int cilindrata;
    protected int n_cilindri;

    public Motore(int cilindrata, int n_cilindri) {
        this.cilindrata = cilindrata;
        this.n_cilindri = n_cilindri;
    }

    public int getCilindrata() {
        return cilindrata;
    }
    public void setCilindrata(int cilindrata) {
        this.cilindrata = cilindrata;
    }

    public int getN_cilindri() {
        return n_cilindri;
    }
    public void setN_cilindri(int n_cilindri) {
        this.n_cilindri = n_cilindri;
    }

    public abstract double getPotenza();

    @Override
    public String toString() {
        return "cilindrata: " + this.cilindrata + ", n_cilindri: " + this.n_cilindri;
    }
}
