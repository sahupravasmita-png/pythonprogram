#wap to separate even and odd elemts in a list to two diffrent list use range method
L=[2,4,6,7,8,5,9]
ev,od=[],[]
for i in range(0,len(L),1) :
	if L[i]%2==0:
		ev.append(L[i])
	else:
		od.append(L[i])
print("list of even=",ev)
print("list of odd=",od)