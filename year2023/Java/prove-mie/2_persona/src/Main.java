import java.time.LocalDate;
import java.time.Month;

import persona.ImpiegatiDemo;
import persona.Impiegato;
import persona.Persona;
import persona.Stagista;

public class Main {
    public static void main(String[] args) {
        Persona Libera = new Persona("Libera", LocalDate.of(1997, Month.JUNE, 3));
        System.out.println("Hi! I'm "+ Libera);

        Impiegato Renzo = new Impiegato("Renzo", LocalDate.of(1964, Month.FEBRUARY, 19), 2242);
        Impiegato Pif = new Impiegato("Pif", LocalDate.of(1972, Month.JUNE, 4), 4242);
        Stagista Luigi = new Stagista("Luigi", LocalDate.of(2000, Month.JUNE, 28), 1000, 424242, 100);

        Impiegato[] array = {Renzo, Pif, Luigi};

        for(int i = 0; i < array.length; i++) System.out.println(array[i]);

        System.out.println("I found " + ImpiegatiDemo.cercaGiovane(array) + " as younger employer");
    }
}