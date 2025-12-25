def add():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a + b
    except ValueError:
        print("Numbers only.")
        return None


def sub():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a - b
    except ValueError:
        print("Numbers only.")
        return None


def mul():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a * b
    except ValueError:
        print("Numbers only.")
        return None


def div():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if b == 0:
            print("Division by zero not allowed.")
            return None
        return a / b
    except ValueError:
        print("Numbers only.")
        return None


while True:
    print("""
==== Calculator ====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        result = add()
    elif choice == "2":
        result = sub()
    elif choice == "3":
        result = mul()
    elif choice == "4":
        result = div()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
        continue

    if result is not None:
        print("Result:", result)
