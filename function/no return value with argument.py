#no return value with argument
def add(no1,no2):
	s=no1+no2
	print("sum=",s)
for i in range(3):
	print("enter a no")
	no1=int(input())
	print("enter another")
	no2=int(input())
	add(no1,no2)
