#!/usr/bin/env python3

import sys;
import fileVector as fv;

def incrementoVector(A):
	print(f'incremento in {A}');
	i = len(A)-1;
	while i >= 0 and A[i] == 1:
		A[i] = 0;
		i = i - 1;
	if i >= 1: #if i = 0 counter overflow
		A[i] = 1;
	return A;

def incremento(read, write):
	new = incrementoVector(read);
	print('new incrvec =', new);
	fv.writeVector(new, write);
	return new;

if __name__ == '__main__':
	write = sys.argv[2];
	fv.main(incremento, 'read write', write);

