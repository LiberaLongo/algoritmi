#!/usr/bin/env python3

import treeAVL;

def es11main():
	print('\n\n(es11) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	print('(a) insert 2'); avlT.insert(2); avlT.draw();
	print('(b) insert 3'); avlT.insert(3); avlT.draw();
	print('(c) insert 4'); avlT.insert(4); avlT.draw();
	print('(d) insert 7'); avlT.insert(7); avlT.draw();
	avlT.print();
	print('(e) delete 3'); avlT.delete(3); avlT.draw();
	avlT.print();
	print('(f) delete 2'); avlT.delete(2); avlT.draw();
	avlT.print();
	print('(g) insert 1'); avlT.insert(1); avlT.draw(); avlT.print();
	print('(h) insert 8'); avlT.insert(8); avlT.draw(); avlT.print();
	print('(i) insert 5'); avlT.insert(5); avlT.draw(); avlT.print();
	print('(j) insert 6'); avlT.insert(6); avlT.draw(); avlT.print();

def es12main():
	print('\n\n(es12) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	print('(a) insert 4'); avlT.insert(4); avlT.draw();
	print('(b) insert 2'); avlT.insert(2); avlT.draw();
	print('(c) insert 1'); avlT.insert(1); avlT.draw();
	print('(d) insert 6'); avlT.insert(6); avlT.draw();
	print('(e) insert 3'); avlT.insert(3); avlT.draw();
	print('(f) insert 5'); avlT.insert(5); avlT.draw();
	print('(g) insert 8'); avlT.insert(8); avlT.draw();
	print('(h) insert 7'); avlT.insert(7); avlT.draw();
	avlT.print();
	print('(i) delete 3'); avlT.delete(3); avlT.draw();
	avlT.print();
	print('(j) delete 5'); avlT.delete(5); avlT.draw();
	avlT.print();

def es14main():
	print('\n\n(es14) Dato un albero AVL inizialmente vuoto effettuare le seguenti operazioni in ordine e mostrare lo stato dell’albero dopo ogni operazione:');	
	avlT = treeAVL.treeAVL();
	print('(a) insert 2'); avlT.insert(2); avlT.draw();
	print('(b) insert 5'); avlT.insert(5); avlT.draw();
	print('(c) insert 8'); avlT.insert(8); avlT.draw();
	print('(d) insert 3'); avlT.insert(3); avlT.draw();
	print('(e) insert 1'); avlT.insert(1); avlT.draw();
	print('(f) insert 4'); avlT.insert(4); avlT.draw();
	print('(g) insert 6'); avlT.insert(6); avlT.draw();
	print('(h) insert 7'); avlT.insert(7); avlT.draw();
	avlT.print();

#es11main();
es12main();
es14main();

