#array is actually a list 
#array similar type of data types but list can contain diff data types 
from array import array
arr=array('i',[1,2,3,4,5,6,7])   # i for integer 
#arr=array('i',[1.5,2,3,4,5,6,7]) #error
print(arr)
arr.append(8)
print(arr)
print(arr[2])  #access element
