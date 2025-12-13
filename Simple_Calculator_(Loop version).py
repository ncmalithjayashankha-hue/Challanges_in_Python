while True:
    print()
    option = input("Enter Your Option: \n Add(A)\n Subtract(S)\n Multiply(M)\n Divide(D)\n Quit(Q)\n: ")
    output = "The answer is"

    if option.upper() in ['A', 'S', 'M', 'D']:
        a = [input("Enter the 1st Value: "), input("Enter the 2nd Value: ")]

        if option.upper() == 'A':
            print(f"{output} {int(a[0]) + int(a[1])}")

        elif option.upper() == 'S':
            print(f"{output} {int(a[0]) - int(a[1])}")

        elif option.upper() == 'M':
            print(f"{output} {int(a[0]) * int(a[1])}")

        elif option.upper() == 'D':
            print(f"{output} {int(a[0]) / int(a[1])}")

    elif option.upper() == 'Q':
        print("Goodbye!")
        break

    else:
        print("Invalid Option")
