#!/bin/env/python3

import DictionaryInterface as dicI;
import Comparable;

#! NOTA BENE: il dizionario è già implementato in python nativamente...
#questo quindi è un esercizio che non servirà mai copiare! (tipo dict)
#ausiliarie
def linsearch(Array, size, key):
	for i in range(size):
		if Array[i].key == key:
			return i;
	return -1;

def leftshift(Array, size, i):
	for j in range(i, size-1):
		Array[j] = Array[j+1];

class ArrayNonOrdinatoDictionary(dicI.myDictionaryInterface):

	#costruttore
	def __init__(self):
		self.Array = [];
		self.size = len(self.Array);

	#dictionary
	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		print(f'\t\tinsert ({key},{data})');
		i = linsearch(self.Array, self.size, key);
		da_inserire = dicI.KeyData(key, data);
		if i == -1:
			self.size = self.size +1;
			self.Array.append(da_inserire);
			return;
		# deleting the list item at the given index using the del keyword
		del self.Array[i];
		self.Array.insert(i, da_inserire);

	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		print(f'\t\tdelete ({key})');
		i = linsearch(self.Array, self.size, key);
		if not i == -1:
			self.Array.pop(i);
			#leftshift(self.Array, self.size, i);
			self.size = self.size -1;

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		print(f'\t\tsearch ({key})');
		i = linsearch(self.Array, self.size, key);
		if not i == -1 :
			return self.Array[i].data
		else:
			return None;
	#to string
	def __str__(self):
		string = '['
		for kd in self.Array:
			string = string + str(kd);
		return string + ']';

print(issubclass(ArrayNonOrdinatoDictionary, dicI.myDictionaryInterface));

print('method resolution order: ' , ArrayNonOrdinatoDictionary.__mro__);

ardict = ArrayNonOrdinatoDictionary();
dicI.test(ardict);

# e ora possiamo buttare via tutto :3
