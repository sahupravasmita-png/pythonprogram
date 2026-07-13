#matrix using array
from array import array
r=int(input("enter rows:"))
c=int(input("enter columns:"))
matrix=[]
for i in range(r):
	row=array('i')
	for j in range(c):
		x=int(input(f"enter element [{i}][{j}]:"))
		row.append(x)
	matrix.append(row)
print("\nmatrix")
for row in matrix:
	print(*row)