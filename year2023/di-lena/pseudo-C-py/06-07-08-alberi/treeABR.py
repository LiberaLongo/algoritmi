import treeBin;
import nodeBin;

class treeABR(treeBin.treeBin):

# dictionary
	def insert(self, key, data=None):
		n = nodeBin.nodeBin(key, data); #node
		p = None;		 #parent
		s = self.radice;
		#search position
		while s:
			p = s;
			if key < s.key:
				s = s.getLeft();
			else:
				s = s.getRight();
		#insert node
		if not p: 
			self.radice = n; #the tree was empty
		else:
			n.parent = p; #already done in the set... functions
			if key < p.key:
				p.setLeft(n);
			else:
				p.setRight(n);
# pseudo code forgot it but i need it in AVL tree
		return n;

	def search(self, key):
		tmp = self.radice;
		while tmp:
			if key == tmp.key:
				return tmp;
			elif key < tmp.key:
				tmp = tmp.getLeft();
			else:
				tmp = tmp.getRight();
		print(f'i don\'t find {key} in the tree.');
		return None;		

#delete:
#case 1: il nodo da rimuovere è una foglia
#case 2: il nodo da rimuovere ha un solo figlio u
#case 3: il nodo da rimuvere ha due figli

	def deleteNode(self, node):
#		print(f'deleteNode({node.key})');
		p = node.parent;
		if p:	# node is not the root node
#			print('non root');
			if not node.getLeft() and not node.getRight(): # case 1
#				print('case 1');
				if p.getLeft == node:
					p.setLeft(None);
				else:
					p.setRight(None);
			elif node.getRight(): # case 2
#				print('case 2');
				if p.getLeft() == node:
					node.getRight().parent = p;
					p.setLeft(node.getRight());
				else:
					node.getRight().parent = p;
					p.setRight(node.getRight());
			elif node.getLeft(): # case 3
#				print('case 3');
				if p.getLeft() == node:
					node.getLeft().parent = p;
					p.setLeft(node.getLeft());
				else:
					node.getLeft().parent = p;
					p.setRight(node.getLeft());
		else: #node is the root node
#			print('root case');
			if node.getRight(): # case 2
				self.radice = node.getRight();
			else: # case 1 or case 2
				self.radice = node.getLeft();			

	def delete(self, key):
		print(f'delete({key})');
		v = self.search(key);
		if v:
			if not v.getLeft() or not v.getRight(): #case 1 or 2
#				print('case 1 or 2');
				#why here no parent is checked?
				self.deleteNode(v);
			else:	#case 3
#				print('case 3');
				u = self.predecessor(v);
				v.key = u.key;
				v.data = u.data;
				self.deleteNode(u);

# ABR
	def max(self, node):
		while node and node.getRight():
			node = node.getRight();
		return node;

	def min(self, node):
		while node and node.getLeft():
			node = node.getLeft();
		return node;

	def predecessor(self, node):
		if not node:
			return None;
		elif node.getLeft(): #case 1
			return self.max(node.getLeft());
		else:			#case 2
			p = node.parent;
			while p and node == p.getLeft():
				node = p;
				p = p.parent;
			return p;

	def successor(self):
		if not node:
			return None;
		elif node.getRight(): #case 1
			return self.min(node.getRight());
		else:			 #case 2
			p = node.parent;
			while p and node == p.getRight():
				node = p;
				p = p.parent;
			return p;

	def print(self):
		print(f'{self.name} ABR {self}');
