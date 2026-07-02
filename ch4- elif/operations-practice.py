no1=int(input("enter 1st number"))
no2=int(input("enter 2nd number"))
print("enter an operator(+,-,*,//:)")
op=input("operator:")
if op=="+":
	print("result=",no1+no2)
elif op=="-":
	 print("result=",no1-no2)
elif op=="*":
	print("result=",no1*no2)
elif op=="//":
	if no2!=0:
		print("result=",no1//no2)
	else:
		print("division by zero not allowed")
else:
	print("invalid operator")