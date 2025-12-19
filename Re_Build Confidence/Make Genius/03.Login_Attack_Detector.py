checking = {}
while True:
    x = input("Please enter a Log Line: ('END' to quit): ").strip().split()
    if not x:
        continue
    if x[0].upper() == "END":
        print("Good Bye User.....!!!!")
        break
    if len(x) !=2:
        print("Invalid Format")
        continue
    user = x[0].upper()
    status = x[1].upper()

    if status == "FAIL":
        if user in checking:
            checking[user] += 1
        else:
            checking[user] = 1

        if checking[user] == 3:
            print(f"Alert: {user} Failed Login 3 times in a row")
    elif status == "SUCCESS":
        checking[user] = 0
    else:
        print("Invalid Status")