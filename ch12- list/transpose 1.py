A=[[1,2,3],[4,5,6]]
B=[]
for i in range(0,len(A[0]),1):
	x=[]
	for j in range(0,len(A),1):
		x.append(A[j][i])
	B.append(x)
print(B)
#v good