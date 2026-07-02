n=int(input("enter a number"))
ec=0
oc=0
while n!=0:
     r=n%10
     if r%2==0:
          ec=ec+1 
     else:
          oc=oc+1
     n=n//10
print("no of even digit=",ec)
print("no of odd digit=",oc)