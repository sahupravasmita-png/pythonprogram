#chcek even&odd using function return value with argument
def check(no):
	if no%2==0:
		print("even")
	else:
		print("odd")
	return no
no=int(input("enter a number"))
res=check(no)
print(res)