import json
import datetime

try:
     with open('ETracker.json','r') as f:
          a=json.load(f)
          print('Expenses loaded from ETracker.json')
except FileNotFoundError:
    a = []
    print("ETracker.json not found. Starting with an empty expense list.")

def add_expense():
    id = max([int(expense['id']) for expense in a]) + 1 if a else 1
    while True:
        try:
            amount = float(input('Enter expense amount: '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
            
    category = input("Enter expense category: ")
    date_str = str(datetime.date.today())  
    note = input("Enter Expense note: ")
    
    expense = {
        "id": id, 
        "date": date_str, 
        "amount": amount, 
        "category": category, 
        "note": note
    }
    a.append(expense)
    print("Expense added successfully!")

def list_expenses():
    if not a:
        print("No expenses found.")
    else:
        for expense in a:
            print(f"ID: {expense['id']} | Date: {expense['date']} | Amount: {expense['amount']} | Category: {expense['category']} | Note: {expense['note']}")

def delete_expense():
    id = int(input("Enter expense ID to delete: "))
    for expense in a:
        if expense['id'] == id:
            a.remove(expense)
            print(f"Expense with ID {id} deleted.")
            return
    print(f"No expense found with ID {id}.")

def save_expenses():
    with open('ETracker.json','w') as f:
        json.dump(a, f)
        print("Expenses saved to ETracker.json")

def monthly_summary(month=None):
    if not month:
        month = input("Enter month to summarize (e.g., 2026-11): ")  
    category_summary = {}
    total_monthly_amount = 0
    matched_count = 0
    
    for expense in a:
        expense_date = expense.get('date', '')
        
        if expense_date.startswith(month):
            matched_count += 1
            category = expense['category']
            category_summary[category] = category_summary.get(category, 0) + expense['amount']
            total_monthly_amount += expense['amount']
            
    if matched_count == 0:
        print(f"No expenses found for {month}.")
        return
        
    print(f"\n--- Summary for {month} ---")
    print(f"Total Expenses: {total_monthly_amount}")
    print("Expenses by Category:")
    for category, amount in category_summary.items():
        print(f"  {category}: {amount}")
        
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
        monthly_summary()
    elif choice == '4':
        delete_expense()
    elif choice == "5":
        save_expenses()
        break
    else:
        print("Invalid choice. Please try again.")