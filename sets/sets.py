# # fruits = {"apple", "banana", "orange", "apple"}
# # print(fruits)

# # my_set = {1, 2, 3}
# # print(my_set, type(my_set))

# # another_set = set([1, 2, 2, 3, 4])
# # print(another_set)

# # for i in my_set:
# #     print(i)

# my_set = {1, 2}
# my_set.add(3)
# print(my_set)
# my_set.update([4, 5])
# print(my_set)

# my_set.remove(5)
# print(my_set)
# my_set.discard(6)
# my_set.pop()
# print(my_set)


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b) 
# print(a.union(b))

# # Intersection
# print(a & b)
# print(a.intersection(b))

# print(a - b)
# print(b-a)

# print(a ^ b)

# a = {1, 2}
# b = {1, 2, 3, 4}
# print(len(a))
# print(a.issubset(b))
# print(b.issuperset(a))

# print(a.isdisjoint(b))
# print(b.isdisjoint(a))

fset = frozenset([1, 2, 3])
print(fset, type(fset))
fset.add(4)