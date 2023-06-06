#!/bin/env/python3

import Comparable;

# i searched ho to do an interface in python and found this:
# https://realpython.com/python-interface/
#dovrei fare altre cose ma non lo capisco (Meta???)

#! NOTA BENE: il dizionario è già implementato in python nativamente...
#questo quindi è un esercizio che non servirà mai copiare! (tipo dict)
# si dichiarano tipo d = { key1: value1, key2, value2 };
#se cerchi dictionary python trovi tutto!
# https://www.w3schools.com/python/python_dictionaries.asp

from collections import namedtuple
class KeyData(namedtuple('KeyData', 'key data')):
	__slots__ = ()
	def __str__(self):
		return '('+str(self.key)+','+str(self.data)+')'

class myDictionaryInterface:

	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		pass;

	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		pass;

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		pass;

#test per tutti i tipi di classi che implementano la mia interfaccia
def test(dictionary: myDictionaryInterface):
	print(dictionary);
	dictionary.insert(1, 'ciao');
	print(dictionary);
	dictionary.insert(2, 'mare');
	print(dictionary);
	dictionary.insert(2, 'arcobaleno');
	print(dictionary);
	dictionary.delete(2);
	print(dictionary);

