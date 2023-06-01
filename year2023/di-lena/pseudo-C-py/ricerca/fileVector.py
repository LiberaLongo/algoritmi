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
			file.write(str(number));

def main(function, usage, x):
	try:
		name = sys.argv[1];
		vector = readVector(name);
		return function(vector, x);
	except OSError:
		print(f'usage {sys.argv[0]} {usage}');
		print(OSError);

