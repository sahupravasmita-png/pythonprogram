#person (parent) employee(child) in inheritance also use keyboard input
class P:
	def __init__(age):
		age.x=int(input("enter age"))
	def dispP(age):
		print("age=",age.x)
class E(P):
	def __init__(salary):
		super().__init__()
		salary.y=float(input("enter salary"))
	def dispE(salary):
		print("salary=",salary.y)
ob=E()  
ob.dispP()
ob.dispE()