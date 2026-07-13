class si:
	def __init__(self,p,r,t):
		self.p=p 
		self.r=r  
		self.t=t  
	def show(self):
		print("principal=",self.p)
		print("rate of interest=",self.r)
		print("time=",self.t)
	def simpleinterest(self):
		return(self.p*self.r*self.t)/100
r1=si(3000,10,5)
r1.show()
print("simple interest=",r1.simpleinterest())