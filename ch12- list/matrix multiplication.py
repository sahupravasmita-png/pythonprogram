#matrix multiplication 
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,5,7],[2,4,3],[1,9,7]]
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(A),1):
	for j in range(0,len(B[i]),1):
		for k in range(0,len(B),1):
			C[i][j]+=A[i][k]*B[k][j]
print(C)