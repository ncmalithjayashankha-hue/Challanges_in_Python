try:
    marks = input("Enter the marks for your all Subjects (Separated by commas): ").strip().split(",")
    int_marks = list(map(int, marks))
    print(f"Total Marks: {sum(int_marks)} \nAverage Marks: {sum(int_marks) / len(int_marks)}\nHighest Marks: {max(int_marks)} \nLowest Marks: {min(int_marks)}")
except:
    print("Try Again")