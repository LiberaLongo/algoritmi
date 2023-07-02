import treeBin;
import nodeBin;

class treeABR(treeBin.treeBin):
	def __init__(self, name=''):
		self.name = name;
		self.radice = None;

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

	def deleteNode(self, v):
		print(f'deleteNode({v.key})');
		p = v.parent;
		if p:	# v is not the root node
#			print('non root');
			if p.getLeft() == v:
#				print('left');
				if v.getRight():
#					print('right');
					p.setLeft(v.getRight());
				else:
#					print('left');
					p.setLeft(v.getLeft());
				#parent
				if p.getLeft():
					p.getLeft().parent = p;
			elif p.getRight() == v:
#				print('right');
				if v.getRight():
#					print('right');
					p.setRight(v.getRight());
				else:
#					print('left');
					p.setRight(v.getLeft());
				#parent
				if p.getRight():
					p.getRight().parent = p;
			else:
				print('something strange happened');
		else: #v is the root node
			print('root case');
			if v.getRight(): # case 2
				self.radice = v.getRight();
			else: # case 1 or case 2
				self.radice = v.getLeft();
			#parent
			if self.radice:
				self.radice.parent = None;
#		self.draw();
# pseudo code forgot it but i need it in AVL tree
		return p;

	def delete(self, key):
		print(f'delete({key})');
		v = self.search(key);
		print(f'searched({key}).key = {v.key}');
		if v:
			if not v.getLeft() or not v.getRight(): #case 1 or 2
				print('case 1 or 2');
				#why here no parent is checked?
				ret = self.deleteNode(v);
			else:	#case 3
				print('case 3');
				u = self.predecessor(v);
				v.key = u.key;
				v.data = u.data;
				ret = self.deleteNode(u);
# pseudo code forgot it but i need it in AVL tree
		return ret;

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
