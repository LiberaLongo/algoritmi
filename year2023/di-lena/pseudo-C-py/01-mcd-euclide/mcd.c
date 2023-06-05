//algoritmo di euclide per massimo comune divisore tra x e y (x >= y)
#include <stdio.h>
#include <stdlib.h>
#include <libgen.h>

int mcd (int x, int y) {
	if (y == 0)
		return x;
	else {
		int r = x % y;
		return mcd(y,r);
	}
}
int main(int argc, char* argv[]) {
	if( argc != 3 ) {
		printf("usage: %s x y\n", argv[0]);
		return -1;
	}
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);
	if( ! (a >= b) ) {
		printf("should value (x >= y)\n");
		return -1;
	}
	printf("mcd(%d,%d) = %d\n", a, b, mcd(a, b));
	return 0;
}
