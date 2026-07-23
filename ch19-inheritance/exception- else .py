L=[10,5,7,6]
try:
	print(L[2]/2)  #exception happening here
except:
	print("exception handle")
else:
	print("no exception occurred") #it comes only when exception not happen inside the try block
finally:  #finally not handel exceptions
	print("must excute")
print("program end")
