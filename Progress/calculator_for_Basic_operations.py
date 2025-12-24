try:
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    option = input("Enter your choice ( + , - , * , / ): ")
    a = int(input("enter a Number: "))
    b = int(input("enter a Number: "))

    if option == "+":
        print(add(a,b))
    elif option == "-":
        print(subtract(a,b))
    elif option == "*":
        print(multiply(a,b))
    elif option == "/":
        print(divide(a,b))
except:
    print("try again")