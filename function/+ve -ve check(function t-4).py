#check +ve -ve number using function return value with argument
def check(no):
	if no>=0:
		print("+ve")
	else:
		print("-ve")
	return no
no=int(input("enter a no"))
res=check(no)
print("res=",res)