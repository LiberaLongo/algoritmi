#!/bin/env/python3

import nodeBin;
import queue;

class treeBin:
	def __init__(self, info):
		self.radice = nodeBin.nodeBin(info);
#tree
	def insertLeft(self, parent, info):
		return parent.insertLeft(nodeBin.nodeBin(info));
	def insertRight(self, parent, info):
		return parent.insertRight(nodeBin.nodeBin(info));

	def insertTreeLeft(self, parent, tree):
		return parent.insertLeft(tree.radice);
	def insertTreeRight(self, parent, tree):
		return parent.insertRight(tree.radice);

#count nodes
	def countNodes(self, node):
		if not node:
			return 0;
		else:
			left_or_none = node.left if node.left else None;
			right_or_none = node.right if node.right else None;
			return 1 + self.countNodes(left_or_none) + self.countNodes(right_or_none);
	def __len__(self):
		return self.countNodes(self.radice);

#visite
	def visitaBFS(self):
		list = [];
		Q = queue.queue();
		if self.radice:
			Q.enqueue(self.radice);
		while not Q.isEmpty():
			x = Q.dequeue();
			list.append(x.info); #visit(x)
			if x.left:
				Q.enqueue(x.left);
			if x.right:
				Q.enqueue(x.right);
		return list;
		
	def visitaDFS(self, ordine, node, list):
		if node:
			left_or_none = node.left if node.left else None;
			right_or_none = node.right if node.right else None;
			match ordine:
				case 'pre':
	# pre-visita
					list.append(node.info);
					list = self.visitaDFS(ordine, left_or_none, list);
					list = self.visitaDFS(ordine, right_or_none, list);
				case 'in':
	# in-visita
					list = self.visitaDFS(ordine, left_or_none, list);
					list.append(node.info);
					list = self.visitaDFS(ordine, right_or_none, list);
				case 'post':
	# post-visita
					list = self.visitaDFS(ordine, left_or_none, list);
					list = self.visitaDFS(ordine, right_or_none, list);
					list.append(node.info);
				case _:
					print('Error! Usage: ordine = \'pre\' | \'in\' | \'post\'');
		return list;
	
	def visitaDepthFS(self, ordine: str):
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
