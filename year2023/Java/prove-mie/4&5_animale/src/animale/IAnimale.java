package animale;

public interface IAnimale {
    String getNome();
    String getVerso();
    int getZampe();
    int getAnno_nascita();
    int getAge();
    int compareTo(Animale a);
}
