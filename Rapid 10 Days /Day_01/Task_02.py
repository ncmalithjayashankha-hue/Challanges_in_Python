try:
    marks = int(input("Enter the Marks: "))
    if not marks:
        print("Please enter a number")
    if 0>marks<100:
        print("Please enter a number between 0 and 100")
    if marks >= 75:
        print("A")
    elif marks >= 65:
        print("B")
    elif marks >= 55:
        print("C")
    elif marks >= 35:
        print("S")
    else:
        print("W")
except ValueError:
    print("Please enter a number")