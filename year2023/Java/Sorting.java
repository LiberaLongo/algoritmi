/*
 * Execute the command
 * 
 * java Sorting <file with integers> <sorting algoritm name>
 *
 * If quickSort crashes due to a high number of recursion calls
 * try to increase the stack size of the JVM, for example
 *
 * java -Xss10M Sorting <file with integers> <sorting algoritm name> 
 *
 */

import java.io.*;
import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.reflect.Method;



public class Sorting {
	static private String[] L  = {"selectionSort", "insertionSort", "mergeSort",
                                "quickSort", "rquickSort", "countingSort","javaSort"};
	/*
	 * SelectionSort
	 */
	public static void selectionSort(int A[]) {
		for (int i = 0; i < A.length - 1; i++) {
			int m = i;
			for (int j = i + 1; j < A.length; j++)
				if (A[j] < A[m]) 
					m = j;
			if (m != i) 
				swap(A,i,m);
		}
	} 	

	private static void swap(int A[],int i, int j) {
		int tmp = A[i];
		A[i] = A[j];
		A[j] = tmp;
	}
	
	/*
	 * InsertionSort
	 */
	public static void insertionSort(int A[]) {
		for (int i = 1; i <= A.length - 1; i++) {
			int j = i;
			while(j > 0 && A[j] < A[j-1]) {
				swap(A,j,j-1);
				j--;
			}
		}
	}

	/*
	 * MergeSort
	 */
	public static void mergeSort(int A[]) {
		mergeSortRec(A,0,A.length - 1);
	}
  
	private static void mergeSortRec(int A[], int p, int r) {
		if (p < r) {
    	int q = p + (r-p) / 2;
    	mergeSortRec(A,p,q);
    	mergeSortRec(A,q+1,r);
    	merge(A,p,q,r);
		}
	}

	private static void merge(int A[], int p, int q, int r) {
		int[] B = new int[r - p + 1];
		int   i = p;
		int   j = q + 1;
		int   k = 0;

    while (i <= q && j <= r)
      if (A[i] <= A[j])  
        B[k++] = A[i++];
      else 
        B[k++] = A[j++];

    while (i <= q)
			B[k++] = A[i++];

		while (j <= r)
			B[k++] = A[j++];

    for (k = 0; k < r-p+1; k++)
			A[p+k] = B[k];       
  }

	/*
	 * QuickSort with deterministic choice of the pivot
	 */
	public static void quickSort(int A[]) {
		quickSortRec(A,0,A.length-1);
	}
  
	public static void quickSortRec(int A[], int p, int r) {
		if (p < r) {
			int q = partition(A,p,r);
			quickSortRec(A,p,q-1);
			quickSortRec(A,q+1,r);
		}
	}

	private static int partition(int A[], int p, int r) {
		int x = A[r];
		int i = p-1;
		for(int j = p; j < r; j++)
			if (A[j] <= x)
				swap(A,++i,j); 
		swap(A,i+1,r);
		return i+1;
  }

  /*
   * QuickSort with random choice of the pivot
   */
	public static void rquickSort(int A[]) {
		rquickSortRec(A,0,A.length-1);
	}

	public static void rquickSortRec(int A[], int p, int r) {
		if (p < r) {
			int q = rpartition(A,p,r);
			rquickSortRec(A,p,q-1);
			rquickSortRec(A,q+1,r);
		}
  }

	private static int rpartition(int A[], int p, int r) {
		Random random = new Random();
		// nextInt(n) returns a random int in [0,n)
		int i = random.nextInt(r-p+1) + p;
		swap(A,i,r);
		return partition(A,p,r);
	}

  /*
   * CountingSort
   */
  public static void countingSort(int A[]) {
		int a = Arrays.stream(A).min().getAsInt();
		int b = Arrays.stream(A).max().getAsInt();
		int k = b-a+1;
		int[] B = new int[b - a + 1];

		for(int i = 0; i < A.length; i++)
			B[A[i]-a]++;

		for(int i = 0, j = 0; i < k; i++)
			while(B[i]-- > 0) 
				A[j++] = i+a;
	}

	public static void javaSort(int A[]) {
		Arrays.sort(A);
	}
	
	private static void printUsage() {
		System.err.println("Usage: Sorting <file> <sorting algorithm>\n");
		System.err.println("Sorting algorithms:");
		for(int i = 0; i < L.length; i++)
			System.err.println("- " + L[i]);
	}


	private static int[] read(String filename) throws IOException {
		return Files.lines(Paths.get(filename)).mapToInt(Integer::parseInt).toArray();
	}
	private static void save(int[] A, String filename) throws IOException {
		FileWriter writer = new FileWriter(filename);
		for (int i = 0; i < A.length; i++)
			writer.write(A[i] + "\n");
		writer.close();
	}
	

	public static void main(String[] args) {
		int[] A;
		Method sort;

		if(args.length != 2) {
			printUsage();
			System.exit(0);
		}

		try {
			// Read the integers into and array
			A = read(args[0]);

			// Select sorting method
			sort = Sorting.class.getMethod(args[1],int[].class);

			// Sorting
			long start = System.currentTimeMillis();
			sort.invoke(null,A);
			long end = System.currentTimeMillis();
			System.out.println(sort.getName() + ": " + (end - start)/1000.0 + " secs");

			save(A,sort.getName() + "." + args[0]);

		} catch(Exception e) {
			System.err.println(e);
			System.exit(1);
		}

	}
}
