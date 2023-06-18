#!/usr/bin/env python3

import DictionaryInterface as dicI;
import Comparable;

class Node():
	def __init__(self, k: Comparable, e: object):
		self.elem = e;
		self.key = k;
		self.next = self.prev = None;

class ListDictionary(dicI.myDictionaryInterface):

	#costruttore
	def __init__(self):
		self.head = None;

	#dictionary
	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		print(f'\t\tinsert ({key},{data})');
		p = Node(key, data);
		if self.head == None:
			self.head = p.prev = p.next = p;
		else:
			p.next = self.head.next;
			self.head.next.prev = p;
			self.next = p;
			p.prev = self.head;

	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		print(f'\t\tdelete ({key})');
		if self.head:
			if 

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		print(f'\t\tsearch ({key})');
		tmp = self.head;
		while not tmp == None:
			if tmp.key == k:
				return tmp;
			tmp = tmp.next;
		return None;

	#to string
	def __str__(self):
		pass;

lista = ListDictionary();
dicI.test(lista);

# e ora possiamo buttare via tutto :3
