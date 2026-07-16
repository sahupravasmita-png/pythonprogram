c=20    #global variable
class test:
	d=70  #class variable ->it comes class under 
	def __init__(self,c): #c is local or formal variable
		#a=10    #local variable
		self.a=10  #instance variable
		self.b=20  #instance variable
	def show(self):
		print(self.a)
		print(self.b)
t=test(5)
t.c=40
t.show()
print(t.__dict__)
t1=test(7)
t1.show()
t1.b=50
print(t1.__dict__)
print(test.__dict__)



