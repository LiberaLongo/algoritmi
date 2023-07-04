import java.util.Iterator;
import java.util.List;

import asdlab.libreria.Alberi.AlberoBinPF; // Albero binario: rappresentazione di tipo puntatori a figli
import asdlab.libreria.Alberi.AlberoPFFS;  // Albero generico: rappresentazione di tipo primo figlio-fratello successivo.
import asdlab.libreria.Alberi.NodoBinPF;   // Nodo di albero binario
import asdlab.libreria.Alberi.NodoPFFS;    // Nodo di albero generico
import asdlab.libreria.Alberi.AlberoBin.TipoVisita;

public class DemoAlberi {

	public static void main(String[] args) {

		/*
		 * Esempio albero binario
		 */
		AlberoBinPF A = new AlberoBinPF();
		
		A.aggiungiRadice("a");
		
		// Crea l'albero binario B con radice (b), figlio sinistro d 
    // e figlio destro e
		AlberoBinPF B = new AlberoBinPF("b");
		B.aggiungiFiglioSin(B.radice(), "d");
		B.aggiungiFiglioDes(B.radice(), "e");

		// Crea l'albero binario C con radice (c), figlio sinistro f
		// e figlio destro g 
		AlberoBinPF C = new AlberoBinPF("c");
    C.aggiungiFiglioSin(C.radice(), "f");
    C.aggiungiFiglioDes(C.radice(), "g");

		// Innesta B come sottoalbero sinistro di A
		// e C come sottoalbero destro
		A.innestaSin(A.radice(), B);
		A.innestaDes(A.radice(), C);
		
		// Effettua una visita DFS in post-ordine di A
		// Necessario dichiarare nodiVisitati di tipo List<?>
		// per evitare warning in fase di compilazione
		List<?> nodiVisitati = A.visitaDFS(TipoVisita.POSTORDER);
		
		// Stampa i nodi visitati
		System.out.println("Stampa DFS post-order dell'albero binario");
		for (Object nodo : nodiVisitati ) {
			System.out.print(" " + ((NodoBinPF)nodo).info);
		}
		System.out.println();
		
		
		/*
		 * Esempio albero n-ario
		 */
		 
		
		// Crea un albero con radice 2
		AlberoPFFS subA = new AlberoPFFS(new NodoPFFS(2));
		// Aggiunge alla radice il figlio 1
		subA.aggiungiFiglio(subA.radice(), 1);

		// Crea un albero con radice 2
		AlberoPFFS subB = new AlberoPFFS(new NodoPFFS(2));
		// Aggiunge alla radice i figli subA, 5 e -1
		subB.innesta(subB.radice(), subA);
		subB.aggiungiFiglio(subB.radice(), 5);
		subB.aggiungiFiglio(subB.radice(), -1);

		// Crea un albero con radice 1
		AlberoPFFS subC = new AlberoPFFS(new NodoPFFS(1));
		// Aggiunge alla radice i figli 0 e -4
		subC.aggiungiFiglio(subC.radice(), 0);
		subC.aggiungiFiglio(subC.radice(), -4);

		// Crea un albero con radice 3
		AlberoPFFS subD = new AlberoPFFS(new NodoPFFS(3));
		// Aggiunge alla radice i figli 2,1 e subC
		subD.aggiungiFiglio(subD.radice(), 2);
		subD.aggiungiFiglio(subD.radice(), 1);
		subD.innesta(subD.radice(), subC);

		AlberoPFFS I = new AlberoPFFS();

		// Crea nodo radice 1 in I
		NodoPFFS radice = (NodoPFFS) I.aggiungiRadice(1);
		// Aggunge sottoalberi subD e subB
		I.innesta(radice, subD);
		I.innesta(radice, subB);

		// Effettua visita BFS su I 
		List<?> visitaInteri = I.visitaBFS();

		// Stampa i nodi visitati
		System.out.println("\nStampa BFS dell'albero n-ario");
		for (Object object : visitaInteri) {
			System.out.print(" " + ((NodoPFFS) object).info);
		}
		System.out.println();
	}

}
