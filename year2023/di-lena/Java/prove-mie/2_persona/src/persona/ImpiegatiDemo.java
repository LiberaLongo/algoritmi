package persona;

public class ImpiegatiDemo {
    public static Persona cercaGiovane(Persona[] array) {
        Persona minAge = array[0];
        for(Persona p : array) {
            if(p.compareTo(minAge) > 0) //younger
                minAge = p;
        }
        return minAge;
    }
}
