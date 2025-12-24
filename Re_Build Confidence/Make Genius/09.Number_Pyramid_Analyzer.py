even_nums = 0
odd_nums = 0
sum_nums = 0
try:
    x = input("Enter the list of Numbers(Separated from commas): ").strip().replace(" ","").split(",")
    y = list(map(int,x))
    for line in range(1, len(y) + 1):
        print(y[:line])
    for num in y:
        if num % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
    for i in range(len(y)-1):
        temp_sum = y[i] + y[i+1]
        if temp_sum > sum_nums:
            sum_nums = temp_sum

    print(f"""
Even Numbers :- {even_nums}
Odd Numbers  :- {odd_nums}
Largest Sum of 2 Consecutive Numbers :- {sum_nums}
""")

except ValueError:
    print("Please Try Again")
