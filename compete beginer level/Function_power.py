def count_even_odd(numbers):
    num_cat = {"Even":0, "Odd":0}
    for num in numbers:
        if num % 2 == 0:
            num_cat["Even"] += 1
        else:
            num_cat["Odd"] += 1
    return num_cat


try:
    nums = input("Enter the Numbers(Separated by commas): ").strip().replace(" ","").split(",")
    int_nums = list(map(int, nums))
    result = count_even_odd(int_nums)
    print(f"""
    Even Numbers : {result["Even"]}
    Odd Numbers  : {result["Odd"]}
    """)
except ValueError:
    print("Please enter numbers separated by commas")