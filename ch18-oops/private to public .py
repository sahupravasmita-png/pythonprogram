class A:
	def __init__(self):
		self.a=10  #public
		self.__b=20  #private
	def __look(self):  #private method 
		print("look function")
	def show(self):   #here we make a public method to call above p.method
		self.__look()  
ob=A() 
print(ob.a)
# print(ob.__b)  error
#print(ob.look())  error
ob.show()
