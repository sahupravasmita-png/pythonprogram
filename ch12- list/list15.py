#wap to separate even and odd elemts in a list to two diffrent list
L=[2,4,6,7,8,5,9]
ev,od=[],[]
for i in L :
	if i%2==0:
		ev.append(i)
	else:
		od.append(i)
print("list of even",ev)
print("list of odd",od)