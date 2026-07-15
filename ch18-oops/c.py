#remember that object occupy memory not class 
class A:
	def __init__(self):   #constructor  (intitialize) self is property of object
		print("constructor")
	def show(self):       #method -> manipulation data
		print("show method")
def look():    #function
		print("look function")
ob=A()    #object create #ob object refrence
ob.show() #method call by object reference
ob.show()	
look()

#object once create kari call kari pariba method ku many times,
