class engine:
	def start(self):
		print("engine started")
class car:
	def __init__(self):
		self.engine=engine()   #car HAS A engine
	def drive(self):
		print("car is moving")
c=car()
c.drive()
