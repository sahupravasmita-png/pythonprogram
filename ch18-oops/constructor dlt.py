class test:
	def __init__(self,n):  #__init__ (constructor method)and self shows current value 
		self.n=n  #class variable  #we use parameter(n)for put diffrent values
		print("constructor",self.n)
	def __del__(self):
		print("destructor",self.n)
t=test("one")   #1st object
test("two")     #nameless object
t1=test("three")   #2nd object
t2=test("four")    #3rd object
