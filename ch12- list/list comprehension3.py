L=[3,6,8,9,2,1,7]
L1=[i+3 if i%2==0 else i-2 for i in L if i>5]
print(L1)