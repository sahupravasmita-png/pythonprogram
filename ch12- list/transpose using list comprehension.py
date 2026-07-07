#transpose of a matrix using list comprehension
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[A[j][i]for j in range(0,len(A[i]),1)]for i in range(0,len(A),1)]
print(B)