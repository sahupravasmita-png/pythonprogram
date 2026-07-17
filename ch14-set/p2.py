#symmetric diff is opposite of intersection(it remove same elemts from both and print other elements)
s1={3,5,7,8}
s2={7,8,6,4}
print(s1^s2)
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
print(s2)