print("enter a number")
a=int(input())
if a%35==0:
	print("divisible by 5 and 7")
elif a%5==0:
	print("divisible only by 5")
elif a%7==0:
	print("divisible only by 7")
else:
	print("not divisible by 5 and 7")