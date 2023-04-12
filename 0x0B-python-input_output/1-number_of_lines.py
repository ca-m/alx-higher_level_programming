#!/usr/bin/python3

"""defines text file line-counting function"""


def number_of_lines(filename=""):
	"""return number of lines in a text file"""
	lines = 0
	with open(filename) as f:
		for line in f:
		lines += 1
	return lines
