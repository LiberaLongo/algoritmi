#!/bin/env/python3

import treeABR;

T = treeABR.treeABR();
T.insert(5, 'five');
T.insert(2, 'two');
T.insert(7, 'seven');
T.insert(1, 'one');
T.insert(3, 'three');
T.insert(4, 'four');
T.insert(6, 'six');
T.insert(8, 'eight');
T.insert(9, 'nine');
T.print();
T.visite();
#delete test
T.delete(10);
T.print();
max = T.max(T.radice)
print(f'il massimo è {max.key}, e suo padre è {max.parent.key}');
T.delete(8); #case 2
T.print();
max = T.max(T.radice)
print(f'il massimo è {max.key}, e suo padre è {max.parent.key}');
T.delete(9); #case 1
T.print();
T.delete(7); #case 3
T.print();
