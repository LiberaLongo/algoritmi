import treePlain;
import nodeBin;

class treeBin(treePlain.treePlain):
	def __init__(self, key, data=None, name=''):
		self.name = name;
		self.radice = nodeBin.nodeBin(key, data);

	def insert(self, parent, where, key, data=None):
		return parent.addChild(where, key, data);

	def print(self):
		print(f'{self.name} binary {self}');
