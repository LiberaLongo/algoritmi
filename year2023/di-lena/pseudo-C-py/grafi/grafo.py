#!/usr/bin/env python3

#nota che sulle slide sono implementate tramite dizionari
#e in python i dizionari sono un tipo speciale chiamato 'dict' che useremo ora!

import networkx as nx;
import matplotlib.pyplot as plt;

class grafo:
	def __init__(self):
		self.dizG = {};

#operazioni che la struttura dati GRAFO deve supportare:
	def numVertici(self):
		#return int
		pass

	def numArchi(self):
		#return int
		pass

	def grado(self, vertice):
		#return int
		pass

	def archiIncidenti(self, vertice):
		#return list of archi
		pass

	def estremi(self, arco):
		#return list of nodi
		pass

	def opposto(self, vertice, arco):
		#return nodo
		pass

	def sonoAdiacenti(self, src, dst):
		#return bool
		pass

	def aggiungiVertice(self, vertice):
		print(f'aggiungi Vertice({vertice})');
		self.dizG[vertice] = {};

	def aggiungiArco(self, src, dst, etichetta=None):
		print(f'aggiungi Arco({src}, {dst}, {etichetta})');
		# Verifica se il nodo sorgente esiste nel dizG
		try:
			self.dizG[src][dst] = etichetta;
		except:
			print('Nodo di partenza non trovato');

	def rimuoviVertice(self, vertice):
		try:
			del self.dizG[vertice];
			# Rimuovi tutti gli archi che hanno come destinazione il vertice da rimuovere
			for src in self.dizG:
				if vertice in self.dizG[src]:
					del self.dizG[src][vertice];
		except KeyError:
			print('Vertice non trovato');


	def rimuoviArco(self, src, dst):
		print(f'rimuovi Arco({src}, {dst})');
		try:
			del self.dizG[src][dst];
		except:
			print('Arco non trovato');

#rappresentazioni
	def draw(self):
		#print del dizionario...
		print('draw', self.dizG);

		# Crea il grafo con networkX (la libreria per disegnarlo)
		G = nx.DiGraph();

		# aggiungi i nodi
		for nodo in self.dizG:
			G.add_node(nodo);

		# aggiungi gli archi
		for src in self.dizG:
			for dst, _ in self.dizG[src].items():
				G.add_edge(src, dst);
		
		# etichette tramite plt.text()
		pos = nx.circular_layout(G)
		nx.draw_networkx(G, pos)

		for src in self.dizG:
			for dst, label in self.dizG[src].items():
				if label:
					x = (pos[src][0] + pos[dst][0]) / 2
					y = (pos[src][1] + pos[dst][1]) / 2
					plt.text(x, y, label, color='red', fontsize=8, fontweight='bold', horizontalalignment='center', verticalalignment='center')

		# e disegno
		plt.axis('off')
		plt.show()
