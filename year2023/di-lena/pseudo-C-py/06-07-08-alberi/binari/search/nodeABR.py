#!/bin/env/python3

class nodeABR:
	def __init__(self, key, data=None):
		self.key = key;
		self.data = data;
		self.parent = None;
		self.right = None;
		self.left = None;

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
