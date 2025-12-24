num = input("Enter a number(Separated by commas): ")
max_num = num.split(",")
lst = list(map(int, max_num))
print(max(lst))
