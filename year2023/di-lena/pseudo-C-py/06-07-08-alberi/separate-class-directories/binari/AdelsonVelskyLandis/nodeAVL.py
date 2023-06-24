#!/usr/bin/env python3

class nodeAVL:
	def __init__(self, key, data=None):
		self.key = key;
		self.data = data;
		self.parent = None;
		self.right = None;
		self.left = None;
		self.height = 0;

#NOTA: nelle slide il prof 'sostituisce il contenuto dei nodi' con l'operazione 'p.right = v.right'
#ma in python questo viene passato come nodo quindi non viene settato il padre!

	def setLeft(self, node):
		self.left = node;
		node.parent = self;
	
	def setRight(self, node):
		self.right = node;
		node.parent = self;

#print
	def print(self):
		print(f'(<{self.key},{self.data}>:[', end='');
		if self.left:
			print(' l:', end='');
			self.left.print();
		if self.right:
			print(' r:', end='');
			self.right.print();
		print('])', end='');

# AdelsonVelskyLandis modifications to ABR
	def updateHeight(self, node): #cost O(1)
		if node:
			nh = lh = rh = 0;
			if node.left:
				lh = node.left.height;
			if node.right:
				rh = node.right.height;
			if node.left or node.right:
				nh = max(lh, rh) +1;
			node.height = nh;

	def betha(self): #cost O(1)
		lh = rh = 0;
		if node.left:
			lh = node.left.height;
		if node.right:
			rh = node.right.height;
		return lh - rh;
