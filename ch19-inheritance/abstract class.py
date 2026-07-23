#shape abstract class    2 abstract method   area  perimeter 
#rectangle child class
#sqaure child class
from abc import ABC ,abstractmethod
class shape(ABC):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def perimeter(self):
		pass
class rectangle(shape):
	def area(self,l,b):
		print(l*b)
	def perimeter(self,l,b):
		print(2*(l+b))
class sqaure(shape):
	def area(self,a):
		print(a*a)
	def perimeter(self,a):
		print(4*a)
rectangle=rectangle()
rectangle.area(2,3)
rectangle.perimeter(2,4)
sqaure=sqaure()
sqaure.area(3)
sqaure.perimeter(2)




 		
 		