#!/bin/env/python3

import fileVector as fv;

def partition(A, p, r):
	print(f'\npartition {A}, p={p}, r={r}');
	x = A[r]; #deterministic choice of the pivot
	i = p -1;
	for j in range(p, r):
		if A[j] <= x:
			fv.swap(A, i+1, j);
			print(f'\tswap A[i+1] = A[{i+1}] = {A[i+1]} con A[j] = A[{j}] = {A[j]}');
			print(A);
			i = i+1;
	#move the pivot value in A[i+1]
	fv.swap(A, i+1, r);
	return i+1; #return the pivot index in A	

def quickSort(A, p, r):
	if p < r:
		q = partition(A, p, r);
		print('pivot = q =', q);
		quickSort(A, p, q-1);
		quickSort(A, q+1, r);
	return A
	
def launchQuickSort(A, n):
	return quickSort(A, 0, n-1);

if __name__ == '__main__':
	print('QuickSort:');
	print('ottimo: Θ(n log n), \n\tmedio: O(n log n),\n\t\tpessimo: Θ(n^2)');
	print('in place: si, stabile: no');
	print('\nn = n° elementi da ordinare');
	fv.ordinamento(launchQuickSort);
