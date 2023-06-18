#!/usr/bin/env python3

# queue in pthon from geeksforgeeks...
# https://www.geeksforgeeks.org/queue-in-python/

# three possible implementation are given...
# then we choose one and if we want to change we change this file only!

from collections import deque;

class queue:
	def __init__(self):
		self.q = deque();

	def enqueue(self, elem):
		self.q.append(elem);
	
	def dequeue(self):
		return self.q.popleft();

	def isEmpty(self):
		return len(self.q) == 0;
