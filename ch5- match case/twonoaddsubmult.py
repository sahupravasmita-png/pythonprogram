print("enter two number")
no1=int(input("enter 1st number"))
no2=int(input("enter 2nd number"))
print("enter your choice\n1.add\n2.sub\n3.mult")
choice=int(input())
match choice:
    case 1:print("add=",no1+no2)
    case 2:print("sub=",no1-no2)
    case 3:print("mult=",no1*no2)