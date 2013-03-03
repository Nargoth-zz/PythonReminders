#This is a new-type class, inheriting from object
class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	health = "good"
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def description(self):
		print self.name
		print self.age
		
hippo = Animal("Jack", 24)
hippo.description()

sloth = Animal("Dieter", 35)
ocelot = Animal("Klaus", 93)

print hippo.health
print sloth.health
print ocelot.health
