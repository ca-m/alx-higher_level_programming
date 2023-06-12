#!/usr/bin/python3
"""defines base geometry class BaseGeometry"""


class BaseGeometry:
	"""represent base geometry"""

	def area(self):
		"""not yet implemented"""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""validate parameter as integer

		Args:
			name (str): name of the parameter
			value (int): parameter to validate
		Raises:
			TypeError: if value is not an integer
			ValueError: if value is <= 0
		"""
		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
