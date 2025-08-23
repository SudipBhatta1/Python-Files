# 1. Basic Variable Declaration
name = "John"            # String variable
age = 25                # Integer variable
height = 5.9            # Float variable
is_student = True       # Boolean variable

# 2. Multiple Assignment
x, y, z = 1, 2, 3       # Assign multiple values at once
a = b = c = 10          # Same value to multiple variables

# 3. Variable Naming Rules
valid_name = "Valid"     # Start with letter or underscore
_private = "Private"     # Underscore prefix for private variables
first_name = "John"      # Use underscores for spaces
# 2invalid = "Invalid"   # Can't start with number (commented as it's invalid)
# my-var = "Invalid"     # Can't use hyphens (commented as it's invalid)

# 4. Variable Type Checking
number = 42
print(f"Type of number: {type(number)}")  # Check variable type
print(f"Is number an integer? {isinstance(number, int)}")  # Type checking

# 5. Variable Type Conversion
string_num = "123"
converted_num = int(string_num)    # String to Integer
float_num = float(converted_num)   # Integer to Float
back_to_string = str(float_num)    # Float to String

# 6. Variable Scope
global_var = "I'm global"          # Global variable

def scope_demo():
    local_var = "I'm local"        # Local variable
    print(local_var)
    print(global_var)              # Can access global variable

# 7. Constants (by convention in Python)
MAX_VALUE = 100                    # Constants are usually uppercase
PI = 3.14159


# 8. Dynamic Typing
dynamic_var = 100      # Integer
dynamic_var = "Hello"  # Now it's a string
dynamic_var = [1,2,3]  # Now it's a list


# 9. Variable Memory Management
import sys
number_memory = sys.getsizeof(number)  # Get memory size of variable

# 10. Variable Deletion
temp_var = "Delete me"
del temp_var                       # Delete variable

# Demonstration
def main():
    print("\n=== Variable Demonstration ===")
    print(f"Basic Variables:")
    print(f"Name: {name}, Type: {type(name)}")
    print(f"Age: {age}, Type: {type(age)}")
    print(f"Height: {height}, Type: {type(height)}")
    print(f"Is Student: {is_student}, Type: {type(is_student)}")
    
    print("\nMultiple Assignment:")
    print(f"x: {x}, y: {y}, z: {z}")
    print(f"a: {a}, b: {b}, c: {c}")
    
    print("\nType Conversion:")
    print(f"String '123' to Integer: {converted_num}")
    print(f"Integer to Float: {float_num}")
    print(f"Float to String: {back_to_string}")
    
    print("\nVariable Memory:")
    print(f"Memory size of number {number}: {number_memory} bytes")
    
    print("\nDynamic Typing:")
    print(f"Dynamic variable type: {type(dynamic_var)}")
    
    scope_demo()

if __name__ == "__main__":

    main()

