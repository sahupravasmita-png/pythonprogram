#inheritance #we can use already there constructors inside class no means B have A quality also have its own quality
class A:
	def show(self):
		print("show method A")
class B(A):
	def look(self):
		print("look method B")
ob=B()
ob.show()
ob.look()
