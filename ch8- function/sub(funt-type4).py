#sub using function return value with argument
def sub(no1,no2):
	s=no1-no2
	return s
no1=int(input("enter a no"))
no2=int(input("enter another no"))
res=sub(no1,no2)
print("res=",res)