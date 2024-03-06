class Rectangle:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def set_width(self, width):
		self.width = width
	
	def set_height(self, height):
		self.height = height
	
	def get_area(self):
		return self.width * self.height
	
	def get_perimeter(self):
		return 2 * self.width + 2 * self.height
	
	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** .5
	
	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			i = 0
			s = ""
			while i < self.height:
				o = (self.width - 1) * "*"
				s += f"*{o}\n"
				i += 1
			return s
	
	def get_amount_inside(self, shape):
		return int(self.get_area() / shape.get_area())
	
	def __str__(self):
		return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
	
	def __init__(self, side_length):
		self.width = side_length
		self.height = side_length
	
	def set_side(self, side_length):
		self.width = side_length
		self.height = side_length
	
	def set_width(self, width):
		self.width = width
		self.height = width
	
	def set_height(self, height):
		self.width = height
		self.height = height
		
	def __str__(self):
		return f"Square(side={self.width})"
