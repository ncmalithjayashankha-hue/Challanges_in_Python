try:
    list_of_numbers = input("Enter the Numbers (Separated by commas): ").split(",")
    int_list = map(int, list_of_numbers)
    print(sum(int_list))
except ValueError:
    print("You can't enter Texts")