#!/bin/env/python3

import node;

class tree:
	def __init__(self, info):
		self.radice = node.node(info);
#tree
	def insertNode(self, parent, info):
		return parent.insertChildren(node.node(info));
	
#visite
	def visitaDFS(self, ordine, node, list):
		if node:
			match ordine:
				case 'pre':
	# pre-visita
					list.append(node.info);
					for child in node.childrens:
						list = self.visitaDFS(ordine, child, list);
				case 'in':
	# in-visita
					first_or_none = node.childrens[0] if node.childrens else None;
					list = self.visitaDFS(ordine, first_or_none, list);
					list.append(node.info);
					next_or_none = node.childrens[node.index+1] if len(node.childrens) > node.index else None;
					list = self.visitaDFS(ordine, next_or_none, list);
				case 'post':
	# post-visita
					for child in node.childrens:
						list = self.visitaDFS(ordine, child, list);
					list.append(node.info);
				case _:
					print('Error! Usage: ordine = \'pre\' | \'in\' | \'post\'');
		return list;
	
	def visitaDepthFS(self, ordine):
		print(f'{ordine}-visita:\t', self.visitaDFS(ordine, self.radice, []));

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
