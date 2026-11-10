import json
try:
     with open('ETracker.json','r') as f:
          a=json.load(f)
          print('Expenses loaded from ETracker.json')
except FileNotFoundError:
    a = []
    print("ETracker.json not found. Starting with an empty expense list.")

def add_expense():
    id=max([int(expense['id']) for expense in a])+1 if a else 1
    while True:
        try:
            amount=float(input('Enter expense amount: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
    category=input("Enter expense category: ")
    note=input("Enter expense note: ")
    expense={"id": id, "amount": amount, "category": category, "note": note}
    a.append(expense)

def list_expenses():
    if not a:
        print("No expenses found.")
    else:
        for expense in a:
            print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Note: {expense['note']}")

def delete_expense():
    id=(input("Enter expense ID to delete: "))
    for expense in a:
        if expense['id'] == id:
            a.remove(expense)
            print(f"Expense with ID {id} deleted.")
            return
    print(f"No expense found with ID {id}.")

def save_expenses():
    with open('ETracker.json','w') as f:
        json.dump(a,f)
        print("Expenses saved to ETracker.json")

def summarize_expenses():
    total_amount = sum(expense['amount'] for expense in a)
    print(f"Total Expenses: {total_amount}")
    category_summary = {}
    for expense in a:
        category = expense['category']
        category_summary[category] = category_summary.get(category, 0) + expense['amount']
    print("Expenses by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: {amount}")

while True:
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Summarize Expenses")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        summarize_expenses()
    elif choice == '4':
        delete_expense()
    elif choice == "5":
        save_expenses()
        break
    else:
        print("Invalid choice. Please try again.")