try:
    num = int(input("Enter a number: "))
    print(num*num)
except ValueError:
    print("PLease Enter a Number")