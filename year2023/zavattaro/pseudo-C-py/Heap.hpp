#ifndef HEAP_HPP
#define HEAP_HPP

#define DIM 100

class Heap {
	int A[]
/*
Individua il valore massimo contenuto in uno heap
- il massimo è sempre la radice (ossia A[1])
- L'operazione ha costo Theta(1) ==> costante
*/
	def findMax(){}
/*
Ripristinare la propietà di max-heap
- Supponiamo di rimpiazzare la radice A[1] di un max-heap con un valore qualsiasi
- Vogliamo fare in modo che A[] diventi nuovamente uno heap
*/
	def fixHeap(){}
/*
Costruire uno heap a partire da un array privo di alcun ordine
*/
	def heapify(){}
/*
Rimuovi l'elemento massimo da un max-heap A[]
*/
	def deleteMax(){}
/*
HeapSort
*/
	def sort(){}
#endif //HEAP_HPP

