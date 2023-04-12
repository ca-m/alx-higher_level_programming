#!/usr/bin/python3

"""function that writes object to text file"""

import json


def save_to_json_file(my_obj, filename):
	"""object to a textfile using JSON representation"""
	with open(filename, 'w', encoding='utf-8') as f:
		json.dump(my_obj, f)
