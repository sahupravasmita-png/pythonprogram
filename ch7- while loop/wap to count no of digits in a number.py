#wap to count no of digits in a number
n=int(input("enter a number"))
c=0
while n!=0:
	n=n//10
	c=c+1
print("no of digits=",c)
