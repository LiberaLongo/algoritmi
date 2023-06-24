#!/usr/bin/env python3

import tree;
import treeBin;
import treeABR;
import treeAVL;

T = tree.tree('key', 'data');
mamma = T.insert(T.radice, 'Laura', 'Mazzanti');
T.insert(mamma, 'Libera', 'Longo');
T.print();
T.visit();
T.draw();

bT = treeBin.treeBin('key', 'data');
left = bT.insert(bT.radice, True, 'Left', 'Sinistra');
bT.insert(bT.radice, False, 'Right', 'Destra');
bT.insert(left, True, 'nipote', 'left');
bT.print();
bT.visit();
bT.draw();

abrT = treeABR.treeABR(10, 'key');
abrT.insert(7);
abrT.insert(13);
abrT.insert(6);
abrT.insert(8);
abrT.insert(15);
abrT.insert(9);
abrT.print();
abrT.visit();
abrT.draw();

avlT = treeAVL.treeAVL('key', 'data');
avlT.print();
avlT.visit();
avlT.draw();
