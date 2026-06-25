#wap to get first digit of any number
n=int(input("enter a number"))
while n!=0:
	r=n%10
	n=n//10
print(r)