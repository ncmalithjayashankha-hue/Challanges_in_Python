import json

profiles = [
    {"name": "Malith", "age": 18},
    {"name": "Jay", "age": 20}
]

with open("profiles.json", "w") as file:
    json.dump(profiles, file, indent=4)
