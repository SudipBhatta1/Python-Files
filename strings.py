# 1. String Creation and Basic Operations
single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = '''This is a
multi-line string'''
raw_string = r"C:\Users\name"  # Raw string ignores escape characters

# 2. String Concatenation
full_greeting = single_quoted + ' ' + double_quoted
formatted_string = f"{single_quoted} {double_quoted}!"
print("String Concatenation:")
print(full_greeting)
print(formatted_string)

# 3. String Methods
text = "  Python Programming  "
print("\nString Methods:")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Strip: {text.strip()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# 4. String Slicing
sample = "Hello World"
print("\nString Slicing:")
print(f"First 5 characters: {sample[0:5]}")
print(f"Last 5 characters: {sample[-5:]}")
print(f"Reverse string: {sample[::-1]}")

# 5. String Methods for Checking
print("\nString Checking Methods:")
print(f"Is alpha? {'abc'.isalpha()}")
print(f"Is numeric? {'123'.isnumeric()}")
print(f"Is alphanumeric? {'abc123'.isalnum()}")
print(f"Starts with 'He'? {sample.startswith('He')}")
print(f"Ends with 'ld'? {sample.endswith('ld')}")


# 7. String Character Count and Find
text = "banana"
print("\nCharacter Operations:")
print(f"Count of 'a': {text.count('a')}")
print(f"First position of 'a': {text.find('a')}")
print(f"Last position of 'a': {text.rfind('a')}")

# 8. String Join and Partition
words = ['Python', 'is', 'awesome']
print("\nJoin and Partition:")
print(f"Join: {' '.join(words)}")
print(f"Partition: {'Python-is-awesome'.partition('-')}")

# 9. String Case Conversion
mixed_case = "PyThOn"
print("\nCase Conversion:")
print(f"Title case: {mixed_case.title()}")
print(f"Swapped case: {mixed_case.swapcase()}")
print(f"Capitalize: {mixed_case.capitalize()}")

# 10. String Alignment
text = "Python"
width = 20
print("\nString Alignment:")
print(f"Left aligned: {text.ljust(width, '*')}")
print(f"Right aligned: {text.rjust(width, '*')}")
print(f"Center aligned: {text.center(width, '*')}")

# 11. String Escape Characters
print("\nEscape Characters:")
print("Line1\nLine2")  # Newline
print("Tab\tSpace")    # Tab
print("Quote: \"Hello\"")  # Quotes

