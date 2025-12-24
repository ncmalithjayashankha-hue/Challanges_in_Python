def get_mark(subject):
    while True:
        try:
            mark = int(input(f"{subject} : "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100")
        except ValueError or KeyError:
            print("Invalid input ! Enter a Number.")
def get_student_data():
    name = input("Enter Student Name: ")
    print(f"Enter marks for {name}")
    sci = get_mark("Science")
    math =get_mark("Maths")
    eng = get_mark("English")
    return{
        "Name": name,
        "Science": sci,
        "Maths": math,
        "English": eng
    }
def calculate_total(students):
    for stu in students:
        total = stu["Science"] + stu["Maths"] + stu["English"]
        stu["Total"] = total
        stu["Average"] = round(total / 3 , 2)

def highest_score(students):
    return max(students, key = lambda x : x["total"])

def subject_average(students):
    count = len(students)

    sci_avg = sum(s["Science"] for s in students)/count
    math_avg = sum(s["Maths"] for s in students)/count
    eng_avg = sum(s["English"] for s in students)/count

    return{
        "Science_avg": round(sci_avg, 2),
        "Maths_avg": round(math_avg, 2),
        "English_avg": round(eng_avg, 2)
    }

def main():
    try:
        count = int(input("How many students "))
        if count <= 0:
            print("Number oof students must be positive.")
            return
    except:
        print("Invalid Number")
        return
    students=[]

    for i in range (count):
        print(f"\n--- Student {i+1} ---")
        data = get_student_data()
        students.append(data)
        calculate_total(students)
        highest = highest_score(students)
        subs_avg = subject_average()

main()