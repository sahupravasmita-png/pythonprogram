#find simple interest using function return value with argument
def sical(si):
	si=p*r*t/100
	return si
p=int(input("enter principal amount"))
r=int(input("enter rate of interset"))
t=int(input("enter time"))
si=p*r*t/100
res=sical(si)
print("simple interset=",res)