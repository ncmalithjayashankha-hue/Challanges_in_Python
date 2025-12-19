previous = None
while True:
    x = input("Enter the numbers: ").strip()
    if x.lower() == "end":
        print("Good Bye User ....!!!!")
        break
    if not x.isdigit():
        print("Please enter a number")
        continue
    current = int(x)
    if previous is not None and current == previous:
        print(f"Repeated Number detected: {current}")
    previous = current