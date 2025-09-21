fruits = ["apple", "banana", "mango","guava", "grapes", "jackfruit"]

# for fruit in fruits:
#     print(fruit)


# using enumerate
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# print(matrix[0][0])
# print(matrix[1][1])

# for row in matrix:
#     # print(row)
#     for num in row:
#         print(num, end=" ")

# squares of 1 to 5
square = []
for i in range(1,6):
    square.append(i**2)
# print(square)

# square = [i**2  for i in range(1,6)]
# print("After applying list comprehension:- ", square)

# even = [ x for x in range(1, 11) if x%2==0]
# print(even)

for row in matrix:
    # print(row)
    for num in row:
        print(num, end=" ")

num = [num for row in matrix for num in row]
print(num)