num = input("Enter the list of numbers (Separated by commas): ").split(",")
lst = list(map(int, num))
print(f"""
count: {len(lst)}
sum  : {sum(lst)}
min  : {min(lst)}
max  : {max(lst)}
""")