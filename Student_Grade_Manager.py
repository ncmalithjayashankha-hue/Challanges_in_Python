f = open("student_manager.txt", "w")
for i in range(1):
    name = input("Enter Your Name: ")
    sci_marks = int(input("Enter the marks for Science Subject: "))
    math_marks = int(input("Enter the marks for Maths Subject: "))
    ict_marks = int(input("Enter the marks for ICT Subject: "))

    dd = {
        "name":name,
        "Science":sci_marks,
        "Math":math_marks,
        "ICT":ict_marks,
        "Average":((sci_marks+math_marks+ict_marks)/3)
    }
    print(dd)

print(("-" * 20) * 5)
print("| {:15} | {:15} | {:15} | {:15} | {:15} | ".format(
    "Name", "Science", "Maths", "ICT", "Average"
))
print(("-" * 20) * 5)
print("| {:15} | {:15} | {:15} | {:15} | {:15.2f} |".format(
    dd["name"],
    dd["Science"],
    dd["Math"],
    dd["ICT"],
    dd["Average"]
))
f.write(str(dd))
f.close()