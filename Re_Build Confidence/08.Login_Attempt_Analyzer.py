dict_status = {"FAIL":0,"SUCCESS":0}
failed_users = {}
count = 0
while True:
    login_attempts = input("Enter the Login Attempts (Line by Line) ('END' to finish) : ").upper().split()

    if not login_attempts:
        print("Please Enter a Line...!")
        continue
    if login_attempts[0] == "END":
        break
    count +=1

    if len(login_attempts)==2:
        user = login_attempts[0]
        status = login_attempts[1]
    else:
        continue

    if status == "FAIL":
        if user in failed_users:
            failed_users[user] += 1
        else:
            failed_users[user] = 1

    if status in dict_status:
        dict_status[status] += 1
    else:
        print("Invalid Login Attempt Line....!")

max_count = 0
max_user = ""
for user in failed_users:
    if failed_users [user] > max_count:
        max_count = failed_users [user]
        max_user = user

print(f"""
==== Login Attempt Analysis ====
Total Attempts      : {count}
Successful Logins   : {dict_status["SUCCESS"]}
Failed Logins       : {dict_status["FAIL"]}
Failed Users        : {failed_users}
Most Failed Users   : {max_user}
""")
if not failed_users:
    print("No Failed Users")