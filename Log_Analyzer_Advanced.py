complete_message = {"INFO":0,"WARNING":0,"ERROR":0}
Activity_detector = {"failed":0,"timeout":0}
count = 0
user_input = input("Enter a log message (Type \"END\" When Finish): ")
log_Message = user_input.split()
while log_Message and log_Message[0] != "END":

    for value in log_Message:
        if value.lower() == "failed":
            Activity_detector["failed"] = Activity_detector["failed"] + 1
        elif value.lower() == "timeout":
            Activity_detector["timeout"] = Activity_detector["timeout"] + 1


    if log_Message[0] == "INFO":
        complete_message["INFO"] = complete_message["INFO"] + 1
    elif log_Message[0] == "WARNING":
        complete_message["WARNING"] = complete_message["WARNING"] + 1
    elif log_Message[0] == "ERROR":
        complete_message["ERROR"] = complete_message["ERROR"] + 1
    elif log_Message[0] == "END":
        break
    else:
        print("Invalid Log Message")
    log_Message = input("Enter a log message (Type \"END\" When Finish): ").split()
print(f"""
==== Log Summary ====
INFO : {complete_message["INFO"]}
WARNING : {complete_message["WARNING"]}
ERROR : {complete_message["ERROR"]}

Suspicious Patterns:
failed : {Activity_detector["failed"]}
timeout :{Activity_detector["timeout"]}
""")