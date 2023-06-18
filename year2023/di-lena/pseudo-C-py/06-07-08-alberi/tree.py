#!/usr/bin/env python3

import node;
import queue;

class tree:
	def __init__(self, info):
		self.radice = node.node(info);
#tree
	def insert(self, parent, info):
		return parent.insertChildren(node.node(info));

	def insertTree(self, parent, tree):
		return parent.insertChildren(tree.radice);
	
#visite
	def visitaBFS(self):
		list = [];
		Q = queue.queue();
		if self.radice:
			Q.enqueue(self.radice);
		while not Q.isEmpty():
			x = Q.dequeue();
			list.append(x.info); #visit(x)
			for child in x.childrens:
				Q.enqueue(child);
		return list;
		
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
					for other_child in node.childrens[1:]:
						list = self.visitaDFS(ordine, other_child, list);
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

	def visite(self):
		self.visitaDepthFS('pre');
		self.visitaDepthFS('in');
		self.visitaDepthFS('post');
		print('\tBFS:\t', self.visitaBFS());

#print
	def print(self):
		print('\nTree: ', end='');
		self.radice.print();
		print();
