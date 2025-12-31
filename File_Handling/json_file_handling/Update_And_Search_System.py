import json
import os

file_name = "friends.json"

if not os.path.exists(file_name):
    print("friends.json file not found.")
    exit()

new_friend = input("Enter the friend name to update: ").strip().lower()

with open(file_name, "r") as f:
    x = json.load(f)

found = False

for friend in x:
    if friend["Name"].lower() == new_friend:
        found = True

        age = int(input("Enter the age of the friend to update: "))
        skills = input("Enter the skills of the friend to update: ").strip().split(",")
        active = input("Enter the active status of the friend to update (True/False): ").strip().lower() == "true"

        friend["Age"] = age
        friend["Skills"] = [s.strip() for s in skills]
        friend["Active"] = active

        break

if not found:
    print("Friend not found.")
    exit()

with open(file_name, "w") as f:
    json.dump(x, f, indent=4)

print("Friend updated successfully.")
