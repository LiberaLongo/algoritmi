#!/usr/bin/env python3

import sys;
import fileVector as fv;

def ricerca_binaria(A, x): # vector A, int x
	print(f'ricerca binaria iterativa di {x}.');
	i = 0;
	j = len(A) -1;
	while i <= j:
		#se mi accorgo che non è ordinato...
		if A[i] > A[j]:
			print('error! vettore non ordinato');
			return -1;
		
		#se no potrei cmq non accorgermene...
		m = (i+j) // 2;
		if A[m] == x:
			return m;
		elif A[m] < x:
			i = m + 1;
		else:
			j = m - 1;
	return -1;

if __name__ == '__main__':
	x = int(sys.argv[2]);
	print('pos=', fv.main(ricerca_binaria, 'file x', x));
