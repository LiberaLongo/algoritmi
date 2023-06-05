#!/bin/env/python3

import fileVector as fv;

def selectionSort(A, n):
	for i in range(n-1):
		#search min in A[ i, ... ,n ]
		m = i;
		for j in range(i+1, n):
			if A[j] < A[m]:
				m = j;
		#swap A[m] with A[i]
		if not m == i:
			fv.swap(A, i, m);
	return A;

if __name__ == '__main__':
	print('SelectionSort:');
	print('ottimo, medio, pessimo: Θ(n^2)');
	print('in place: si, stabile: si');
	print('\nn = n° elementi da ordinare');
	fv.ordinamento(selectionSort);
