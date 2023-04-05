package animale;

import java.time.LocalDate;

public abstract class Animale implements IAnimale{
    
    protected String nome;
    protected String verso;
    protected int zampe;
    protected int anno_nascita;

    Animale(String nome, int anno_nascita) {
        this.nome = nome;
        this.anno_nascita = anno_nascita;
    }

    public String getNome() {
        return nome;
    }
    public String getVerso() {
        return verso;
    }
    public int getZampe() {
        return zampe;
    }
    public int getAnno_nascita() {
        return anno_nascita;
    }
    public int getAge() {
        return LocalDate.now().getYear() - this.anno_nascita;
    }

	@Override
    public int compareTo(Animale a) {
        return this.getAge() - a.getAge();
    }

    @Override
    public String toString() {
        return "\tnome = \"" + nome + "\",\tetà = " + this.getAge() + ",\tverso = \"" + verso + "\",\tzampe = " + zampe;
    }
}
