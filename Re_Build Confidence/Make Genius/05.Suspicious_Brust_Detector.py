checks = {}
while True:
    x = input("Enter the Log lines('END' to quit): ").strip().split()
    if not x:
        continue
    if x[0].upper() == "END":
        print("Good Bye User....!!!!")
        break
    if len(x) != 2:
        print("Invalid Format")
        continue

    user = x[0].upper()
    status = x[1]

    if status.upper() == "FAIL":
        if user in checks:
            checks[user] += 1
        else:
            checks[user] = 1
        if checks[user] == 3:
            print(f"Alert! {user} Tries to login multiple times")
    elif status.upper() == "SUCCESS":
        checks[user] = 0
    else:
        print("Invalid Log status ):")
