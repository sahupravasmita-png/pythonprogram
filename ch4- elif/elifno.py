print("enter a number")
n=int(input())
if n<=0:
	n=-n
if n<=10:
	print("single digit")
elif n<=100:
	print("double digit")
elif n<=1000:
	print("third digit")
else:
	print("other digit")
