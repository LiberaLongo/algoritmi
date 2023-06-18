#!/usr/bin/env python3

class nodeBin:
	def __init__(self, info):
		self.info = info;
		self.parent = None;
		self.right = None;
		self.left = None;

#childerns
	def insertLeft(self, node):
		node.parent = self;
		self.left = node;
		return node;

	def insertRight(self, node):
		node.parent = self;
		self.right = node;
		return node;

#print
	def print(self):
		print(f'({self.info}:[', end='');
		if self.left:
			print(' l:', end='');
			self.left.print();
		if self.right:
			print(' r:', end='');
			self.right.print();
		print('])', end='');
