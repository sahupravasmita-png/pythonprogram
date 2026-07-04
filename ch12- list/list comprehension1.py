#using list comprehension show nos greater than 5and also even 
L=[3,6,8,9,2,1,7]
L1=[i for i in L if i>5 and i%2==0]
print(L1)