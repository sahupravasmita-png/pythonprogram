L=[3,6,8,9,2,1,7]
L1=[]
for i in L:
	if i >5:
		if i%2==0:
			L1.append(i+3)
		else:
			L1.append(i-2)
print(L1)