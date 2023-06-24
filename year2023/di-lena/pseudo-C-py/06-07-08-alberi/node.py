import nodePlain;

class node(nodePlain.nodePlain):
	def __init__(self, key, data=None):
		super().__init__(key, data);
		self.childrens = [];

	def addChild(self, key, data=None):
		new = node(key, data);
		new.parent = self;
		self.childrens.append(new);
		return new;
