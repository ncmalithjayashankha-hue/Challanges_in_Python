for i in range(5):
    marks = input("Enter the marks(separated by commas): ")
    with open("demo.txt",'a') as file:
        file.writelines(f"\n{marks}")