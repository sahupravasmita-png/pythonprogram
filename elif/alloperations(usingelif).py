print("enter two numbers")
no1=int(input("first number:"))
no2=int(input("second number:"))
print("\n enter an operator(+,-,*,//:)")
op=input("operator:")
if op=="+":
	print("result=",no1+no1)
elif op=="-":
	print("result=",no1-no2)
elif op=="*":
	print("result=",no1*no2)
elif op=="//":
	if no2!=0:
		print("result=",no1//no2)
	else:
		print("division by zero is not allowed")
else:
	print("invalid operator")