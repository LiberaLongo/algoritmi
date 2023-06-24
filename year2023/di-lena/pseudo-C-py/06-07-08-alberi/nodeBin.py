import nodePlain;

class nodeBin(nodePlain.nodePlain):
	def __init__(self, key, data=None):
		super().__init__(key, data);
		self.childrens = [None, None];

	def addChild(self, where, key, data=None):
		new = nodeBin(key, data);
		if where:
			self.setLeft(new);
		else:
			self.setRight(new);
		return new;

	def getLeft(self):
		return self.childrens[0];
	def getRight(self):
		return self.childrens[1];

	def setLeft(self, node):
		if node:
			node.parent = self;
			self.childrens[0] = node;
	def setRight(self, node):
		if node:
			node.parent = self;
			self.childrens[1] = node;
