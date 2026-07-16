class test:
	def __init__(self,):
		print("constructor")
	def show(self):
		print("show instance/object method")
	@classmethod
	def look(cls):
		print("class method")
	@staticmethod
	def disp():
		print("static disp method")
test.look()
#test.show(): object required
t=test()
t.show()
test.disp()
