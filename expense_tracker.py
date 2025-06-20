import json
import os

# File to store data
FILE_NAME = "expenses.json"

# Load existing data or create new
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

# Add a new expense
def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (food, travel, etc.): ")
    expenses.append({"amount": amount, "category": category})
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)
    print("Expense added!\n")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ₹{e['amount']} - {e['category']}")
    print()

# Summary of expenses
def summary():
    total = 0
    category_totals = {}
    for e in expenses:
        total += e["amount"]
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]
    
    print(f"Total spent: ₹{total}")
    print("Spending by category:")
    for cat, amt in category_totals.items():
        print(f" - {cat}: ₹{amt}")
    print()

# Menu system
while True:
    print("💸 Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
