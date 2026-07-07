#upper trangle 
A=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(A),1):
	for j in range(0,len(A),1):
		if i<=j:
			print(A[i][j],end="\t")
		else:
			print(" ")
	print()