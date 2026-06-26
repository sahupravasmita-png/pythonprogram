#using ternary operator find salary
print("enter basic salary")
sal=float(input())
da=sal*0.4 if sal>=5000 else sal*0.3
hra=sal*0.3 if sal>=5000 else sal*0.2
totalsal=sal+da+hra
print("sal=",sal)
print("da=",da)
print("hra=",hra)
print("totalsalary=",totalsal)