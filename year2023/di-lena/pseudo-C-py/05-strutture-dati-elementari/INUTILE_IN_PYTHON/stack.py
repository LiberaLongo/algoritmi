#!/usr/bin/env python3

import DictionaryInterface as dicI;
import Comparable;

class StackDictionary(dicI.myDictionaryInterface):

	#costruttore
	def __init__(self):
		self.s = []; #le liste sono già presenti in python

	#dictionary
	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		print(f'\t\tinsert -> push ({key},{data})');

	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		print(f'\t\tdelete -> pop ({key})');

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		print(f'\t\tsearch ({key})');

	#to string
	def __str__(self):
		pass;

stack = StackDictionary();
dicI.test(stack);

# e ora possiamo buttare via tutto :3
