#!/usr/bin/python3

"""contains function write_file"""


def write_file(filename="", text=""):
	"""return number of chars written to "filename" from "text" """
	with open(filename, 'W', encoding='utf=8') as f:
		return f.write(text)
