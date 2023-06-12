#!/usr/bin/python3
"""defines inherited list class MyList."""


class MyList(list):
	"""implements sorted printing for built-in list class."""

	def print_sorted(self):
		"""prints list in sorted ascending order."""
		print(sorted(self))
