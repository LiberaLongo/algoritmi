/*
 * Ordinamenti.java 
 *
 * Compilare con
 *
 * javac Ordinamenti.java
 *
 * Eseguire con
 *
 * java Ordinamenti <N> 
 *
 * Genera immagini con la rappresentazione a punti dell'evoluzione
 * di un array che contiene i valori da 1 a N durante l'esecuzione
 * di un algoritmo di ordinamento.
 * Ad esempio, l'algoritmo SelectionSort genera delle immagini
 * dal nome SelectionSortXXXX.bmp, con X numerazione progressiva.
 * A partire da questi file e' possibile creare una gif animata con:
 *
 * magick -delay 10 SelectionSort*.bmp SelectionSort.gif
 */

import java.io.*;
import java.util.Random;
import java.util.Scanner;

public class Ordinamenti {
	
	/*
	 * Generazione delle immagini
	 */
	
	// contatore utilizzato per numerare le immagini
	static int globalcounter;
	
	// creare l'immagine bitmap sapendo che il valore x
	// si trova nell'array in posizione posValore[x]
	static void creaIMG(int size, int posValore[], String outputfile) {
		try {
			BufferedWriter f=new BufferedWriter(new FileWriter(outputfile));
			f.write("P1\n");
			f.write(size+" "+size+"\n");
			for(int i=size-1; i>=0; i--) {
				for(int j=0; j<size; j++) {
					if(j==posValore[i]) f.write("1 ");
					else f.write("0 ");
				}
				f.write("\n");
			}
			f.close();
		}
		catch (IOException ex) {
			System.err.println(ex);
			System.exit(1);
		}
		
	}
	
	// prepara il vettore di posizionamento per creare l'immagine
	static void creaFile(int size, int v[], String outputfile) {
		int posValore[] = new int[size];
		for (int i=0; i<size; i++) posValore[v[i]]=i;
		creaIMG(size, posValore, outputfile);
	}
	
	// prepara il vettore di posizionamento per creare l'immagine
	// nel caso di heapsort, in cui si memorizzano i valori
	// a partire dall'indice 1
	static void creaFileHeap(int size, int v[], String outputfile) {
		int posValore[] = new int[size];
		for (int i=1; i<size+1; i++) posValore[v[i]]=i-1;
		creaIMG(size, posValore, outputfile);
	}
	
	// funzione ausiliaria per trasformare il numero dell'immagine
	// in stringa di lunghezza 4
	static String myToString(int x) {
		if (x<10) return "000"+x;
		else if (x<100) return "00"+x;
		else if (x<1000) return "0"+x;
		else return ""+x;
	}
	
	/*
	 * Selection Sort
	 */
	
	static void selectionSort(int A[]) {
		creaFile(A.length, A, "SelectionSort"+myToString(0)+".bmp");
		for (int k = 0; k < A.length - 1; k++) {
			// cerca il minimo A[m] in A[k..n-1]
			int m = k;
			for (int j = k + 1; j < A.length; j++)
				if (A[j] < A[m]) 
				m = j;
			// scambia A[k] con A[m]
			if (m != k) {
				int temp = A[m];
				A[m] = A[k];
				A[k] = temp;
			}
			creaFile(A.length, A, "SelectionSort"+myToString(k+1)+".bmp");
		}
	} 	
	
	/*
	 * Insertion Sort
	 */
	
	public static void insertionSort(int A[]) {
		creaFile(A.length, A, "InsertionSort"+myToString(0)+".bmp");
		for (int k = 1; k <= A.length - 1; k++) {
			int j;
			int x = A[k];
			// cerca la posizione j in cui inserire A[k]
			for (j = 0; j < k; j++)
				if (A[j] > x) break;
			if (j < k) {
				// Sposta A[j..k-1] in A[j+1..k]
				for (int t = k; t > j; t--) 
					A[t] = A[t - 1];
				// Inserisci A[k] in posizione j
				A[j] = x;
			}
			creaFile(A.length, A, "InsertionSort"+myToString(k)+".bmp");
		}
	}
	
	/*
	 * Bubble Sort
	 */
	
	public static void bubbleSort(int A[]) {
		creaFile(A.length, A, "BubbleSort"+myToString(0)+".bmp");
		for (int i = 1; i < A.length; i++) {
			boolean scambiAvvenuti = false;
			for (int j = 1; j <= A.length - i; j++) {
				// Se A[j-1] > A[j], scambiali
				if (A[j - 1] > A[j]) {
					int temp = A[j - 1];
					A[j - 1] = A[j];
					A[j] = temp;
					scambiAvvenuti = true;
				}
			}
			creaFile(A.length, A, "BubbleSort"+myToString(i)+".bmp");
			if (!scambiAvvenuti) break;
		}
	}
	
	/*
	 * Quicksort
	 */
	
	public static void quickSort(int A[]) {
		globalcounter=0;
		creaFile(A.length, A, "QuickSort"+myToString(globalcounter++)+".bmp");
		quickSortRec(A, 0, A.length - 1);
	}
	
	public static void quickSortRec(int A[], int i, int f) {
		if (i >= f) return;
		int m = partition(A, i, f);
		quickSortRec(A, i, m - 1);
		quickSortRec(A, m+1, f);
	}
	
	private static int partition(int A[], int i, int f) {
		int inf = i, sup = f + 1;
		int temp, x = A[i];
		while (true) {
			do {
				inf++;
			} while (inf <= f && A[inf] <= x) ;
			do {
				sup--;
			} while (A[sup] > x);
			if (inf < sup) {
				temp = A[inf];
				A[inf] = A[sup];
				A[sup] = temp;
			} else
			break;
		}
		temp = A[i];
		A[i] = A[sup];
		A[sup] = temp;  	 	 
		creaFile(A.length, A, "QuickSort"+myToString(globalcounter++)+".bmp");
		return sup;
	}
	
	/*
	 * Mergesort
	 */
	
	public static void mergeSort(int A[]) {
		globalcounter=0;
		creaFile(A.length, A, "MergeSort"+myToString(globalcounter++)+".bmp");
		mergeSortRec(A, 0, A.length - 1);
	}
	
	private static void mergeSortRec(int A[], int i, int f) {
		if (i >= f) return;
		int m = (i + f) / 2;
		mergeSortRec(A, i, m);
		mergeSortRec(A, m + 1, f);
		merge(A, i, m, f);
	}
	
	private static void merge(int A[], int i1, int f1, int f2) {
		int[] X = new int[f2 - i1 + 1];
		int i = 0, i2 = f1 + 1, k = i1;
		while (i1 <= f1 && i2 <= f2) {
			if (A[i1] < A[i2])  
				X[i++] = A[i1++];
			else 
				X[i++] = A[i2++];
		}
		if (i1 <= f1)
			for (int j = i1; j <= f1; j++, i++) X[i] = A[j];
		else 
			for (int j = i2; j <= f2; j++, i++) X[i] = A[j];
		for (int t = 0; k <= f2; k++, t++) A[k] = X[t];	  	 	
		creaFile(A.length, A, "MergeSort"+myToString(globalcounter++)+".bmp");
	}
	
	/*
	 * Heapsort
	 */
	
	public static void heapSort(int S[]) {
		globalcounter=0;
		creaFileHeap(S.length-1, S, "HeapSort"+myToString(globalcounter++)+".bmp");
		heapify(S, S.length - 1, 1);
		creaFileHeap(S.length-1, S, "HeapSort"+myToString(globalcounter++)+".bmp");
		for (int c = (S.length - 1); c > 0; c--) {
			int k = findMax(S);
			deleteMax(S, c);
			S[c] = k;	 
			creaFileHeap(S.length-1, S, "HeapSort"+myToString(globalcounter++)+".bmp");
		}
	}
	
	private static void heapify(int S[], int n, int i) {
		if (i > n) return;
		heapify(S, n, 2 * i); // crea heap radicato in S[2*i]
		heapify(S, n, 2 * i + 1); // crea heap radicato in S[2*i+1]
		fixHeap(S, n, i);
	}
	
	private static void fixHeap(int S[], int c, int i) {
		int max = 2 * i; // figlio sinistro
		if (2 * i > c) return;
		if (2 * i + 1 <= c && S[2 * i] < S[2 * i + 1])
			max = 2 * i + 1; // figlio destro
		if (S[i] < S[max])  {
			int temp = S[max];
			S[max] = S[i];
			S[i] = temp;
			fixHeap(S, c, max);
		}
	}
	
	private static int findMax(int S[]) {
		return S[1];
	}
	
	private static void deleteMax(int S[], int c) {
		S[1]=S[c];
		fixHeap(S, c, 1);
	}
	
	/*
	 * Main per generare le immagini di simulazione
	 * di esecuzione algoritmi di ordinamento
	 */
	public static void main( String[] args ) {
		int size = Integer.valueOf(args[0]);
		int[] v = new int[size];
		boolean[] used = new boolean[size];
		int[] copia = new int[size];
		int randValue;
		Random random = new Random();
		
		// inserimento randomico dei valori nel vettore da ordinare
		for (int i=0; i<size; i++) 
			used[i]=false;
		for (int i=0; i<size; i++) {
			randValue = random.nextInt(size);
			while(used[randValue] == true) { 
				randValue = random.nextInt(size);
			}
			v[i]=randValue;
			used[randValue]=true;
		}
				
		// esecuzione degli algoritmi di ordinamento
		for (int i=0; i<size; i++) copia[i]=v[i];
		selectionSort(copia);
		
		for (int i=0; i<size; i++) copia[i]=v[i];
		//insertionSort(copia);
		
		for (int i=0; i<size; i++) copia[i]=v[i];
		//bubbleSort(copia);
		
		for (int i=0; i<size; i++) copia[i]=v[i];
		//quickSort(copia);
		
		for (int i=0; i<size; i++) copia[i]=v[i];
		//mergeSort(copia);
		
		int[] copiaPerHeapSort = new int[size+1];
		for (int i=0; i<size; i++) copiaPerHeapSort[i+1]=v[i];
		//heapSort(copiaPerHeapSort);
		
	}
	
}
 
 
