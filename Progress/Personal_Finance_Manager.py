Finance = {
    "Income":[],
    "Expenses":[]
}

def add_income():
    try:
        amount = float(input("Enter your amount: "))
        source = input("Enter Source of Income: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        Finance["Income"].append({
            "amount":amount,
            "source":source,
            "date":date
        })
        print("Income Added Successfully")
    except ValueError:
        print("Please enter valid details")

def add_expenses():
    try:
        amount = float(input("Enter your amount: "))
        category = input("Enter Category of Expenses: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        Finance["Expenses"].append({
            "amount": amount,
            "category": category,
            "date": date
        })
        print("Expense Added Successfully")
    except ValueError:
        print("Please enter valid details")

def show_balance():
    total_income = sum(item["amount"] for item in Finance["Income"])
    total_expenses = sum(item["amount"] for item in Finance["Expenses"])
    print(f"Your Current Balance is {total_income - total_expenses}")

def monthly_summary(month, year):
    """Show total income and expenses for a specific month"""
    month_str = f"{year}-{month:02d}"
    income_total = sum(item["amount"] for item in Finance["Income"] if item['date'].startswith(month_str))
    expense_total = sum(item["amount"] for item in Finance["Expenses"]if item['date'].startswith(month_str))
    print(f"---- Summary for {month_str} ----")
    print(f"Total Income: {income_total}")
    print(f"Total Expenses: {expense_total}")
    print(f"Net Balance: {income_total - expense_total}\n")

def search_transactions(criteria, value):
    """Search Transaction by Criteria"""
    print(f"--- Searching for {criteria} = {value} ---")

    for item in Finance["Income"]:
        if str(item.get(criteria, "")).lower() == str(value).lower():
            print("Income:",item)
    for item in Finance["Expenses"]:
        if str(item.get(criteria, "")).lower() == str(value).lower():
            print("Expenses:",item)
    print("Search complete. \n")


def main():
    while True:
        print("""
==== Finance Manager ====
1. Add Income
2. Add Expenses
3. Show Balance
4. Monthly Summary
5. Search Transactions
6. Exit
        """)
        try:
            option = int(input("Enter your choice: "))

            if option == 1:
                add_income()
            elif option == 2:
                add_expenses()
            elif option == 3:
                show_balance()
            elif option == 4:
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2025): "))
                monthly_summary(month, year)
            elif option == 5:
                criteria = input("Search by (amount/source/category/date): ").lower()
                value = input("Enter value to search: ")
                search_transactions(criteria, value)
            elif option == 6:
                print("Goodbye! See you next time.")
                break
            else:
                print("Please enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


# ------------------- Start Program -------------------
main()