#!/bin/env/python3

import sys;
import fileVector as fv;

def minimo(A, x): # vector A, x is none
	m = 0;
	for i in range(1,len(A)):
		if A[i] < A[m]:
			m = i;
	return m;

def valore_minimo(A, x):
	pos = minimo(A, x);
	print('pos =', pos);
	return A[pos];

if __name__ == '__main__':
	print('minimo =', fv.main(valore_minimo, 'file x', None));
