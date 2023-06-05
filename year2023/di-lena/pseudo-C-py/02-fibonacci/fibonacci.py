#!/bin/env/python3

import sys, math;
from timeit import default_timer as timer;
import numpy as np; #fibonacci 5 e 6

def fib1(n): # => O(1)
	print('formula chiusa')
	square5 = math.sqrt(5)
	plus_phi = ( 1 + square5 ) / 2;
	minus_phi = (1 - square5 ) / 2;
	return 1/square5 * ( plus_phi**n - minus_phi**n ); #arrotondamento a int

def fib2(n): # => Omega(2^{n/2}), memoria O(n)
	print('ricorsiva ingenua, n =', n); 
	if n <= 2:
		return 1;
	else:
		return fib2(n-1) + fib2(n-2);

def fib3(n): # => O(n), memoria O(n)
	print('soluzione iterativa');
	F=[] #array of int
	F.append(1); F.append(1);
	for i in range(2,n):
		F.append(F[i-1] + F[i-2]);
	return F[n-1];

def fib4(n): # => O(n), memoria O(1)
	print('efficente in memoria');
	a = 1;
	b = 1;
	for i in range(2,n):		
		c = a + b;
		print(f'a= {a}, b= {b}, c= {c}');
		a = b;
		b = c;
	return b;

def fib5(n): # => O(n), memoria O(1)
	print('matrici');
	A = np.array([[1,1],[1,0]]);
	for i in range(2,n):
		A = np.dot(A, np.array([[1,1],[1,0]]));
		print(f'{A}, i = {i}');
	return A[0][0];

def fibMatPow(n): # => O(log n), memoria O(log n)
	print('exponentiation by squaring, n =', n);
	A = np.array([[1,1],[1,0]]);
	if n > 1:
		M = fibMatPow(n//2); #divisione intera
		A = np.dot(M,M);
		print(f'{A}, n = {n}');
		if n % 2 != 0:
			A = np.dot(A, np.array([[1,1],[1,0]]));
	return A;

def fib6(n): # => fibMatPow
	M = fibMatPow(n-1);
	return M[0][0];

def chooseAlgorithm(algoritmo, n):
	#print('algoritmo =', algoritmo);
	match algoritmo:
		case 1:
			return fib1(n);
		case 2:
			return fib2(n);
		case 3:
			return fib3(n);
		case 4:
			return fib4(n);
		case 5:
			return fib5(n);
		case 6:
			return fib6(n);
		case _:
			print('Error! algoritmo =', algoritmo);
			return -1;

def main(alg, n):
	start = timer();
	result = chooseAlgorithm(alg, n);
	end = timer();
	elapsed_time = end - start; #in seconds
	print(f'\t\t\tfibonacci({n}) = {result}');
	print('\t\t\ttime =', elapsed_time);

if __name__ == '__main__':
	try:
		alg = int(sys.argv[1]);
		n   = int(sys.argv[2]);
		main(alg,n);
		
	except:
		print(f'usage: {sys.argv[0]} alg n');

	while input('continue? ') in ('y','yes') :
		alg = int(input('\talgorithm? '));
		n   = int(input('\tnumber? '));				
		main(alg,n);

