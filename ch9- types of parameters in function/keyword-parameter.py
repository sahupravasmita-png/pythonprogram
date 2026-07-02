#keyword parameters
#let you pass values to a function by specifying the parameter names, rather than relying on their position.
def show(a=0,b=2,c=0,d=4):
	print(a,b,c,d)
show("hi",1,7,8)
show(d=10,a=5,b=20,c=8)
show(c=30)