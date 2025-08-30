def demonstrate_control_flow():
    # 1. If-Elif-Else Statements
    print("1. If-Elif-Else Demo:")
    score = 85
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")

    # 2. For Loops
    print("\n2. For Loop Demo:")
    # Range-based for loop
    for i in range(3):
        print(f"Count: {i}")
    
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    # 3. While Loops
    print("\n3. While Loop Demo:")
    count = 3
    while count > 0:
        print(f"Countdown: {count}")
        count -= 1

    # 4. Break Statement
    print("\n4. Break Statement Demo:")
    for i in range(5):
        if i == 3:
            break
        print(f"Number before break: {i}")

    # 5. Continue Statement
    print("\n5. Continue Statement Demo:")
    for i in range(5):
        if i == 2:
            continue
        print(f"Number after continue: {i}")

    # 6. Try-Except Block
    print("\n6. Try-Except Demo:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("No error occurred")
    finally:
        print("This always executes")

    # 7. Match Case (Python 3.10+)
    print("\n7. Match Case Demo:")
    status = "success"
    match status:
        case "success":
            print("Operation successful")
        case "error":
            print("Operation failed")
        case _:
            print("Unknown status")

    # 8. Nested Control Structures
    print("\n8. Nested Control Structures Demo:")
    for i in range(3):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

if __name__ == "__main__":
    demonstrate_control_flow()
