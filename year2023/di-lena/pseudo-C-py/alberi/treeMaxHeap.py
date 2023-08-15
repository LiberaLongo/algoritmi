import tree;

class treeMaxHeap(tree.tree):
	'''N.B.
- in teoria usa un albero Binario...
ma io non ho capito a cosa gli serve il d-heap dopo...
- La visione ad array non viene usata nella mia implementazione dello pseudocodice in python
(tra l'altro avrei difficoltà a usare un array pk in python ci sono solo le 'list' e i 'dict')
- A[0] non viene usato per poter fare calcoli matematici
'''
	def build(self, array):
		'''
costruisce un treeMaxHeap a partire da un array che rappresenta un max heap nello pseudocodice (ma non nell'implementazione.
'''
		pass;

	def findMax(self):
		'''
Individua il valore massimo contenuto in uno heap
- il massimo è sempre la radice (ossia A[1])
- L'operazione ha costo Theta(1) ==> costante'
'''
		pass;

	def fixHeap(self):
		'''
Ripristinare la propietà di max-heap
- Supponiamo di rimpiazzare la radice A[1] di un max-heap con un valore qualsiasi
- Vogliamo fare in modo che A[] diventi nuovamente uno heap
'''
		pass;

	def heapify(self, disordered_array):
		'''
Costruire uno heap a partire da un array privo di alcun ordine
'''
		pass;

	def deleteMax(self):
		'''
Rimuovi l'elemento massimo da un max-heap A[]
'''
		pass;

	def sort(self):
		'''
HeapSort
'''
		pass;

#una funzione a caso da copia incollare e modificare
	def FUNZIONE(self):
		'''
Descrizione della FUNZIONE
'''
		pass;

