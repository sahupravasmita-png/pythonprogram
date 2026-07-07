#using list comprehension show even elements in list
L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[[j for j in i if j%2==0] for i in L]
print(L1)