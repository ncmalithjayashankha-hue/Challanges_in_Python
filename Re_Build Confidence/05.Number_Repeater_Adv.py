nums = input("Enter the Numbers (Separated by commas): ").split(",")
num_list = {}
repeted_nums = []
unique_nums = []

numss = list(map(int, nums))
for num in numss:
    if num not in num_list:
        num_list[num] = 1
    else:
        num_list[num] += 1
for num in num_list:
    if num_list[num] > 1:
        repeted_nums.append(num)
    else:
        unique_nums.append(num)
print(f"""
Unique Numbers : {len(unique_nums)} ({unique_nums})
Repeated Numbers : {len(repeted_nums)} ({repeted_nums})
""")