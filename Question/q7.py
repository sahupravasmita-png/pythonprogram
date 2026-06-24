#wap take two no from keyboard enter your choice 1.add 2.sub 3.mult other invalid choice  using elif
no1=int(input("enter first no"))
no2=int(input("enter another no"))
print("enter your choice\n1.add\n2.sub\n3.mult")
ch=int(input())
if ch==1:
	print("result=",no1+no2)
elif ch==2:
	print("result=",no1-no2)
elif ch==3:
	print("result=",no1*no2)
else:
	print("invalid choice")