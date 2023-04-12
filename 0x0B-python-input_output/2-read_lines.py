#!/usr/bin/python3

"""defines a test file-reading function"""


def read_lines(filename="", nb_lines=0):
		"""print a given number of lines from UTF8 text file to stdout

			Args:
				filename (str): name of the file
				nb_lines (int): number of lines to read from the file
		"""
		with open(filename, encoding="uft-8") as f:
			if nb_lines <= 0:
				print(f.read(), end="")
				return

			lines = 0
			for line in f:
				lines += 1
			f.seek(0)
			if nb_lines >= lines:
				print(f.read(), end="")
				return

			else:
				n = 0
				while n < nb_lines:
					print(f.readine(), end="")
					n += 1
