#upper trangle using list comprehnsion 

A=[[1,2,3],[4,5,6],[7,8,9]]
L=[[A[i][j]for j in range(0,len(A),1)if i<=j]for i in range(0,len(A),1)]
print(L)