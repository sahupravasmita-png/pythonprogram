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
d.update()
d1.update()
d2.update()
d.show()
d1.show()
d2.show()