#!/usr/bin/python3

"""contains read_file function"""


def read_file(filename=""):
	"""Print the contents of a UTF8 text file to stdout."""
	with open(filename, "r", encoding="utf-8") as f:
		print(f.read(), end="")
