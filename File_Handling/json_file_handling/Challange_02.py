import json

friends = [
    {"Name":"Malith","Age":18,"Skills":["Swimming","Econ"],"Active":True},
    {"Name":"Dimal","Age":18,"Skills":["Chess","Maths"],"Active":False},
    {"Name":"Osanda","Age":18,"Skills":["Accounting","Dancing"],"Active":True},
]
new_friend_name = input("Enter your Friend's Name: ").strip()
new_friend_Age = int(input("Enter your Friend's Age: "))
new_friend_Skills = input("Enter your Friend's Skills (Separated by commas): ").strip().replace(" ","").split(",")
new_friend_Active = input("Is your friend active? (True/False): ").strip().lower() == "true"

new_friend = {
    "Name":new_friend_name,
    "Age":new_friend_Age,
    "Skills":new_friend_Skills,
    "Active":new_friend_Active
}
friends.append(new_friend)

with open("friends.json","w") as file:
    json.dump(friends,file,indent=4)
with open("friends.json","r") as file_open:
    data = json.load(file_open)
    for friend in data:
        print(f"{friend['Name']} - Age: {friend['Age']} - Skills: {', '.join(friend['Skills'])} - Active: {friend['Active']}")