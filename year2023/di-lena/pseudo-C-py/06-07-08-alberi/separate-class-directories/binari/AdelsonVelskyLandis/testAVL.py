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
#T.delete(10);
T.print();
T.draw();
