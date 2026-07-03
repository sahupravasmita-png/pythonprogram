#input output
L=[0,0,0,0]
s=0
print("enter",len(L),"elements")
for i in range(len(L)):
	print("enter element",i+1)
	L[i]=int(input())
	s=s+L[i]
	avg=s/4
print("total=",s)
print("average=",avg)