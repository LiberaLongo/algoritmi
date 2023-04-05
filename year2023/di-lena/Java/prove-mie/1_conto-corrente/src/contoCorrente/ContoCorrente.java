package contoCorrente;

public class ContoCorrente extends Saldo {

    private Valuta valuta;
    
    public ContoCorrente() {
        super();
        this.valuta = Valuta.EURO;
    }
    public ContoCorrente(int saldo) {
        super(saldo);
        this.valuta = Valuta.EURO;
    }
    public ContoCorrente(int saldo, Valuta valuta) {
        super(saldo);
        this.valuta = valuta;
    }
    
    @Override
    public String toString() {
        return super.toString() + " " + this.valuta.toString();
    }
}