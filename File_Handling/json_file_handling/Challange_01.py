import json

friends = [
    {"Name":"Malith","Age":18,"Skills":["Swimming","Econ"],"Active":True},
    {"Name":"Dimal","Age":18,"Skills":["Chess","Maths"],"Active":False},
    {"Name":"Osanda","Age":18,"Skills":["Accounting","Dancing"],"Active":True},
]
with open("friends.json","w") as file:
    json.dump(friends,file,indent=4)
with open("friends.json","r") as file_open:
    data = json.load(file_open)
    for friend in data:
        print(f"{friend['Name']} - Age: {friend['Age']} - Skills: {', '.join(friend['Skills'])} - Active: {friend['Active']}")