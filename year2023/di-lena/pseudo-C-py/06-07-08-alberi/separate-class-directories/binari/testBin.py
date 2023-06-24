#!/usr/bin/env python3

import treeBin;

T1 = treeBin.treeBin('nonno');
T1.print();
n = T1.insertLeft(T1.radice, 'padreLeft');
T1.insertRight(T1.radice, 'zioRight');
T1.insertLeft(n, 'figlioLeft');
T1.insertRight(n, 'figlioRight');
T1.print();
print(f'There are {len(T1)} nodes.');
T1.visite();

T2 = treeBin.treeBin('A');
b = T2.insertLeft(T2.radice, 'B');
c = T2.insertRight(T2.radice, 'C');
T2.insertLeft(b, 'D');
T2.insertRight(b, 'E');
T2.insertLeft(c, 'F');
T2.insertRight(c, 'G');
T2.print();
print(f'There are {len(T2)} nodes.');
T2.visite();

T = treeBin.treeBin('mix');
T.insertTreeLeft(T.radice, T1);
T.insertTreeRight(T.radice, T2);
T.print();
print(f'There are {len(T)} nodes.');
T.visite();
T.draw();
