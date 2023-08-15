//visit stuff
import java.util.Iterator;
import java.util.List;

import asdlab.libreria.Alberi.AlberoBinPF; // Albero binario
import asdlab.libreria.Alberi.NodoBinPF;   // Nodo di albero binario
import asdlab.libreria.Alberi.AlberoBin.TipoVisita;

//my stuff
import asdlab.libreria.AlberiRicerca.AlberoAVL;

public class myDemo {

	public static void main(String[] args) {

		AlberoAVL AVL = new AlberoAVL();
		
		AVL.insert("alessandra", "a");
		
		//toString non mi serve pk stampa solo il riferimento java e non come è fatto l'albero
		System.out.println(AVL);

		//visit
		AlberoBinPF A = (AlberoBinPF) AVL;

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
	}
}
