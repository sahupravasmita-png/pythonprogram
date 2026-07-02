#find the smallest elemt in a list 
L=[5,17,3,6,9,4,8]
small=L[0]
for i in range(1,len(L),1):
	if small>L[i]:
		small=L[i]
print("small element=",small)


