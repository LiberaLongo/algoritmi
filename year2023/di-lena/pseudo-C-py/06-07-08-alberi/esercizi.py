#!/usr/bin/env python3

import treeAVL;

def esSlide():
	print('\n\n(es1) Dato un albero AVL T con chiavi intere inizialmente vuoto, disegnare l’albero ottenuto dalle operazioni di inserimento in ordine delle seguenti chiavi');
	avlT = treeAVL.treeAVL();
	avlT.insert(50); avlT.draw();
	avlT.insert(20); avlT.draw();
	avlT.insert(10); avlT.draw();
	avlT.insert(60); avlT.draw();
	avlT.insert(40); avlT.draw();
	avlT.insert(45); avlT.draw();
	avlT.print();
	print('\n\n(es2) Continuare con le seguenti operazioni (sull’albero precedente, mostrato sotto):');
	avlT.insert(85); avlT.draw();
	avlT.insert(55); avlT.draw();
	avlT.delete(40); avlT.draw();
	avlT.delete(45); avlT.draw();
	avlT.insert(15); avlT.draw();
	avlT.print();
	print('\n\n(es3) Continuare con le seguenti operazioni (sull’albero precedente, mostrato sotto):');
	avlT.insert(83); avlT.draw();
	avlT.delete(55); avlT.draw();
	avlT.insert(90); avlT.draw();
	avlT.delete(60); avlT.draw();
	avlT.print();
	print('\n\n(es4) Continuare con le seguenti operazioni (sull’albero precedente, mostrato sotto):');
	avlT.insert(5); avlT.draw();
	avlT.insert(13); avlT.draw();
	avlT.insert(17); avlT.draw();
	avlT.insert(65); avlT.draw();
	avlT.insert(1); avlT.draw();
	avlT.delete(90); avlT.draw();
	avlT.print();
	print('\n\n(es5) Continuare con le seguenti operazioni (sull’albero precedente, mostrato sotto):');
	avlT.delete(15); avlT.draw();
	avlT.delete(13); avlT.draw();
	avlT.delete(10); avlT.draw();
	avlT.delete(50); avlT.draw();
	avlT.print();

def es11main():
	print('\n\n(es11) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	avlT.insert(2); avlT.draw();
	avlT.insert(3); avlT.draw();
	avlT.insert(4); avlT.draw();
	avlT.insert(7); avlT.draw();
	avlT.delete(3); avlT.draw();
	avlT.delete(2); avlT.draw();
	avlT.insert(1); avlT.draw();
	avlT.insert(8); avlT.draw();
	avlT.insert(5); avlT.draw();
	avlT.insert(6); avlT.draw();
	avlT.print();

def es12main():
	print('\n\n(es12) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	avlT.insert(4); avlT.draw();
	avlT.insert(2); avlT.draw();
	avlT.insert(1); avlT.draw();
	avlT.insert(6); avlT.draw();
	avlT.insert(3); avlT.draw();
	avlT.insert(5); avlT.draw();
	avlT.insert(8); avlT.draw();
	avlT.insert(7); avlT.draw();
	avlT.delete(3); avlT.draw();
	avlT.delete(5); avlT.draw();
	avlT.print();

def es14main():
	print('\n\n(es14) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	avlT.insert(2); avlT.draw();
	avlT.insert(5); avlT.draw();
	avlT.insert(8); avlT.draw();
	avlT.insert(3); avlT.draw();
	avlT.insert(1); avlT.draw();
	avlT.insert(4); avlT.draw();
	avlT.insert(6); avlT.draw();
	avlT.insert(7); avlT.draw();
	avlT.print();

print('slide');
esSlide();
print('main');
es11main();
es12main();
es14main();

