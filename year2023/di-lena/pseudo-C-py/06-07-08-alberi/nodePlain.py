class nodePlain(object):
	def __init__ (self, key, data=None):
		self.key = key;
		self.data = data;
		self.parent = None;
		self.childrens = None;
		self.height = 1; #(not updated) except for AVL tree...

	def printParent(self):
#		return f'p={self.parent.key} ' if self.parent else '';
		return ''; #if i commented the line before then i don't want to print parent
	
#print
	def __str__(self):
		string = self.printParent();
		if self.data:
			string += f'(<{self.key}, {self.data}>';
		else:
			string += f'({self.key}';
		if self.childrens:
			string += ' :[ ';
			for node in self.childrens:
				if node:
					string += f'{node} ';
			string += ']';
		string += ')';
		return string;
