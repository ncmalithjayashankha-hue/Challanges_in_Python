sus_activities = {}
while True:
    log_line = input("Enter the log line('END' to quit): ").strip().split()
    if not log_line:
        continue
    if log_line[0].upper() == "END":
        print("Good Bye User....!!!!")
        break
    if len(log_line) != 2:
        print("Invalid Log Format")
        continue
    user = log_line[0].upper()
    activity = log_line[1].upper()

    if activity == "FAIL" or activity == "IDLE":
        if user not in sus_activities:
            if activity == "FAIL":
                sus_activities[user]  = {"FAIL":1, "IDLE":0}
            else:
                sus_activities[user] = {"FAIL":0, "IDLE":1}
        else:
            if activity == "FAIL":
                sus_activities[user]["FAIL"] += 1
                sus_activities[user]["IDLE"] = 0
            else:
                sus_activities[user]["IDLE"] += 1
                sus_activities[user]["FAIL"] = 0

    elif activity == "LOGIN":
        if user in sus_activities:
            sus_activities[user]["FAIL"] = 0
            sus_activities[user]["IDLE"] = 0
        else:
            print(f"User {user} Dose not exist!!!")
    elif activity == "LOGOUT":
        sus_activities.pop(user, None)
        continue
    elif activity == "SUCCESS":
        if user in sus_activities:
            sus_activities[user]["FAIL"] = 0
            sus_activities[user]["IDLE"] = 0
        else:
            print(f"User {user} Dose not exist!!!")

    if user in sus_activities:
        if sus_activities[user]["FAIL"] >= 3:
            print(f"Alert {user} Trying to do something suspicious")
        elif sus_activities[user]["IDLE"] >= 3:
            print(f"Alert {user} Trying to do something suspicious")