#wap for sum of even and sum of odd elemts in a list using range concept
L=[2,4,5,3]
se,so=0,0
for i in range(0,len(L),1):
	if L[i]%2==0:
		se=se+L[i]
	else:
		so=so+L[i]
print("sum of even=",se)
print("sum of odd=",so)