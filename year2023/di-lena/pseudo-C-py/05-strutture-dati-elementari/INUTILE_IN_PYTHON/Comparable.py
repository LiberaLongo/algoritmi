#!/usr/bin/env python3

#Comparable type...
# https://betterprogramming.pub/how-to-use-comparable-classes-in-python-a897f9bccf25

from typing import Protocol, TypeVar

T = TypeVar("T")

class Comparable(Protocol[T]):
	def __eq__(self: T, other: T) -> bool:
		"""x == y, equals"""
		pass;

	def __ne__(self: T, other: T) -> bool:
		"""x != y, not equals"""
		pass;

	def __lt__(self: T, other: T) -> bool:
		"""x < y, less than"""
		pass;

	def __gt__(self: T, other: T) -> bool:
		"""x > y, greater than"""
		pass;

	def __le__(self: T, other: T) -> bool:
		"""x <= y, less or equal"""
		pass;

	def __ge__(self: T, other: T) -> bool:
		"""x >= y, greater or equal"""
		pass;

