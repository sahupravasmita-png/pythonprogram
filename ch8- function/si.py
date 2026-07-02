#find simple interset using function no return value no argument
def sical():
	print("enter principal amount")
	p=int(input())
	print("enter rate of interset")
	r=int(input())
	print("enter time")
	t=int(input())
	si=p*r*t/100
	print("simple interset=",si)
sical()