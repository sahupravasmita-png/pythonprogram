#wap to sum of even and odd of 1st 10th natural number
i=1
ev=0
od=0
while i<=10:
	if i%2==0:
		ev=ev+i
	else:
		od=od+i 
	i=i+1 
print("sum of even number=",ev)
print("sum of odd number=",od)