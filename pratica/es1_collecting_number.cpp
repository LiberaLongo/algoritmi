
Collecting Numbers
Dato un array che contiene ogni numero compreso tra 1 e n esattamente una volta. Il
tuo compito è raccogliere i numeri da 1 a n in ordine crescente.
Ad ogni round, si passa attraverso l’array da sinistra a destra e si raccolgono quanti
più numeri possibile. Quale sarà il numero totale di round?

int solve_n2(vector<int> n) {
	int next = 1;
	int sol = 1;
	int current = 0;
	while (true) {
		if (n[current] == next) {
			next++;
		}
		if (next == n.size() + 1)
		break;
		current++;
		if (current >= n.size()) {
			sol++;
			current = 0;
		}
	}
}


Soluzione n log n
int solve_nlogn(vector<int> n) {
	vector<array<int, 2>> a;
	for (int i = 0; i < n.size(); i++) {
		a.push_back({n[i], i});
	}
	sort(a.begin(), a.end());
	int sol = 1;
	for (int i = 1; i < n.size(); i++) {
		if (a[i][1] < a[i - 1][1]) {
		sol++;
		}
	}
	return sol;
}


idea: controllare se il precedente è già stato incontrato.


soluzione n:
int solve_n(vector<int> n) {
	vector<bool> k(n.size() + 1, false);
	k[0] = true;
	int sol = 1;
	for (int i = 0; i < n.size(); i++) {
		k[n[i]] = true;
		if (!k[n[i] - 1]) {
			sol++;
		}
	}
	return sol;
}



 
 
