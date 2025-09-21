# # # def greet(name, city="Delhi"):
# # #     print("Hello", name, "from", city)

# # # greet("Ankit","Mumbai")

# # def greet(fname, lname, age):
# #     print("Welcome,", fname, lname, "of ", age)

# # greet("Ankit","Pandey", 21)
# # greet("Ankit", 21)

# def friends(*names):
#     print("My friends are:", names)

# friends("Rohit", "Aman", "Neha")


# def intro(**info):
#     print("Name:", info["name"])
#     print("Age:", info["age"])

# intro(name="Kunal", age=20)

def square(num):
    return num * num

result = square(5)
print("the square of 5 is ", result)
print(100/result)