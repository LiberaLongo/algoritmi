import myQueue as queue;

#per disegnare
import networkx as nx;
import matplotlib.pyplot as plt;
# eseguire il comando 'pip install networkx matplotlib'

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
					Graph.add_node(child.key);
					Graph.add_edge(node.key, child.key);
					self.drawGraph(Graph, child);

	def draw(self):
		#voglio disegnare quindi uso le cose già fatte... ok?
		if self.radice:
			G = nx.DiGraph();
			G.add_node(self.radice.key);
			self.drawGraph(G, self.radice);
			nx.draw(G, with_labels=True);
			plt.show();

#show => print, visit, draw
	def show(self):
		self.print();
		self.visit();
		self.draw();
