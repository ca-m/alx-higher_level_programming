#!/usr/bin/python

"""function that creates object from JSON file """

import json


def load_from_json_file(filename):
	"""crate and object from JSON file"""
	with open(filename, 'r', encoding='utf-8') as f:
		return json.load(f)
