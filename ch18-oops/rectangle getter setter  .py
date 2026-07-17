class rectangle:
	def __init__(self,length,breadth):
		self.__length=length 
		self.__breadth=breadth  
	#getter 
	@property
	def length(self):
		return self.__length
	@property
	def breadth(self):
		return self.__breadth
	#setter 
	@length.setter 
	def length(self,length):
		self.__length=length 
	@breadth.setter 
	def breadth(self,breadth):
		self.__breadth=breadth
	#area 
	def area(self):
		return self.__length*self.__breadth
	#perimeter 
	def perimeter(self):
		return 2*(self.__length+self.__breadth)
s=rectangle(5,2)
print("length=",s.length)
print("breadth=",s.breadth)
print("area=",s.area())
print("perimeter=",s.perimeter())

		
	