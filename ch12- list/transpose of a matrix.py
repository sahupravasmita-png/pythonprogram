#transpose of a matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(A),1):
	for j in range(0,len(A[i]),1):
		print(A[j][i],end="\t")
	print()