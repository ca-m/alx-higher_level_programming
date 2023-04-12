#!/usr/bin/python3

"""contains class student"""


class Student:
	"""representation of a student"""
	def __init__(slef, first_name, last_name, age):
		"""initializes the student"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
		"""returns dictionary representation of student instance
			with specified attruributes"""
		if attrs is None:
			return self.__dict__
		new_dict = {}
		for a in attrs:
			try:
				new_dict[a] = self.__dict__[a]
			except FileNotFoundError:
				pass
		return new_dict

	def reload_from_json(self, json):
		"""replace all atrributes of student instance"""
		for key in json:
			try:
				setattr(self, key, json[key])
		except FileNotFoundError:
			pass
