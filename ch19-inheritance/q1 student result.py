#student result
class student:
	def __init__(self):
		self.n=input("enter name of student")
		self.roll=int(input("enter roll no"))
		self.mark1=int(input("enter 1st mark"))
		self.mark2=int(input("enter 2nd mark"))
		self.mark3=int(input("enter 3rd mark"))
	def dispstudent(self):
		print("name=",self.n)
		print("rollno=",self.roll)
		print("mark1=",self.mark1)
		print("mark2=",self.mark2)
		print("mark3=",self.mark3)
	def __init__(self):
		super().__init__()
		self.total=self.mark1+self.mark2+self.mark3
		self.percentage=(self.total/300)*100
		if self.percentage>=80:
			self.grade="A"
		elif self.percentage>=60:
			self.grade="B"
		elif self.percentage>=40:
			self.grade="C"
		else:
			self.fail
	def dispB(self):
		print("total=",self.total)
		print("percentage=",self.percentage)
		print("grade=",self.grade)
n=int(input("enter number of student data to put"))
for i in range(n):
	print("\nenter details of students",i+1)
	ob=B()  
	 ob.dispB() 

