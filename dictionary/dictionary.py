student = {
    "name":"Ankit",
    "age": 21,
    "city":"Mumbai",
    "country":"India"
}

print(student, type(student))

print(student["name"])
print(student["country"])
print(student.get("age"))
print(student.get("marks"))

student["age"] = 22
print(student)

student["college"] = "IIT"
print(student)

# student.pop("age")  
# print(student)       # removes key 'age'
# del student["name"]        # deletes 'name'
# print(student)      

# student.clear()   
# print(student)     

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(value)