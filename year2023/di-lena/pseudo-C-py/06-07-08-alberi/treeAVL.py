import treeABR;

class treeAVL(treeABR.treeABR):
	def __init__(self, name=''):
		self.name = name;
		self.radice = None;

#rotazioni
	def rotateDX(self, u):
		print(f'rotateDX({u.key})');
		if u and u.getLeft():
			v = u.getLeft();
			v.parent = u.parent;
			u.parent = v;
			u.setLeft(v.getRight());
			v.setRight(u);
			if not v.parent: #v is the new root
				self.radice = v;
			else:
				if v.parent.getLeft() == u:
					v.parent.setLeft(v);
				else:
					v.parent.setRight(v);

	def rotateSX(self, u): #simmetrico a DX
		print(f'rotateSX({u.key})');
		if u and u.getRight():
			v = u.getRight();
			v.parent = u.parent;
			u.parent = v;
			u.setRight(v.getLeft());
			v.setLeft(u);
			if not v.parent: #v is the new root
				self.radice = v;
			else:
				if v.parent.getRight() == u:
					v.parent.setRight(v);
				else:
					v.parent.setLeft(v);

#bilanciamento
	def balance(self, node):
		print(f'balance({node.key})');
		betha = node.betha()
		if node and abs(betha) == 2:
			if betha == 2:
				if node.getLeft().betha() == -1:
					self.rotateSX(node.getLeft());
				self.rotateDX(node);
			else:
				if node.getRight().betha() == 1:
					self.rotateDX(node.getRight());
				self.rotateSX(node);

#dizionario
	def insert(self, key, data=None):
		print(f'\ninsert({key}, {data})');
		v = super().insert(key, data);
		p = v.parent;
		while p:
			if abs(p.betha()) == 2:
				break;
			p.updateHeight();
			p = p.parent;
		if p:
			self.balance(p);
		return (key, data); #i don't understand why i have to return infos

	def delete(self, key):
		p = super().delete(key);
		while p:
			if abs(p.betha()) == 2:
				self.balance(p);
			else:
				p.updateHeight();
			p = p.parent;
	
	#search is not modified from ABR, then it is inherited

#stampa
	def print(self):
		print(f'{self.name} AVL {self}');
