/*
* ConnectionAnalysis.java 
*
* Compilare con
*
* javac -cp /Users/gianluigizavattaro/Documents/Didattica/Algoritmi/Java/asdlab/lib/asdlab.jar ConnectionAnalysis.java
*
* Eseguire con
*
* java -cp .:/Users/gianluigizavattaro/Documents/Didattica/Algoritmi/Java/asdlab/lib/asdlab.jar ConnectionAnalysis <FILENAME>
*
* Esempio di punti non connessi in roadNet-TX.txt
* 0 1309432
*/

import java.io.*;
import java.util.*;
import asdlab.libreria.UnionFind.*;
import asdlab.libreria.StruttureElem.Rif;

public class ConnectionAnalysis {	
	
	/*
	* Fondi i disjoint set considerando i collegamenti bidirezionali
	*/
	public static void fondi(Rif[] sets, ArrayList<Integer> src, 
							 ArrayList<Integer> dst, UnionFind uf) {
		for (int i = 0; i < src.size(); i++) {
			uf.union(uf.find(sets[src.get(i)]),uf.find(sets[dst.get(i)]));	 
		}
	}	
		
		
	/*
	* Main per leggere una rete e poi controllari collegamenti
	*/
	public static void main( String[] args ) {
			
		try {
			
			long start_t, end_t, elapsed, min;
			double sec;
			
			File file = new File(args[0]);
			
			BufferedReader br = new BufferedReader(new FileReader(file));
			ArrayList<Integer> src = new ArrayList<Integer>();
			ArrayList<Integer> dst = new ArrayList<Integer>();
			String st;
			int max=0,s,d,v;
			while ((st = br.readLine()) != null) {
				v = st.indexOf("\t");
				s = Integer.valueOf(st.substring(0,v));
				d = Integer.valueOf(st.substring(v+1));
				if (s>max) max=s;
				if (d>max) max=d;
				src.add(s);
				dst.add(d);
			}
			
			Rif[] sets = new Rif[max+1];
			UnionFind uf = new QuickFind();
			for (int i=0; i<sets.length; i++) sets[i]=uf.makeSet();
			
			start_t = System.currentTimeMillis();
			fondi(sets,src,dst,uf);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			System.out.println("Elaborazione collegamenti: "+min+" min "+sec+" sec");

			Scanner scanner = new Scanner(System.in);
			int u1,u2;
			boolean connected;
			do {
				System.out.println("Inserisci due punti (-1 per terminare):");
				u1 = scanner.nextInt();
				if (u1 == -1) break;
				u2 = scanner.nextInt();
				start_t = System.currentTimeMillis();
				connected = (uf.find(sets[u1]) == uf.find(sets[u2]));
				end_t = System.currentTimeMillis();
				elapsed = (end_t - start_t);
				min = elapsed / (60*1000);
				sec = (elapsed - min*60*1000)/1000.0;
				System.out.println("Controllo connessione: "+min+" min "+sec+" sec");
				if (connected)
					System.out.println("collegati");
				else
					System.out.println("scollegati");
			} while (u1 != -1);
				
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
}
 
 
