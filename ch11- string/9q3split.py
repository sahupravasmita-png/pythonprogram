s="ram is a good boy"
L=s.split() #split acc to space 
print(L)
s1="#".join(L)
print(s1)
#reverse the string looping
for i in range(len(s)-1,-1,-1):
	print(s[i],end="")
#reverse using slicing
s1=s[::-1]
print(s1)