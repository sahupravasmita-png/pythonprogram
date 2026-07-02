#wap for sum of even and sum of odd elemts in a list using index concept
L=[2,4,5,3]
se,so=0,0
for i in L :
	if i%2==0:
		se=se+i
	else:
		so=so+i
print("sum of even=",se)
print("sum of odd=",so)