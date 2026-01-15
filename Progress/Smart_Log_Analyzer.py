users = {}
suspicious = []

while True:
    line = input("Enter the LOG line: ").lower().strip().split()

    if line[0] ==  "end":
        break

    if len(line) == 0:
        pass
    else:
        if line[0] not in users:
            if line[1] == "fail":
                users[line[0]] = {"fail":1,"success":0}
            elif line[1] == "success":
                users[line[0]] = {"fail":0,"success":1}
            else:
                print("Invalid Log Line")
        else:
            if line[1] == "fail":
                users[line[0]]["fail"] += 1
            elif line[1] == "success":
                users[line[0]]["success"] += 1
            else:
                print("Invalid Log Line")
print("\n==== Log Report ====")
try:
    for user in users:
        print(f"{user:10} -> FAIL: {users[user]["fail"]}, SUCCESS: {users[user]["success"]}")
        if users[user]["fail"]>3:
            suspicious.append(user)

except NameError or KeyError:
    print("Log is empty")
print(f"Suspicious users: {suspicious}")