count = 0
logs = {"INFO":0,"WARNING":0,"ERROR":0,"CRITICAL":0}
while True:
    inpt_log = input("Enter the log line by line('END' to Finish): ").split()
    count += 1
    if not inpt_log:
        continue
    elif inpt_log[0].upper() == "END":
        count -= 1
        break
    elif inpt_log[0].upper() == "INFO":
        logs["INFO"] += 1
    elif inpt_log[0].upper() == "WARNING":
        logs["WARNING"] += 1
    elif inpt_log[0].upper() == "ERROR":
        logs["ERROR"] += 1
    elif inpt_log[0].upper() == "CRITICAL":
        logs["CRITICAL"] += 1
    else:
        print("Invalid Log Line")
print(f"""
==== log Report ====
Total log lines : {count}
INFO            : {logs["INFO"]}
WARNING         : {logs["WARNING"]}
ERROR           : {logs["ERROR"]}
CRITICAL        : {logs["CRITICAL"]}
""")


