import math
print("choose a shape to find area:")
print("1.sqaure")
print("2.rectangle")
print("3.circle")
choice=int(input("enter choice (1-3):"))
if choice==1:
	side=float(input("enter the side of sqaure:"))
	area=side*side
	print("area of sqaure=",area)
elif choice==2:
	length=float(input("enter the length of rectangle:"))
	breadth=float(input("enter the breadth of rectangle:"))
	area=length*breadth
	print("area of rectangle=",area)
elif choice==3:
	radius=float(input("enter radius of circle:"))
	area=math.pi*radius*radius
	print("area of circle=",area)
else:
	print("invalid choice")