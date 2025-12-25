c = 0
numbers = []
try:
    while c<=2:
        number = int(input("Enter a number: "))
        numbers.append(number)
        c+=1
    print(f"""
Largest number: {max(numbers)}
Smallest number: {min(numbers)}
Average number: {sum(numbers)/len(numbers)}
""")
except ValueError:
    print("Please enter a number")
