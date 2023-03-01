package persona;

public class ImpiegatiDemo {
    public static Persona cercaGiovane(Persona[] array) {
        Persona minAge = array[0];
        for(int i = 1; i < array.length; i++) {
            if(array[i].getNascita().compareTo(minAge.getNascita()) > 0) //younger
                minAge = array[i];
        }
        return minAge;
    }
}
