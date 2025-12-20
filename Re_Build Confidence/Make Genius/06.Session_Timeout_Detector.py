checks = {}
while True:
    x = input("Enter the Log lines('END' to quit): ").strip().split()

    if not x:
        continue
    if x[0].upper() =="END":
        print("GoodBye User....!!!!!")
        break
    if not len(x) == 2:
        print("Invalid Log Format")
        continue

    user = x[0].upper()
    session = x[1].upper()

    if session == "IDLE":
        if user in checks:
            checks[user] += 1
        else:
            checks[user] = 1
        if checks[user] == 3:
            print(f"Alert! {user} Session Timeout Risk")
    elif session == "LOGIN":
        checks[user] = 0
    elif session == "LOGOUT":
        del(checks[user])
    else:
        print("Invalid Log status")