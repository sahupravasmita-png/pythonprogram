#using without list comprehension (range method)
L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[]
for i in range(0,len(L),1):
	x=[]
	for j in range(0,len(L[i]),1):
		x.append(L[i][j])
	L1.append(x)
print(L1)

