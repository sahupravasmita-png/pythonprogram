#find the biggest elemt in a list 
L=[5,17,3,6,9,4,8]
big=L[0]
for i in range(1,len(L),1):
	if big<L[i]:
		big=L[i]
print("big element=",big)