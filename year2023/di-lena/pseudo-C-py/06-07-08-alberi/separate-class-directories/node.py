#!/usr/bin/env python3

class node:
	def __init__(self, info):
		self.info = info;
		self.parent = None;
		self.childrens = [];
		self.index = 0; #a index used for small stuff... it can be removed...

#childerns
	def insertChildren(self, node):
		node.parent = self;
		node.index = len(self.childrens);
		self.childrens.append(node);
		return node;

#print
	def print(self):
		print(f'({self.info}', end='');
		if self.childrens:
			print(' :[ ', end='');
			for node in self.childrens:
				if node.index > 0:
					print(' --> ', end='');
				node.print();
			print(' ]', end='');
		print(')', end='');

