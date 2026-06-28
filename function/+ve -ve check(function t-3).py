#check +ve -ve number using function return value with no argument
def check():
	if no>=0:
		print("+ve")
	else:
		print("-ve")
	return no
no=int(input("enter a no"))
res=check() #call the function
print("res=",res)