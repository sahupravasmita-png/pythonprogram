print("enter basic salary")
sal=float(input())
da=sal*0.3 if sal>=4000 else sal*0.2
hra=sal*0.2 if sal>=4000 else sal*0.1
totalsal=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("totalsal=",totalsal)