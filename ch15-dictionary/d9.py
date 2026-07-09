# Nested Dictionary
d = {}
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nstudent",i + 1)
    rollno = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    mark=float(input("mark:"))
    d[rollno] = {
        "name": name,
        "age": age,
        "mark":mark
    }

print("\nnested dictionary")
print(d)