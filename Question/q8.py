 #wap take two no from keyboard enter your choice 1.add 2.sub 3.mult other invalid choice  using match case
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
print("enter your choice\n1.add\n2.sub\n3.mult")
ch=int(input())
match ch:
    case 1:print("result=",a+b)
    case 2:print("result=",a-b)
    case 3:print("result=",a*b)
    case _:print("invalid choice")