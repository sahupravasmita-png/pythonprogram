class student:
	def __init__(self,name,roll,mark):
		self.__name=name 
		self.__roll=roll  
		self.__mark=mark 
	#getter 
	@property
	def name(self):
		return self.__name 
	@property
	def roll(self):
		return self.__roll 
	@property
	def mark(self):
		return self.__mark
	#setter 
	@name.setter 
	def name(self,name):
		self.__name=name 
	@roll.setter 
	def roll(self,roll):
		self.__roll=roll 
	@mark.setter
	def mark(self,mark):
		self.__mark=mark 
#object
s=student("muna",1,90)

print("name=",s.name)
print("roll=",s.roll)
print("mark=",s.mark)


#update value
s.name="muna das"
s.roll=2
s.mark=95

print("\nAfter update")

print("name=",s.name)
print("roll=",s.roll)
print("mark=",s.mark)

		
	