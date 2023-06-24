import nodeBin;

class nodeAVL(nodeBin.nodeBin):
	def __init__(self, key, data=None):
		super().__init__(key, data);
		self.height = 0;

# AdelsonVelskyLandis modifications to ABR
	def updateHeight(self, node): #cost O(1)
		if node:
			nh = lh = rh = 0;
			if node.getLeft():
				lh = node.getLeft().height;
			if node.getRight():
				rh = node.getRight().height;
			if node.getLeft() or node.getRight():
				nh = max(lh, rh) +1;
			node.height = nh;

	def betha(self): #cost O(1)
		lh = rh = 0;
		if node.getLeft():
			lh = node.getLeft().height;
		if node.getRight():
			rh = node.getRight().height;
		return lh - rh;
