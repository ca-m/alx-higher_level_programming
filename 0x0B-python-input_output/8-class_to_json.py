#!/usr/bin/python3

"""contains function class_to_json """


def class_to_json(obj):
	"""returns dictionary description with simple data structure
		(list, dictionary, string, integer, boolean)
		 for JSON serialization of object"""
	return obj.__dict__
