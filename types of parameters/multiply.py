def multiply(*args):
	result=1
	for no in args:
		result *=no
	return result
# Calling with a varying number of arguments
print(multiply(2,3))
print(multiply(2,3,2))
print(multiply(6,8,9,6))