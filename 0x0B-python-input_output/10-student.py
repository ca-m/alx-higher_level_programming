#!/usr/bin/python3

"""defines Student class"""


class Student:
	"""represent a student"""

		def __init__(self, first_name, last_name, age):
			"""initialises new student

				Args:
				first_name (str): first name of the student
				last_name (str): last name of the student
				age (int): age of the student
			"""
			self.first_name = first_name
			self.last_name = last_name
			self.age = age

		def to_json(self, attrs=None):
			"""gets dictionary represenation of student
				if attrs is a list of strings,
				represent only those attributes included in list

				Args:
				attrs (list): (Optional) attributes to represent
			"""
			if (type(attrs) == list and
					all(type(ele) == str for ele in attrs)):
				return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
			return self.__dict__
