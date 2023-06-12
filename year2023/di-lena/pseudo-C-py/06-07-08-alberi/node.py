#!/bin/env/python3

class node:
	def __init__(self, info):
		self.info = info;
		self.parent = None;
		self.childrens = [];
		self.tree = None; #albero a cui questo noto è associato

#childerns
	def insertChildren(self, node):
		self.childrens.append(node);
		return node;

#print
	def print(self):
		print(f'({self.info}', end='');
		if self.childrens:
			print(':[', end='');
			for node in self.childrens:
				node.print();
			print(']', end='');
		print(')', end='');
