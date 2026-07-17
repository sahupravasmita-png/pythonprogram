class A:
	def __init__(self):
		self.a=10  #public
		self.__b=20  #private
	def look(self):
		return self.__b
ob=A() 
print(ob.a)
# print(ob.__b)  error
print(ob.look())
