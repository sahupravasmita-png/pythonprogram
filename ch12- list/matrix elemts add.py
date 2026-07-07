#matrix addition using list only when length of two list same 
A=[[1,2,3],[4,5,6]]
B=[[2,3,4],[1,5,2]]
c=[]
for i in range(0,len(A),1):
	x=[]
	for j in range(0,len(A[i]),1):
		x.append(A[i][j]+B[i][j])
	c.append(x)
print(c)