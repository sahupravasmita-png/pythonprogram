#find no of digit,alphabets,space,special symbol,upper,lower,vowel,consonat
print("enter a string")
s=input()
dig,alp,sp,sy,up,lw,vw,co=0,0,0,0,0,0,0,0
for i in s:
	if i.isdigit():
		dig=dig+1
		if i.isupper():
			up=up+1
		else:
			lw=lw+1
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			co=co+1
	elif i.isalpha():
		alp=alp+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
print("no of digit=",dig)
print("no of uppercase=",up)
print("no of lowercase=",lw)
print("no of vowels=",vw)
print("no of consonant=",co)
print("no of alphabets=",alp)
print("no of space=",sp)
print("no of special symbol=",sy)

