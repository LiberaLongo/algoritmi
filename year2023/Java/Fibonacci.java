/**
* Performs comparisons on the time needed to compute a
* given Fibonacci number using different algorithms
*
* To compile: javac Fibonacci.java
*
* To execute: java Fibonacci 
* Then introduce in separate lines 
* <n> 
* <activation bit vector> 
* <display option>
* 
* The activation bit vector is a string of length 6 with
* '1' for methods to execute and '0' otherwise
*
* The display option is a character; 
* if it is 'y' the computed value is displayed
*/

import java.util.*;
import java.math.BigInteger; 
import java.lang.Math; 

public class Fibonacci {
	
	/**
	* Auxiliary function for matrix multiplication
	*/
	static void MatProd(BigInteger[][] M1, 
		BigInteger[][] M2, 
		BigInteger[][] M3) {
		M1[0][0] = (M2[0][0]).multiply(M3[0][0]).add(
			(M2[0][1]).multiply(M3[1][0]));
		M1[0][1] = (M2[0][0]).multiply(M3[0][1]).add(
			(M2[0][1]).multiply(M3[1][1]));
		M1[1][0] = (M2[1][0]).multiply(M3[0][0]).add(
			(M2[1][1]).multiply(M3[1][0]));
		M1[1][1] = (M2[1][0]).multiply(M3[0][1]).add(
			(M2[1][1]).multiply(M3[1][1]));
	}
		
	/**
	* Auxiliary function for matrix exponentiation
	*/
	static void MatPow(BigInteger[][] M, int k) {
		if (k>1) {   
			BigInteger[][] temp = new BigInteger[2][2];
			temp[0][0] = M[0][0];
			temp[0][1] = M[0][1];
			temp[1][0] = M[1][0];
			temp[1][1] = M[1][1];
			if (k%2==0) {
				MatPow(temp,k/2);
				MatProd(M,temp,temp);
			} else {       
				BigInteger[][] temp2 = new BigInteger[2][2];
				MatPow(temp,(k-1)/2);
				MatProd(temp2,temp,M);
				MatProd(M,temp,temp2); 
			}
		}
	}
	
	
	/**
	* Compute Fibonacci with the direct method
	*/
	static double fib_1( int n ) {
		return 1.0/Math.sqrt(5.0)*
		( Math.pow( (1.0+Math.sqrt(5.0))/2.0, n) - 
			Math.pow( (1.0-Math.sqrt(5.0))/2.0, n) );
	}
		
	/**
	* Compute Fibonacci using the inductive definition
	*/
	static BigInteger fib_2( int n ) {
		if (n<=2) return new BigInteger("1");
		else return (fib_2(n-1)).add(fib_2(n-2));
	}
	
	/**
	* Iterative computation of Fibonacci using an array
	*/
	static BigInteger fib_3( int n ) {
		if (n<=2) return new BigInteger("1");
		else {
			BigInteger Fib[]=new BigInteger[n+1];
			Fib[1]=new BigInteger("1");
			Fib[2]=new BigInteger("1");
			for (int i=3; i<=n; i++)
				Fib[i]=Fib[i-1].add(Fib[i-2]);
			return Fib[n];
		}
	}
		
	/**
	* Iterative computation of Fibonacci using two variables
	*/
	static BigInteger fib_4( int n ) {
		BigInteger prev = new BigInteger("1"), last=new BigInteger("1"), help;
		for (int i=3; i<=n; i++) {
			help = last;
			last = prev.add(last);
			prev = help;
		}
		return last;
	}
		
	/**
	* Computation of Fibonacci using matrix multiplication
	*/
	static BigInteger fib_5( int n ) {
		BigInteger[][] A = new BigInteger[2][2];
		A[0][0] = new BigInteger("1");
		A[0][1] = new BigInteger("1");
		A[1][0] = new BigInteger("1");
		A[1][1] = new BigInteger("0");
		BigInteger[][] X = new BigInteger[2][2];
		X[0][0] = new BigInteger("1");
		X[0][1] = new BigInteger("1");
		X[1][0] = new BigInteger("1");
		X[1][1] = new BigInteger("0");
		BigInteger[][] temp = new BigInteger[2][2];
		for(int i=2; i<=n-1; i++) {
			temp[0][0] = A[0][0];
			temp[0][1] = A[0][1];
			temp[1][0] = A[1][0];
			temp[1][1] = A[1][1];
			MatProd(A,temp,X);
		}
		return A[0][0];
	}
		
	/**
	* Computation of Fibonacci using matrix exponentiation 
	*/
	static BigInteger fib_6( int n ) {
		if (n<2) return new BigInteger("1");
		else {
			BigInteger[][] A = new BigInteger[2][2];
			A[0][0] = new BigInteger("1");
			A[0][1] = new BigInteger("1");
			A[1][0] = new BigInteger("1");
			A[1][1] = new BigInteger("0");
			MatPow(A,n-1);
			return A[0][0];
		}
	}
		
	public static void main( String args[] ) {
		long start_t, end_t, elapsed, min;
		double sec;
		int n=0;
		String av="";
		String d="n";   
		try {
			System.out.println("Insert n:");
			Scanner input = new Scanner(System.in);
			String s1 = input.nextLine();
			n = Integer.parseInt(s1);
			System.out.println(
				"Insert activation vector (six bits, 1 to execute):");
			av = input.nextLine();
			System.out.println("Insert display option y/n:");
			d = input.nextLine();
		} catch (Exception e) {
			System.out.println("Error reading from user");
			System.exit(0);
		}  
		double res1;
		BigInteger res;
		
		if (av.charAt(0)=='1') {
			start_t = System.currentTimeMillis();
			res1 = fib_1(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** DIRECT METHOD: "+res1);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
		
		if (av.charAt(1)=='1') {
			start_t = System.currentTimeMillis();
			res = fib_2(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** RECURSIVE METHOD: "+res);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
		
		if (av.charAt(2)=='1') {
			start_t = System.currentTimeMillis();
			res = fib_3(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** ITERATIVE WITH ARRAY: "+res);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
		
		if (av.charAt(3)=='1') {
			start_t = System.currentTimeMillis();
			res = fib_4(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** ITERATIVE WITH TWO VARIABLES: "+res);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
		
		if (av.charAt(4)=='1') {
			start_t = System.currentTimeMillis();
			res = fib_5(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** MATRIX MULTIPLICATION: "+res);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
		
		if (av.charAt(5)=='1') {
			start_t = System.currentTimeMillis();
			res = fib_6(n);
			end_t = System.currentTimeMillis();
			elapsed = (end_t - start_t);
			min = elapsed / (60*1000);
			sec = (elapsed - min*60*1000)/1000.0;
			if (d.charAt(0)=='y')
				System.out.println("** MATRIX EXPONENTIATION: "+res);
			System.out.println("Time: "+min+" min "+sec+" sec");
		}
	}
}
