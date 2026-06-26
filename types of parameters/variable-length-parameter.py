#A variable-length parameter is a parameter that allows a function to accept any number of arguments.
#arguments is treated as tuple
def show(*a):
	print(a)
show(3,4,6,8)

def show(b,*a):
	print(a,b)
show(3,4,6,8)


def show(a,*b):
	print(a,b)
show(10,12,3,4)