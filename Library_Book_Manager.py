books={}    #an empty string

try:
    with open("books.txt", "r") as f:
        for line in f:
            name, sci, math, ict, avg = line.strip().split(",")
            books[name] = {
                "Science": int(sci),
                "Math": int(math),
                "ICT": int(ict),
                "Average": float(avg)
            }
except FileNotFoundError:
    pass   # file doesn't exist on first run, so ignore

while True:
    print("\n==== Student Manager ====")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search a Book")
    print("3. Borrow a Book")
    print("3. Return a Book")
    print("4. Remove a Book")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print()
