#!/bin/env/python3

import sys;
import fileVector as fv;

def binsearch(A, x, i, j):
	if i > j:
		return -1;
	else:
		m = (i+j) // 2;
		if A[m] == x:
			return m;
		elif A[m] > x:
			return binsearch(A,x, i , m-1 );
		else:
			return binsearch(A,x, m+1 , j );

def ricerca_binaria(A, x): # vector A, int x
	print(f'ricerca binaria ricorsiva di {x}.');
	return binsearch(A,x,0,len(A));

if __name__ == '__main__':
	x = int(sys.argv[2]);
	print('pos =', fv.main(ricerca_binaria, 'file x', x));
