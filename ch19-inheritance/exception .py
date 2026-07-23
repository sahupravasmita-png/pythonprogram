#exceptional handling
print("a")
try:
	print("try start")
	print(10//0)    #here exception occur so end try block not showing
	print("end try block")
except:     #base exception   other u can use exception name like zero exception error
	print("exception handle")
print("end program")