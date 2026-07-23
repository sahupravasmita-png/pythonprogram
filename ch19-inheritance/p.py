class subject:
	def __init__(self,p,c,m):
		self.p=p 
		self.c=c 
		self.m=m 
	def show(self):
		print("p=",self.p)
		print("c=",self.c)
		print("m=",self.m)
class student:
	def __init__(self,r,p,c,m):
		self.s1=subject(p,c,m)
		self.roll=r 
	def info(self):
		self.s1.show()
		total=self.s1.p+self.s1.m
		print("total mark , total")
s=student(1,90,80,70)
s.info()
