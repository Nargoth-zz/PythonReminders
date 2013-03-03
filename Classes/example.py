#This is a new-type class, inheriting from object
class Animal(object):
	def __init__(self, name):
		self.name = name
		
zebra = Animal("Jeffrey")
print zebra.name
