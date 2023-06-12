#!/usr/bin/python3
"""defines class-checking function."""


def is_same_class(obj, a_class):
	"""check if object is exactly an instance of given class.

	Args:
		obj (any): object to check.
		a_class (type): class to match type of obj to.
	Returns:
		If obj is an exact instance of a_class - True.
		Otherwise - False.
	"""
	if type(obj) == a_class:
		return True
	return False
