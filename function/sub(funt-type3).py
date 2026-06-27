#sub using function return value with no argument
def sub():
	s=no1-no2
	return s
no1=int(input("enter a no"))
no2=int(input("enter another no"))
res=sub()
print("res=",res)