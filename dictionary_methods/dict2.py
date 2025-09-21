student = {"name": "Rahul", "age": 21, "course": "B.Sc"}
# print(student.keys())

# print(student.values())

# print(student.items())

print(student.get("name"))
# print(student["roll_no"])
print(student.get("roll_no"))

student.update({"age": 22, "roll_no": 101})
print(student)

# student.pop("roll_no")
# print(student)

# student.popitem()
# print(student)

# student.clear()
# print(student)

del student["age"]
print(student)

del student
print(student)