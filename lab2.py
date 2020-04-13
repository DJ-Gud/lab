import json

class Person():

	def __init__(self, fname=None, sname=None, age=None):

		self.fname = fname 
		self.sname = sname
		self.age = age

	def __eq__(self, other):
		return self.fname == other.fname and \
			   self.sname == other.sname  and \
			   self.age == other.age


	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)

	@classmethod 
	def fromJSON(cls, data):
		return cls(**json.loads(data).copy())



def test_init():
	p = Person('f', 's', 1)

	assert p.fname == 'f' and \
		   p.sname == 's' and \
		   p.age == 1

def test_eq():
	p1 = Person('name1', 'sname1', 20)
	p2 = Person('name1', 'sname1', 20)
	p3 = Person('name2', 'sname1', 20)
 
	assert p1 == p2 and p1 != p3

def test_JSON():
	p1 = Person('name1', 'sname1', 20)

	p2 = Person.fromJSON(p1.toJSON())

	assert p1.__dict__ == p2.__dict__
