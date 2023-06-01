#!/bin/env/python3

import fileVector as fv;

def swap(A, i, j):
	tmp = A[i];
	A[i] = A[j];
	A[j] = tmp;

def selectionSort(A, n):
	for i in range(n-1):
		#search min in A[ i, ... ,n ]
		m = i;
		for j in range(i+1, n):
			if A[j] < A[m]:
				m = j;
		#swap A[m] with A[i]
		if not m == i:
			swap(A, i, m);
	return A;

if __name__ == '__main__':
	fv.ordinamento(selectionSort);
