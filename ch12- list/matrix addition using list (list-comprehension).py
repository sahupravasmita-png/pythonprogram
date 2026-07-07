#matrix addition using list (list-comprehension method)only when length of two list same 
A=[[1,2,3],[4,5,6]]
B=[[2,3,4],[1,5,2]]
c=[[A[i][j]+B[i][j]for j in range(0,len(A[i]),1)]for i in range(0,len(A),1)]
print(c)