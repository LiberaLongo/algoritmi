#!/usr/bin/env python3

import DictionaryInterface as dicI;
import Comparable;

class QueueDictionary(dicI.myDictionaryInterface):

	#costruttore
	def __init__(self):
		self.q = []; #le liste sono già presenti in python
		#inoltre quando utilizzo le code preferisco usare '06-07-08-alberi/queue.py'
		#che utilizza 'from collections import deque'

	#dictionary
	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		print(f'\t\tinsert -> enqueue ({key},{data})');

	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		print(f'\t\tdelete -> dequeue ({key})');

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		print(f'\t\tsearch ({key})');

	#to string
	def __str__(self):
		pass;

queue = QueueDictionary();
dicI.test(queue);

# e ora possiamo buttare via tutto :3
