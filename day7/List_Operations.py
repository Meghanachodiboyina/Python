# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# append()
numbers.append(60)
print("After append:", numbers)

# insert()
numbers.insert(2, 25)
print("After insert:", numbers)

# remove()
numbers.remove(40)
print("After remove:", numbers)

# pop()
numbers.pop(2)
print("After pop:", numbers)

# count()
print("Count of 20:", numbers.count(20))

# index()
print("Index of 30:", numbers.index(30))

# extend()
numbers.extend([70, 80])
print("After extend:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# copy()
new_list = numbers.copy()
print("Copied list:", new_list)

# len()
print("Length:", len(numbers))

# max()
print("Maximum:", max(numbers))

# min()
print("Minimum:", min(numbers))

# sum()
print("Sum:", sum(numbers))