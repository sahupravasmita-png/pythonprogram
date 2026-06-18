import sys
print("enter lower char")
ch=input()
if len(ch)!=1:
	print("single char")
	sys.exit()
if ch>="a" and ch<="z":
	x=ord(ch)-32
	print(chr(x))
