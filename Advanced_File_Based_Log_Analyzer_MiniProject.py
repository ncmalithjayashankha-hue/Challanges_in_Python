complete_message = {"INFO":0,"WARNING":0,"ERROR":0}
suspicious = {"failed":0,"timeout":0,"unauthorized":0}

file_name = input("Enter file name: ")
file_log = open(file_name,"r")

lines_analyzed = 0
try:
    for line in file_log:
        lines_analyzed += 1
        line_parts = line.split()
        if line_parts:
            log_type = line_parts[0].upper().replace(":","")
            if log_type == "INFO":
                complete_message["INFO"] += 1
            elif log_type == "WARNING":
                complete_message["WARNING"] += 1
            elif log_type == "ERROR":
                complete_message["ERROR"] += 1
            else:
                print(f"Skipping line {lines_analyzed}: Unknown log type '{log_type}' ")
except FileNotFoundError:
    print("File Not Found")

print(f"""
==== LOG Summary ====
Total Lines Analyzed    : {lines_analyzed}
INFO                    : {complete_message["INFO"]}
WARNING                 : {complete_message["WARNING"]}
ERROR                   : {complete_message["ERROR"]}

==== Security Alerts ====
failed
timeout
unauthorized

Most Suspicious Log Level :
""")
file_log.close()