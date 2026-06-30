#we can only remove left space &right space not the middle space in a string 
s=" ram "
print(len(s)) #to check the length of string
print(len(s.lstrip())) #remove left space
print(len(s.rstrip())) #remove right space
print(len(s.strip())) #remove both side space 