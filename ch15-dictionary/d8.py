#3 students roll no & name display it using dict 
d={}
print("enter how many student data store")
s=int(input())
for i in range(s):
	print("enter student",(i+1),"rollno and name")
	r=int(input())
	n=input()
	d[r]=n
print(d)


