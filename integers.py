# 1. Integer Declaration
a = 10
b = -5
c = 0
large_int = 12345678901234567890  # Python supports arbitrarily large integers

print("Integer Declaration:")
print(f"a = {a}, b = {b}, c = {c}, large_int = {large_int}")

# 2. Type Checking
print("\nType Checking:")
print(f"Type of a: {type(a)}")
print(f"Is a an integer? {isinstance(a, int)}")

# 3. Arithmetic Operations
x = 7
y = 3
print("\nArithmetic Operations:")
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")      # Division (float result)
print(f"x // y = {x // y}")    # Floor division (integer result)
print(f"x % y = {x % y}")      # Modulus (remainder)
print(f"x ** y = {x ** y}")    # Exponentiation

# 4. Augmented Assignment
z = 5
print("\nAugmented Assignment:")
z += 2
print(f"z += 2: {z}")
z -= 1
print(f"z -= 1: {z}")
z *= 3
print(f"z *= 3: {z}")
z //= 2
print(f"z //= 2: {z}")

# 5. Conversion Between Types
float_num = 3.7
str_num = "42"
print("\nType Conversion:")
print(f"Float to int: {int(float_num)}")
print(f"String to int: {int(str_num)}")
print(f"Int to float: {float(a)}")
print(f"Int to string: {str(a)}")

# 6. Built-in Functions
numbers = [1, 2, 3, 4, 5]
print("\nBuilt-in Functions:")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Absolute value of b: {abs(b)}")
print(f"Power: {pow(2, 5)}")

# 7. Integer Division and Remainder
dividend = 17
divisor = 4
quotient, remainder = divmod(dividend, divisor)
print("\nInteger Division and Remainder:")
print(f"{dividend} divided by {divisor}: quotient = {quotient}, remainder = {remainder}")

# 8. Checking Even/Odd
num = 11
print("\nEven/Odd Check:")
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 9. Working with Binary, Octal, Hexadecimal
print("\nBinary, Octal, Hexadecimal:")
print(f"Binary of a: {bin(a)}")
print(f"Octal of a: {oct(a)}")
print(f"Hexadecimal of a: {hex(a)}")

# 10. Large Integer Operations
big1 = 10**50
big2 = 10**45
print("\nLarge Integer Operations:")
print(f"big1 + big2 = {big1 + big2}")
print(f"big1 - big2 = {big1 - big2}")

# 11. Integer in Collections
print("\nInteger in Collections:")
int_list = [1, 2, 3]
int_tuple = (4, 5, 6)
int_set = {7, 8, 9}
print(f"List: {int_list}")
print(f"Tuple: {int_tuple}")
print(f"Set: {int_set}")

