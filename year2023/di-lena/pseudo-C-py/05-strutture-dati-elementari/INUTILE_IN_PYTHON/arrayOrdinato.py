#!/usr/bin/env python3

import DictionaryInterface as dicI;
import Comparable;

#! NOTA BENE: il dizionario è già implementato in python nativamente...
#questo quindi è un esercizio che non servirà mai copiare! (tipo dict)
#ausiliarie

#tento di unire binSearcPos e binSearch
#facendo in modo di tornare quello che serve...

def searchBinaryPos(A, key):
	i = 0;
	j = len(A);
	while i < j: #a che serve l'uguale del <= dello pseudocodice ?
		M = (i+j) // 2;
		if A[M].key == key:
			return (M, True);
		elif A[M].key < key:
			i = M +1;
		else:
			j = M -1;
	return (i, False);
	
def binsearch(Array, key):
	(value, finded) = searchBinaryPos(Array, key);
	if not finded:
		return -1;
	return value;

#binsearchPos ovvero value di (value, finded) restituito da searchBinaryPos non ha senso pk devo sapere che istruzione sugli array di Python devo fare (visto che questi non sono proprio uguali al C e hanno operazioni diverse)

#non usate pk in python gli array non funzionano così...
def leftshift(Array, i):
	for j in range(i, size-1):
		Array[j] = Array[j+1];

def rigthshift(Array, i):
	for j in range(i, size +1):
		A[j+1] = A[j]


class ArrayOrdinatoDictionary(dicI.myDictionaryInterface):

	#costruttore
	def __init__(self):
		self.Array = [];

	#dictionary
	def insert(self, key: Comparable, data: object) -> None:
		"""Aggiunge al dizionario la coppia (key, data)"""
		print(f'\t\tinsert ({key},{data})', end=' ');
		#codice diverso dalle slide per python / array
		(i,found) = searchBinaryPos(self.Array, key);
		da_inserire = dicI.KeyData(key, data);
		if found:	#se ho trovato
			if self.Array[i].key == key:
				print('replace');
				self.Array[i] = da_inserire;
			else:
				print('insert');
				self.Array.insert(i, da_inserire);
		else:
			print('append');
			self.Array.append(da_inserire);
		
	def delete(self, key: Comparable) -> None:
		"""Rimuove dal dizionario l'elemento con chiave key"""
		print(f'\t\tdelete ({key})');
		i = binsearch(self.Array, key);
		if not i == -1:
			self.Array.pop(i);
			#leftshift(self.Array, self.i);

	def search(self, key: Comparable) -> object:
		"""Restituisce l'elemento data con chiave k"""
		print(f'\t\tsearch ({key})');
		i = binsearch(self.Array, key);
		if not i == -1 :
			return self.Array[i].data;
		else:
			return None;

	#to string
	def __str__(self):
		string = '['
		for kd in self.Array:
			string = string + str(kd);
		return string + ']';

print(issubclass(ArrayOrdinatoDictionary, dicI.myDictionaryInterface));

print('method resolution order: ' , ArrayOrdinatoDictionary.__mro__);

ardict = ArrayOrdinatoDictionary();
dicI.test(ardict);

# e ora possiamo buttare via tutto :3
