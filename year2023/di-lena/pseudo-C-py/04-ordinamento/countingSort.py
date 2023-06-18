#!/usr/bin/env python3

import fileVector as fv;

def countingSort(A, n):
	a = min(A);
	b = max(A);
	print(f'a=min(A)={a}, b=max(A)={b}');
	k = b - a +1;
	B = [];
	for i in range(k):
		B.append(0);
	#count
	for i in range(n):
		B[ A[i]-a ] = B[ A[i]-a ] +1;
	#rearrange
	j = 0;
	for i in range(k):
		while B[i] > 0:
			A[j] = i + a;
			B[i] = B[i] - 1;
			j = j +1;
	return A;

if __name__ == '__main__':
	print('CountingSort:');
	print('ottimo, medio, pessimo: Θ(n+k)');
	print('in place: no, stabile: si');
	print('\nn = n° elementi da ordinare');
	print('k = ampiezza del range di valori chiave');
	fv.ordinamento(countingSort);
