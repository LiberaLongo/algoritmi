#!/usr/bin/env python3

import tree;

T1 = tree.tree('radice');
T1.print();
n = T1.insert(T1.radice, 'padre');
T1.insert(T1.radice, 'fratello');
T1.insert(n, 'figlio');
T1.insert(n, 'secondo')
T1.print();
T1.visite();

T2 = tree.tree('A');
b = T2.insert(T2.radice, 'B');
c = T2.insert(T2.radice, 'C');
T2.insert(T2.radice, 'H');
T2.insert(b, 'D');
T2.insert(b, 'E');
T2.insert(b, 'I');
T2.insert(c, 'F');
T2.insert(c, 'G');
T2.print();
T2.visite();

T = tree.tree('mix');
T.insertTree(T.radice, T1);
T.insertTree(T.radice, T2);
T.print();
T.visite();
