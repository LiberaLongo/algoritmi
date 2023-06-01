#!/bin/env/python3

import fileVector as fv;

def merge(A, n, p, q, r):
	B = [];
	i = p;
	j = q+1;
	while i <= q and j <= r:
		if A[i] <= A[j]:
			B.append(A[i]);
			i = i+1;
		else:
			B.append(A[j]);
			j = j+1;
#copia la prima parte rimanente alla fine di B
	while i <= q :
		B.append(A[i]);
		i = i+1;
#copia la seconda parte rimanente alla fine di B
	while j <= r :
		B.append(A[j]);
		j = j+1;
#copy the sorted numbers from B to A ...
	for k in range(r-p+1):
		A[p+k] = B[k];
	return A;

def mergesort(A, n, p, r):
	print(f'mergesort(A={A}, n={n}, p={p}, r={r}');
	if p < r:
		q = p + (r-p) // 2;
		A = mergesort(A, n, p, q);
		A = mergesort(A, n, q+1, r);
		#qui le due metà vengono ordinate
		merge(A, n, p, q, r);
	return A;

def mergeSorting(A, n):
	return mergesort(A, n, 0, n-1);

if __name__ == '__main__':
	fv.ordinamento(mergeSorting);
