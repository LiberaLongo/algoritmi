#!/bin/env/python3

import sys

def readVector(filename):
	vector = [];
	with open(filename, 'r') as file:
		for line in file:
			for word in line.split():
				vector.append(int(word));
	return vector;

def writeVector(vector, filename):
	with open(filename, 'w') as file:
		for number in vector:
			file.write(' ' + str(number));

def swap(A, i, j):
	tmp = A[i];
	A[i] = A[j];
	A[j] = tmp;

def ordinamento(funzione):
	read = sys.argv[1];
	write = sys.argv[2];
	vector = readVector(read);
	print(' input =', vector);
	output = funzione(vector, len(vector));
	print('output =', output);
	writeVector(output, write);

def main(function, usage, x):
	try:
		name = sys.argv[1];
		vector = readVector(name);
		print('vector =', vector);
		return function(vector, x);
	except OSError:
		print(f'usage {sys.argv[0]} {usage}');
		print(OSError);

