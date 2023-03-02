import animale.*;

public class Test {
    public static void test() {
        Gatto micia = new Gatto("Lulù", 2017);
        Gatto pucci = new Gatto("Pucci", 2012);
        Cane otto = new Cane("Otto", 2020);
        Tacchino gluglu = new Tacchino("Sio", 2023);
        System.out.println(micia);
        System.out.println(pucci);
        System.out.println(otto);
        System.out.println(gluglu);
        System.out.println("Io ho una gatta di nome " + micia.getNome() + " che non sembra " + micia.getVerso() + "re molto bene...");
        System.out.print("Il gatto di mia nonna si chiama " + pucci.getNome());
        if(pucci.compareTo(micia) > 0)
            System.out.println(" lui è il più vecchio dei due.");
        else
            System.out.println(" lei dovrebbe non essere più vecchia.");
        System.out.println("Il cane della cugina ha " + otto.getAge() + " anni ed è il più giovane.");
        System.out.print("Questi animali hanno in comune di avere ");
        if(micia.getZampe() == otto.getZampe())
            System.out.println(pucci.getZampe() + " zampe.");
        System.out.println("Mentre il tacchino ha solo " + gluglu.getZampe() + " e " + gluglu.getVerso() + ".");
    }
}
