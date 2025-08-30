# 1. Creating Arrays (Lists in Python)
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

print("Arrays (Lists) in Python:")
print("Numbers:", numbers)
print("Fruits:", fruits)

# 2. Accessing Elements
print("\nAccessing Elements:")
print("First number:", numbers[0])
print("Last fruit:", fruits[-1])

# 3. Modifying Elements
numbers[2] = 35
print("\nModified Numbers:", numbers)

# 4. Adding Elements
numbers.append(60)
fruits.insert(1, "orange")
print("\nAfter Adding Elements:")
print("Numbers:", numbers)
print("Fruits:", fruits)

# 5. Removing Elements
numbers.remove(20)
removed_fruit = fruits.pop()
print("\nAfter Removing Elements:")
print("Numbers:", numbers)
print("Removed fruit:", removed_fruit)
print("Fruits:", fruits)

# 6. Slicing Arrays
print("\nSlicing Arrays:")
print("First three numbers:", numbers[:3])
print("Fruits except first:", fruits[1:])

# 7. Looping Through Arrays
print("\nLooping Through Arrays:")
for num in numbers:
    print(num, end=" ")
print()
for fruit in fruits:
    print(fruit, end=" ")
print()

# 8. Array Length
print("\nArray Lengths:")
print("Numbers length:", len(numbers))
print("Fruits length:", len(fruits))

# 9. Sorting and Reversing
numbers.sort()
fruits.reverse()
print("\nSorted Numbers:", numbers)
print("Reversed Fruits:", fruits)

# 10. Nested Arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nNested Arrays (Matrix):")
for row in matrix:
    print(row)
