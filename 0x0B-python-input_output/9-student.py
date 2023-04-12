#!/usr/bin/python3

"""contains student class """


class Student:
	"""representation of a student"""
	def __init__(self, first_name, last_name, age):
		"""initializes student"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		"""return dictionary represenation of Student instance"""
		return self.__dict__
