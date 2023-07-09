#!/usr/bin/env python3

#nota che sulle slide sono implementate tramite dizionari
#e in python i dizionari sono un tipo speciale chiamato 'dict' che useremo ora!

import networkx as nx;
import matplotlib.pyplot as plt;

all_layout = {
    'circular': nx.circular_layout,
    'random': nx.random_layout,
    'shell': nx.shell_layout,
    'spring': nx.spring_layout,
    'spectral': nx.spectral_layout,
    'kawai': nx.kamada_kawai_layout
}

class grafo:
	def __init__(self):
		self.dizG = {};

#operazioni che la struttura dati GRAFO deve supportare:

#creazione
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

# altre operazioni che la struttura dati dovrebbe supportare
	def numVertici(self):
		return len(self.dizG.keys());

	def numArchi(self):
		num_edges = 0;
		for node in self.dizG:
			num_edges += len(self.dizG[node]);
		return num_edges;

	def grado(self, vertice):
		if node in self.dizG:
			return len(self.dizG[node]);
		return 0;

	def archiIncidenti(self, vertice):
		if node in self.dizG:
			return list(self.dizG[node].keys());
		return [];

	def sonoAdiacenti(self, node1, node2):
		if node1 in self.dizG and node2 in self.dizG:
			return node2 in self.dizG[node1] or node1 in self.dizG[node2];
		return False;

#queste funzioni hanno senso solo se gli archi possono avere etichette o venisse usata un altra rappresentazione del grafo...
	def estremi(self, edge_label):
		lista = [];
		for node, outgoing_edges in self.dizG.items():
			if edge_label in outgoing_edges.values():
				lista.append(node);
		return lista;

	def opposto(self, start_node, edge_label):
		vertici = []
		for end_node, outgoing_edges in self.dizG.items():
			if start_node in outgoing_edges and outgoing_edges[start_node] == edge_label:
				vertici.append(end_node)
		return vertici

#rappresentazioni
	def __str__(self):
		string = 'grafo = {'
		string += "".join([f"\n\t'{k}': {v}" for k, v in self.dizG.items()]);
		string += '\n}';
		return string;

	def draw(self, layout='kawai'):
		#print del dizionario...
		print('draw', self);

		# Crea il grafo con networkX (la libreria per disegnarlo)
		G = nx.DiGraph();

		# aggiungi nodi
		for src in self.dizG:
			G.add_node(src);

		# aggiungi archi
		for src in self.dizG:
			for dst, label in self.dizG[src].items():
				# aggiungi arco
				G.add_edge(src, dst);
		
		# etichette tramite plt.text()
		layout_func = all_layout.get(layout);
		if layout_func is None:
			print("Invalid layout:", layout);
			print("Available layouts:", list(all_layout.keys()));
			return;
		pos = layout_func(G);
		nx.draw_networkx(G, pos);

		for src in self.dizG:
			for dst, label in self.dizG[src].items():
				if label:
					x = (pos[src][0] + pos[dst][0]) / 2;
					y = (pos[src][1] + pos[dst][1]) / 2;
					plt.text(x, y, label, color='red', fontsize=8, fontweight='bold', horizontalalignment='center', verticalalignment='center');

		# e disegno
		plt.axis('off');
		plt.show();
	
	def drawAllLayout(self):
		for layout in all_layout:
			self.draw(layout);
