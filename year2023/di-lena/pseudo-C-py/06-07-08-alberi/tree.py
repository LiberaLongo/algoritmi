#!/bin/env/python3

import node;

class tree:
	def __init__(self, info):
		self.radice = node.node(info);
#tree
	def radice(self):
		return self.radice;
	def insertNode(self, parent, info):
		return parent.insertChildren(node.node(info));
#print
	def print(self):
		print('Tree:', end='');
		self.radice.print();
		print();

T = tree('radice');
T.print();
n = T.insertNode(T.radice, 'padre');
T.insertNode(T.radice, 'fratello');
T.insertNode(n, 'figlio');
T.insertNode(n, 'secondo')
T.print();
