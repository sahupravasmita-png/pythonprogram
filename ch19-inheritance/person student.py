#person student 
class person:
	def __init__(self):
		self.x=20
	def dispperson(self):
		print(self.x)
class student(person):
	def __init__(self):
		super().__init__()
		self.y=1
	def dispstudent(self):
		print(self.y)
ob=student()
ob.dispperson()
ob.dispstudent()

