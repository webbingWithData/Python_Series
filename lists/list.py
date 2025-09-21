# # # a = [1,2,3,4,5,6] #numbers
# # # b = ['ankit', 'Adarsh', 'Ayush','Akarshit'] #string

# # # c = [1,'heyy',3.296, True] #mixed list

# # # print(a, type(a))
# # # print(b, type(b))
# # # print(c, type(c))

# # # a = list((4, 2, 3, 'apple', 4.5))  
# # # print(a)

# # fruits = ["apple", "banana", "mango"]

# # # print(fruits[0])
# # # print(fruits[2])
# # # print(fruits[3])

# # # fruits[1] = "grapes"
# # # print(fruits)

# # a = []
# # a.append(10)
# # a.append(13)
# # print(a)

# # a.extend([7, 20, 9])  
# # print("After extending with [7, 20, 9]:- ", a) 

# # a.insert(1,5)
# # print(a)
# # a.remove()
# # print(a)


# fruits = ["apple", "banana", "mango", "grapes", "banana", "grapes"]

# fruits.remove("grapes")
# print(fruits)
# fruits.pop(2) 
# print(fruits)
# fruits.pop()
# print(fruits)
# del fruits[2]
# print(fruits)
# fruits.clear()
# print(fruits)

# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:4])
# print(numbers[0:6:2]) #start:end:step
# print(numbers[0:3])
# print(numbers[:3])
# print(numbers[:])
# print(numbers[:-3])
# print(numbers[-3:])

numbers = [10, 20, 5, 30, 20, 10, 40]

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(20))
print(numbers.count(20))
copy_list = numbers.copy()
print(copy_list)


conc_list = numbers+copy_list+numbers
print(conc_list)
