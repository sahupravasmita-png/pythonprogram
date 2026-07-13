class rectangle:
	def __init__(self,L,B):
		self.L=L  
		self.B=B  
	def show(self):
		print("length=",self.L)
		print("breadth=",self.B)
	def area(self):
		return self.L*self.B
	def perimeter(self):
		print("perimeter of rectangle=",2*(self.L+self.B))
r1=rectangle(4,5)
r1.show()
print("area of rectangle=",r1.area())
r1.perimeter()