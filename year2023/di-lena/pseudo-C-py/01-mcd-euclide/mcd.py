#!/bin/env/python3

#algoritmo di euclide per massimo comune divisore
#tra x e y (x >= y)

import sys;

def mcd (x, y):
	if (y == 0):
		return x;
	else:
		r = x % y;
		return mcd(y,r);

if __name__ == '__main__':
	try:
		a = sys.argv[1];
		b = sys.argv[2];
		print(f"mcd({a},{b}) = {mcd(a,b)}");
	except:
		print(f"usage: {sys.argv[0]} x y");
		print("should value (x >= y)");

