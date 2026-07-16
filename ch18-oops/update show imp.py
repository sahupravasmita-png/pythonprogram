class demo:
	c=0
	def __init__(self):
		demo.c=1   
		self.a=1
	def update(self):
		demo.c=demo.c+1 
		self.a=self.a+1
	def show(self):
		print(self.a,demo.c)
d=demo()   #jetiki ob setiki a create heba
d1=demo()
d2=demo()
d.show()
d1.show()
d2.show()
d.update(3)
d1.update(5)
d2.update(7)
d.show()
d1.show()
d2.show()