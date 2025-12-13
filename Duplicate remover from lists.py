while True:
    try:
        list_input = input("Enter a list (Separated by Commas): ").split(",")
        unique_list = []
        test = list(map(int, list_input))
        for i in test:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)

        break
    except ValueError:
        print("Please enter a number")