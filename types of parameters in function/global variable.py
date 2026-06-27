a=10 #global
def show():
	a=30 #local
	print("local ",a)
def disp():
	print(a)#global variable will prints
	print("hi")
show()
disp()
print(a)
