import math
class circle:
	def __init__(self,r):
		self.r=r  
	def show(self):
		print("radius=",self.r)
	def area(self):
		return math.pi*self.r*self.r
r1=circle(5)
r1.show()
print("area of circle=",r1.area())
