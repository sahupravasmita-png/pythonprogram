#add using function return value with argument
def add(no1,no2):
	s=no1+no2
	return s
no1=int(input("enter a number"))
no2=int(input("enter another number"))
res=add(no1,no2)
print("add of two no=",res)