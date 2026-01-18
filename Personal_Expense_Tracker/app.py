import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
import pandas as pd
import matplotlib.pyplot as plt
import os

console = Console()

DATA_FILE = 'expenses.json'

#Load existing expenses

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#Save expenses
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date (YYYY-MM-DD) or leave empty for today: ")
    note = input("Enter Note (Optional): ")

    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    expenses.append({
        "amount": amount,
        "category": category,
        "date": date,
        "note": note
    })

    save_expenses(expenses)
    print("Expense Added!")

def view_expenses(expenses):
    table = Table(title="Expenses")
    table.add_column("Amount",justify="right")
    table.add_column("Category")
    table.add_column("Date")
    table.add_column("Note")

    for exp in expenses:
        table.add_row(str(exp["amount"]), exp["category"], exp["date"], exp["note"])

    console.print(table)

def view_by_category(expenses):
    category = input("Enter Category to filter: ")
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    view_expenses(filtered)

def summary(expenses):
    if not expenses:
        print("No expenses to Summarize.!")
        return

    df = pd.DataFrame(expenses)
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])

    choice = input("Summary by [weekly/monthly]? : ").lower()

    if choice == "weekly":
        df['week'] = df['date'].dt.isocalendar().week
        summary_df = df.groupby('week')['amount'].sum().reset_index()
        table = Table(title="Weekly Summary of Expenses")
        table.add_column("Week", justify="center")
        table.add_column("Total_Amount", justify="right")
        for  _, row in summary_df.iterrows():
            table.add_row(str(int(row["week"])),f"{row['amount']:.2f}")
    else:
        df['month'] = df['date'].dt.to_period('M')
        summary_df = df.groupby('month')['amount'].sum().reset_index()
        table = Table(title="Monthly Summary of Expenses")
        table.add_column("Month", justify="center")
        table.add_column("Total_Amount", justify="right")
        for _, row in summary_df.iterrows():
            table.add_row(str(row['month']),f"{row['amount']:.2f}")

    console.print(table)

def plot_trends(expenses):
    df = pd.DataFrame(expenses)
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)

    plt.figure(figsize = (10,5))
    plt.plot(df['date'], df['amount'], marker='o')
    plt.title('Expenses Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.show()

def search_expenses(expenses):
    keyword = input("Enter keyword to search: ").lower()
    results = [e for e in expenses if keyword in e['note'].lower() or keyword in e['category'].lower()]
    view_expenses(results)

def main():
    os.system("clear")
    expenses = load_expenses()

    while True:
        print("\n1.Add Expense")
        print("2.View All Expenses")
        print("3.View by Category")
        print("4.Summary")
        print("5.Plot Trends")
        print("6.Search Expenses")
        print("7.Exit")

        choice = input("Choose an Option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            summary(expenses)
        elif choice == "5":
            plot_trends(expenses)
        elif choice == "6":
            search_expenses(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()