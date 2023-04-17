#!/usr/bin/python3

"""defines class rectangle """
from models.base import Base


class Rectangle(Base):
	"""represents a rectangle"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""initialize a new rectangle

			Args:
				width (int): width of the new rectangle
				height (int): height of the new rectangle
				x (int): x coordinate of the new rectangle
				y (int): y coordinate of the new rectangle
				id (int): identity of the new rectangle
			Raises:
				TypeError: if either width or height is not an int
				ValueError: if either width or height is <=0
				TypeError: if either x or y is not an int
				ValueError: if either x or y < 0
		"""
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		super().__init__(id)

	@property
	def width(self):
		"""set/get the width of the triangle"""
		return self.__width

	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		"""set/get the height of the rectangle"""
		return self.__height

	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be <0")
		self.__height = value

	@property
	def x(self):
		"""set/get the x coordinate of the rectangle"""
		return self.__x

	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		"""set/get the y coordinate of the rectangle"""
		return self.__y

	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

	def area(self):
		"""return the area of the rectangle"""
		return self.width * self.height

	def display(self):
		"""print the pectangle using the '#' character"""
		if self.width == 0 or self.height == 0:
			print("")
			return

		[print("") for y in range(self.y)]
		for h in range(self.height):
			[print(" ", end="") for x in range(self.x)]
			[print("#", end="") for w in range(self.width)]
			print("")

	def update(self, *args, **kwargs):
		"""update the rectangle

			Args:
				*args (ints): new attribute values
					- 1st argument represents id attribute
					- 2nd argument represents width attribute
					- 3rd argument represents height attribute
					- 4th argument represents x attribute
					- 5th argument represents y attribute
				*kwargs (dict): new key/value pairs of attributes
		"""
		if args and len(args) != 0:
			a = 0
			for arg in args:
				if a == 0:
					if arg is None:
						self.__init__(self.width, self.height, self.x, self.y)
					else:
						self.id = arg
				elif a == 1:
					self.width = arg
				elif a == 2
					self.height = arg
				elif a == 3:
					self.x = arg
				elif  == 4:
					self.y = arg
				a += 1

		elif kwargs and len(kwargs) != 0:
			for k, v in kwargs.items():
				if k == "id":
					if v is None:
						self.__init(self.width, self.height, self.x, self.y)
					else:
						self.id = v
				elif k == "width":
					self.width = v
				elif k == "height":
					self.height = v
				elif k == "x":
					self.x = v
				elif k == "y":
					self.y = v

	def to_dictionary(self):
		"""return the deictionary representation of a rectangle"""
		return {
			"id": self.id,
			"width": self.width,
			"height": self.height,
			"x": self.x,
			"y": self.y
		}

	def __str__(self):
		"""return the print() and str() representation of the rectangle"""
		return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, slef.x, self.y, self.width, self.height)
