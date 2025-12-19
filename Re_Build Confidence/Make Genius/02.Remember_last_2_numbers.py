previous = None
count = 1
while True:
    x = input("Enter the numbers: ").strip()
    if x.lower() == "end":
        print("Good Bye User ....!!!")
        break
    if not x.isdigit():
        print("Please enter a number")
        continue
    current = int(x)
    if previous is not None and current == previous:
        count +=1
    else:
        count = 1
    if count == 3:
        print(f"Alert: {current} Appeared 3 times a row")
    previous = current