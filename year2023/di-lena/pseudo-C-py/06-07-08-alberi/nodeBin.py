import nodePlain;

class nodeBin(nodePlain.nodePlain):
	def __init__(self, key, data=None):
		super().__init__(key, data);
		self.childrens = [None, None];

	def addChild(self, where, key, data=None):
		new = nodeBin(key, data);
		new.parent = self;
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
		self.childrens[0] = node;
	def setRight(self, node):
		self.childrens[1] = node;

# AdelsonVelskyLandis (AVL) modifications to ABR
	def updateHeight(self): #cost O(1)
#		print(f'updateHeight({self.key}), before = {self.height}, ', end='');
		# if self:
		nh = lh = rh = 1;
		if self.getLeft():
			lh = self.getLeft().height;
		if self.getRight():
			rh = self.getRight().height;
		if self.getLeft() or self.getRight():
			nh = max(lh, rh) +1;
		self.height = nh;
#		print(f'after = {self.height}');

	def betha(self): #cost O(1)
		lh = rh = 0;
		if self.getLeft():
			lh = self.getLeft().height;
		if self.getRight():
			rh = self.getRight().height;
		return lh - rh;
