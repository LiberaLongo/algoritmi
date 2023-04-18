/**
 * Compute the Levenshtein distance between two strings
 * passed from the command line.
 *
 * To compile: javac Levenshtein.java
 *
 * To execute: java Levenshtein LIBRO ALBERO
 *
 * (C) 2016 Moreno Marzolla (http://www.moreno.marzolla.name/)
 * Distributed under the CC-zero 1.0 license
 * https://creativecommons.org/publicdomain/zero/1.0/
 * 
 */
 class Levenshtein {
 	 
 	 /**
     * Restituisce il massimo tra |i| e |j|
     */
     static int max( int i, int j )
     {
     	 return (i>j ? i : j);
     }
     
     /**
     * Restituisce il minimo tra |i|, |j| e |k|,
     */
     static int min3( int i, int j, int k )
     {
     	 int result = i;
     	 if (j < result) result = j;
     	 if (k < result) result = k;
     	 return result;
     }
     
     /**
     * Restituisce la distanza di Levenshtein tra due stringhe |S| e
     * |T|.  La distanza e' un intero compreso tra 0 e la massima
     * lunghezza delle due stringhe. Si presti attenzione al fatto che
     * le posizioni dei caratteri delle stringhe in Java iniziano da 0
     * e non da 1 come nello pseudocodice usato nei lucidi. 
     */     
     static int levDistance( String S, String T )
     {
     	 int i, j;
     	 final int n = S.length(), m = T.length();
     	 int L[][] = new int[n+1][m+1];
     	 for ( i=0; i<n+1; i++ ) {
     	 	 for ( j=0; j<m+1; j++ ) {
     	 	 	 if ( i==0 || j==0 ) {
     	 	 	 	 L[i][j] = max(i, j);
     	 	 	 } else {
     	 	 	 	 L[i][j] = 
     	 	 	 	 min3(L[i-1][j] + 1, L[i][j-1] + 1,
     	 	 	 	 	  L[i-1][j-1] + (S.charAt(i-1)!=T.charAt(j-1) ? 1 : 0));
     	 	 	 }
     	 	 }
     	 }
     	 
     	 /* Stampa la matrice L */
     	 for (i=0; i<n+1; i++) {
     	 	 for (j=0; j<m+1; j++) {
     	 	 	 System.out.print(L[i][j]);
     	 	 	 System.out.print("  ");
     	 	 }
     	 	 System.out.println();
     	 }
     	 return L[n][m];
     }
     
     public static void main( String[] args )
     {
     	 System.out.println(levDistance(args[0], args[1]));
     }
 }
