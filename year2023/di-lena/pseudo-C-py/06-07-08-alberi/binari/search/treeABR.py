#!/bin/env/python3

import nodeABR;
import queue;

class treeABR:
	def __init__(self):
		self.radice = None;

# dictionary
	def insert(self, key, data=None):
		n = nodeABR.nodeABR(key, data); #node
		p = None;		 #parent
		s = self.radice;
		#search position
		while s:
			p = s;
			if key < s.key:
				s = s.left;
			else:
				s = s.right;
		#insert node
		if not p: 
			self.radice = n; #the tree was empty
		else:
			n.parent = p;
			if key < p.key:
				p.left = n;
			else:
				p.right = n;

	def search(self, key):
		tmp = self.radice;
		while tmp:
			if key == tmp.key:
				return tmp;
			elif key < tmp.key:
				tmp = tmp.left;
			else:
				tmp = tmp.right;
		return None;		

#delete:
#case 1: il nodo da rimuovere è una foglia
#case 2: il nodo da rimuovere ha un solo figlio u
#case 3: il nodo da rimuvere ha due figli
	def deleteNode(self, node):
		p = node.parent;
		if p:	# node is not the root node
			if not node.left and not node.right: # case 1
				if p.left == node:
					p.left = None;
				else:
					p.right = None;
			elif node.right: # case 2
				if p.left == node:
					p.left = node.right;
				else:
					p.right = node.right;
			elif node.left: # case 3
				if p.left == node:
					p.left = node.left;
				else:
					p.right = node.left;
		else: #node is the root node
			if node.right: # case 2
				self.radice = node.right;
			else: # case 1 or case 2
				self.radice = node.left;			

	def delete(self, key):
		v = self.search(key);
		if v:
			if not v.left or not v.right: #case 1 or 2
				self.deleteNode(v);
			else:	#case 3
				u = self.predecessor(v);
				v.key = u.key;
				v.data = u.data;
				self.deleteNode(u);

# ABR
	def max(self, node):
		while node and node.right:
			node = node.right;
		return node;

	def min(self, node):
		while node and node.left:
			node = node.left;
		return node;

	def predecessor(self, node):
		if not node:
			return None;
		elif node.left: #case 1
			return self.max(node.left);
		else:			#case 2
			p = node.parent;
			while p and node == p.left:
				node = p;
				p = p.parent;
			return p;

	def successor(self):
		if not node:
			return None;
		elif node.right: #case 1
			return self.min(node.right);
		else:			 #case 2
			p = node.parent;
			while p and node == p.right:
				node = p;
				p = p.parent;
			return p;

# count nodes
	def countNodes(self, node):
		if not node:
			return 0;
		else:
			left_or_none = node.left if node.left else None;
			right_or_none = node.right if node.right else None;
			return 1 + self.countNodes(left_or_none) + self.countNodes(right_or_none);
	def __len__(self):
		return self.countNodes(self.radice);

# visite
	def visitaBFS(self):
		list = [];
		Q = queue.queue();
		if self.radice:
			Q.enqueue(self.radice);
		while not Q.isEmpty():
			x = Q.dequeue();
			list.append((x.key, x.data)); #visit(x)
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
					list.append((node.key, node.data));
					list = self.visitaDFS(ordine, left_or_none, list);
					list = self.visitaDFS(ordine, right_or_none, list);
				case 'in':
	# in-visita
					list = self.visitaDFS(ordine, left_or_none, list);
					list.append((node.key, node.data));
					list = self.visitaDFS(ordine, right_or_none, list);
				case 'post':
	# post-visita
					list = self.visitaDFS(ordine, left_or_none, list);
					list = self.visitaDFS(ordine, right_or_none, list);
					list.append((node.key, node.data));
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
