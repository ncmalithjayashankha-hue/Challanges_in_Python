list_of_items = input("Enter the Numbers (Separated by commas): ").strip().split(",")
list_of_nums = list(map(int, list_of_items))
unique_sorted = sorted(set(list_of_items))
print(unique_sorted)