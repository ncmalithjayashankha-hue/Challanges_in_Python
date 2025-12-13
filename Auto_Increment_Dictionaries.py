students ={}
while True:
    name = input("Enter the name of the student [(Q)uit]: ")
    if name.upper() == 'Q':
        print("Good Bye User...!!!")
        break
    else:
        key = f"S{len(students) + 1:03}"
        students[key] = {"Name": name}
print("\n" + "_"*37)
print(f"| {'index':15} | {'name':15} |")
print("-"*37)
for key,name in students.items():
    print(f"| {key:15} | {students[key]['Name']:15} |")