nums = input("Enter the Numbers (Separated by commas): ").split(",")
num_list = {}

numss = list(map(int, nums))
for num in numss:
    if num not in num_list:
        num_list[num] = 1
    else:
        num_list[num] += 1
print(num_list)