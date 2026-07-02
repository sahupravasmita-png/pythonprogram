#addition,sub,mult of 2 no using elif
no1=int(input("enter a number"))
no2=int(input("enter another number"))
print("enter your choice\n1.add\n2.sub\n3.mult")
ch=int(input())
if ch==1:
	print("add=",no1+no2)
elif ch==2:
	print("sub=",no1-no2)
elif ch==3:
	print("mult=",no1*no2)
else:
	print("invalid choice")