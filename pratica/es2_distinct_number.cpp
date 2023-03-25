idea: sorto e conto

int distinct_number(int n, int A[]) {
	int counter = 0;
	int B[n] = sort(A);
	for (int i = 0; i < n-1 ; i++) {
		if(A[i] < A[i+1]) {
			counter ++;
		} 
	}
	return counter;
}
O(n log n)


