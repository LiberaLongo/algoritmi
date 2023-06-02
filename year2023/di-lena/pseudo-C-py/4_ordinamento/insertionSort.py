#!/bin/env/python3

import fileVector as fv;

def insertionSort(A, n):
	for i in range(1, n):
		j = i;
		while j > 1 and A[j] < A[j-1]:
			fv.swap(A, j, j-1);
			j = j-1;
	return A;

if __name__ == '__main__':
	print('InsertionSort:');
	print('ottimo, medio, pessimo: Θ(n^2)');
	print('in place: si, stabile: si');
	print('\nn = n° elementi da ordinare');
	fv.ordinamento(insertionSort);
