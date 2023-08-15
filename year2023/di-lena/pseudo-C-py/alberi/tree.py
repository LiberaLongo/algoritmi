import treePlain;
import node;

class tree(treePlain.treePlain):
	def __init__(self, key=None, data=None, name=''):
		self.name = name;
		self.radice = node.node(key, data);

	def insert(self, parent, key, data=None):
		return parent.addChild(key, data);

	def print(self):
		print(f'{self.name} {self}');
