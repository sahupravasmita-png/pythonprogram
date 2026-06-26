#find area of square& rectangle using elif
print("choose a shape to find area")
print("1.sqaure")
print("2.rectangle")
print("enter your choice(1-2)to find area")
choice=int(input())
if choice==1:
	side=int(input("enter side of sqaure"))
	area=side*side
	print("area of sqaure=",area)
elif choice==2:
	length=int(input("enter length of a rectangle"))
	breadth=int(input("enter breadth of a rectangle"))
	area=length*breadth
	print("area of rectangle=",area)
else:
	print("invalid choice")