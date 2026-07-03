L=[]
print("enter how many element store in list ")
size=int(input())
for i in range(0,size,1):
	print("enter element",i+1)
	L.append(eval(input()))
print(L)