import contoCorrente.ContoCorrente;
import contoCorrente.Valuta;

public class Test {
    public static void test() {
        ContoCorrente a = new ContoCorrente();
        ContoCorrente b = new ContoCorrente(10, Valuta.POUND);
        ContoCorrente c = new ContoCorrente(40, Valuta.DOLLAR);

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        a.prelievo(10); //dovrebbe dire errore
        a.versamento(30);
        a.prelievo(10);
        System.out.println(a);
    }
}
