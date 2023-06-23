#!/usr/bin/env python3

import treeAVL;

# 2

T = treeAVL.treeAVL();
T.insert(11, '11');
T.insert(8, '8');
T.insert(13, '13');
T.insert(6, '6');
T.insert(9, '9');
T.insert(15, '15');
T.insert(7, '7');
T.insert(10, '10');
T.print();
T.visite();
#delete test
search_key = 10; #già testati 10
n = T.search(search_key);
print(f'n has key {n.key}, and parent {n.parent.key}.');
T.delete(10); #già testati: 9
T.print();
n = T.search(search_key);
print(f'n has key {n.key}, and parent {n.parent.key}.');

