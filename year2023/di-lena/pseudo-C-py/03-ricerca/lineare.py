#!/usr/bin/env python3

import sys;
import fileVector as fv;

def ricerca_lineare(A, x): # vector A, int x
	print(f'ricerca lineare di {x} in {A}');
	for i in range(len(A)):
		#print(f'A[{i}] = {A[i]}');
		if A[i] == x:
			return i;
	return -1;

if __name__ == '__main__':
	x = int(sys.argv[2]);
	print('pos=', fv.main(ricerca_lineare, 'file x', x));
