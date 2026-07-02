#check even&odd using fuction return value with no argument
def check():
	print("enter a number")
	no=int(input())
	if no%2==0:
		print("even")
	else:
		print("odd")
	return no
res=check()
