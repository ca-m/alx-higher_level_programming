#!/usr/bin/python3

"""contains function append after """


def append_after(filename="", serch_string="", new_string=""):
	"""appends new string after line containing search_string in filename"""
	with open(filename, 'r', encoding='utf-8') as f:
	line_list = []
	while True:
		line = f.readline()
		if line == "":
			break
		line_list.append(line)
		if search_string in line:
			line_list.append(new_string)
	with open(filename, 'w', encoding='utf-8') as f:
		f.writelines(line_list)
