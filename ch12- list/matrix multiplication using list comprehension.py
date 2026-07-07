#matrix multiplication using list comprehension
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,5,7],[2,4,3],[1,9,7]]
C=[[sum(A[i][k]*B[k][j]for k in range(0,len(B),1))for j in range(0,len(B[i]),1)]for i in range(0,len(A),1)]
print(C)