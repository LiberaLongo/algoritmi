import myQueue as queue;

#per disegnare
import networkx as nx;
import matplotlib.pyplot as plt;
# eseguire il comando 'pip install networkx matplotlib'

# utilizzo graphviz e pydot quindi potresti dover fare anche il comando:
# pip install pydot
# sudo apt install graphviz
# (pk provando 'pip install graphviz' non trova il file 'dot')
# dot -V
# questo comando dovrebbe dire la versione di graphviz se tutto va bene (e il file 'dot' viene trovato)

class treePlain(object):

#visite
	def visitaBFS(self):
		list = [];
		Q = queue.queue();
		if self.radice:
			Q.enqueue(self.radice);
		while not Q.isEmpty():
			x = Q.dequeue();
			list.append(x.key); #visit(x)
			for child in x.childrens:
				if child:
					Q.enqueue(child);
		return list;
		
	def visitaDFS(self, ordine, node, list):
		if node:
			match ordine:
				case 'pre':
	# pre-visita
					list.append(node.key);
					for child in node.childrens:
						list = self.visitaDFS(ordine, child, list);
				case 'in':
	# in-visita
					first_or_none = node.childrens[0] if node.childrens else None;
					list = self.visitaDFS(ordine, first_or_none, list);
					list.append(node.key);
					for other_child in node.childrens[1:]:
						list = self.visitaDFS(ordine, other_child, list);
				case 'post':
	# post-visita
					for child in node.childrens:
						list = self.visitaDFS(ordine, child, list);
					list.append(node.key);
				case _:
					print('Error! Usage: ordine = \'pre\' | \'in\' | \'post\'');
		return list;
	
	def visitaDepthFS(self, ordine):
		print(f'{ordine}-visita:\t', self.visitaDFS(ordine, self.radice, []));

	def visit(self):
		self.visitaDepthFS('pre');
		self.visitaDepthFS('in');
		self.visitaDepthFS('post');
		print('\tBFS:\t', self.visitaBFS());
#print
	def __str__(self):
		return f'tree: {self.radice}';

#draw
	def drawGraph(self, Graph, node):
		#inserisci ogni nodo e ogni arco
		if node:
			for child in node.childrens:
				if child:
					#debug
					if child.parent is not node:
						print(f'ERROR! drawing {child.key} i have seen he haven\'t {node.key} as parent but he have {child.parent}!');
					#code
					Graph.add_node(child.key, height=child.height);
					Graph.add_edge(node.key, child.key);
					self.drawGraph(Graph, child);

	def draw(self):
		#voglio disegnare quindi uso le cose già fatte... ok?
		if self.radice:
			#G è un grafo orientato
			G = nx.DiGraph();
			#inserisci la radice
			G.add_node(self.radice.key, height=self.radice.height);
			#inserisci tutti gli altri nodi e tutti gli altri archi
			self.drawGraph(G, self.radice);

			#disegna G come se fosse un albero!
			# Disegna l'albero utilizzando il layout "dot" con nx_pydot
			pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot');
			# Disegna i nodi
			nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='lightblue');
			# Disegna gli archi
			nx.draw_networkx_edges(G, pos, arrows=True);
			# Disegna le etichette dei nodi
			node_labels = {node: f'{node}\nh={G.nodes[node]["height"]}' for node in G.nodes}
			nx.draw_networkx_labels(G, pos, labels=node_labels)
			# Mostra il grafico
			plt.axis('off');
			plt.show();

#show => print, visit, draw
	def show(self):
		self.print();
		self.visit();
		self.draw();
