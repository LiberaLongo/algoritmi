package contoCorrente;

public class Saldo {

    private int saldo;

    public Saldo() {
        //Aprire un conto corrente vuoto (con 0 euro)
        this.saldo = 0;
    }
    public Saldo(int money) {
        //Aprire conto corrente con X euro
        this.saldo = money;
    }
    public void versamento(int money) {
        //Versare X euro nel conto
        this.saldo += money;
    }
    public void prelievo(int money) {
        //Prelevare X euro dal conto
        if(money >= this.saldo) {
            System.out.println("Ehi! You cannot pick up more coins than u have!");
            return ;
        }
        this.saldo -= money;
    }
    public String toString() {
        //Stampare un messaggio con il saldo attuale (nel metodo toString() )
        return String.valueOf(this.saldo);
    }
}
