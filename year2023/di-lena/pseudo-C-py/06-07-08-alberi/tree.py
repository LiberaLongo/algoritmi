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

	def visitaDFS(self, ordine, node, list):
		match ordine:
			case 'pre':
# pre-visita
				list.append(node.info);
				for child in node.childrens:
					list = self.visitaDFS(ordine, child, list);
			case 'in':
# in-visita
				print('TODO');
			case 'post':
# post-visita
				for child in node.childrens:
					list = self.visitaDFS(ordine, child, list);
				list.append(node.info);
			case _:
				print('Error! Usage: ordine = \'pre\' | \'in\' | \'post\'');
		return list;
	
	def visitaDepthFS(self, ordine):
		print(f'{ordine}-visita:\t', T.visitaDFS(ordine, self.radice, []));

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
T.visitaDepthFS('pre');
T.visitaDepthFS('in');
T.visitaDepthFS('post');
