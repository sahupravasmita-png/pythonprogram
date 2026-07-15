#wap to count no of even and odd elemts in a list
L=[2,4,6,7,8,5,9]
ev,od=0,0
for i in L :
	if i%2==0:
		ev=ev+1
	else:
		od=od+1
print("no of even=",ev)
print("no of odd=",od)