#!/usr/bin/env python3

import tree;
import treeBin;
import treeABR;
import treeAVL;

def treetest():
	T = tree.tree('key', 'data');
	mamma = T.insert(T.radice, 'Laura', 'Mazzanti');
	T.insert(mamma, 'Libera', 'Longo');
	T.show();

def binarytreetest():
	bT = treeBin.treeBin('key', 'data');
	left = bT.insert(bT.radice, True, 'Left', 'Sinistra');
	bT.insert(bT.radice, False, 'Right', 'Destra');
	bT.insert(left, True, 'nipote', 'left');
	bT.show();

def ABRtest():
	abrT = treeABR.treeABR(10, 'key');
	abrT.insert(7);
	abrT.insert(13);
	abrT.insert(6);
	abrT.insert(8);
	abrT.insert(15);
	abrT.insert(9);
	abrT.insert(22);
	abrT.show();

def AVLtest():
	avlT = treeAVL.treeAVL();
	for i in range(1, 21): #range(9, 0, -1) to go from 9 to 0
		avlT.insert(i);
		#avlT.draw(); #se vuoi disegnare l'albero step by step scommenta questa riga
	avlT.show();

treetest();
binarytreetest();
ABRtest();
AVLtest();
