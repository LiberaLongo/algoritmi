import motore.Benzina;
import motore.Diesel;
import motore.Metano;

public class Test {
    public static void test() {
        Benzina benzina = new Benzina(100, 10);
        Diesel diesel = new Diesel(100, 10);
        Metano metano = new Metano(100, 10);

        System.out.println(benzina);
        System.out.println(diesel);
        System.out.println(metano);
    }
}
