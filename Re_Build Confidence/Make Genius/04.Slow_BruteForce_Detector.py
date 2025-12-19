checking = {}
while True:
    x = input("Enter the Log Lines ('END' to quit): ").strip().split()
    if not x:
        print("Please enter a Log Line")
        continue
    if x[0].upper() == "END":
        print("Good Bye User.....!!!!!")
        break
    if len(x) != 2:
        print("Invalid Log Format")
        continue
    user = x[0].upper()
    status = x[1].upper()

    if status == "FAIL":
        if user in checking:
            checking[user] += 1
        else:
            checking[user] = 1
        if checking[user] == 5:
            print(f"Alert {user} is Failed 5 times")
