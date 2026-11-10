# 💰 Expense Tracker (Python CLI)

A simple **command-line app** to record your daily expenses, see where your money goes, and keep your data safe in a file, so nothing is lost when you close the program.

Built as **Project 1** of my AI Engineer learning roadmap, using only core Python (no extra libraries).

---

## ✨ What it can do

| # | Feature | What happens |
|---|---------|--------------|
| 1 | **Add expense** | Saves amount, category, note and today's date |
| 2 | **List expenses** | Shows every saved expense |
| 3 | **Summarize** | Shows the total and the total per category |
| 4 | **Delete expense** | Removes one expense using its ID |
| 5 | **Exit** | Saves everything and closes |

Your data is stored in `ETracker.json`, so it is still there the next time you open the app.

---

## 🚀 How to run

You need **Python 3.12 or newer**. Check with:

```bash
python --version
```

Then:

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
python expense_tracker.py
```

> On Mac, use `python3` instead of `python` if `python` is not found.

---

## 🖥️ Sample output

```
1. Add Expense
2. List Expenses
3. Summarize Expenses
4. Delete Expense
5. Exit
Enter your choice: 1
Enter expense amount: 250
Enter expense category: food
Enter expense note: lunch

Enter your choice: 3
Total Expenses: 570.0
Expenses by Category:
food: 450.0
travel: 120.0
```

---

## 🧠 How it works (explained simply)

### 1. Every expense is a dictionary

One expense is stored like a small card with labels:

```python
{"id": 1, "amount": 250.0, "category": "food", "note": "lunch"}
```

All the cards are kept together in a **list**. Think of it as a box of cards.

### 2. Loading data when the app starts

The app tries to open the file. If this is the first run, the file does not exist yet, so it starts with an empty list instead of crashing:

```python
try:
    with open('ETracker.json', 'r') as f:
        a = json.load(f)
except FileNotFoundError:
    a = []
```

- `json.load` reads the file and turns the text back into a Python list.
- `except FileNotFoundError` is the safety net for the very first run.

### 3. Safe input: no crash on wrong typing

If someone types `abc` where a number is needed, the app does not crash. It asks again:

```python
while True:
    try:
        amount = float(input('Enter expense amount: '))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
```

- `try` attempts to turn the text into a number.
- If it fails, `except` prints a message and the loop asks again.
- `break` only runs when the number was valid.

### 4. Every expense gets a unique ID

```python
id = max([int(expense['id']) for expense in a]) + 1 if a else 1
```

It takes the biggest existing ID and adds 1. If the list is empty, the first ID is 1. This keeps IDs unique even after deleting items.

### 5. Adding up by category with a dictionary

A dictionary works like a tally sheet: one row per category, with a running total.

```python
category_summary = {}
for expense in a:
    category = expense['category']
    category_summary[category] = category_summary.get(category, 0) + expense['amount']
```

- `.get(category, 0)` means "give me the current total, or 0 if this category is new".

### 6. Saving to the file

```python
with open('ETracker.json', 'w') as f:
    json.dump(a, f)
```

- `'w'` means write. `json.dump` turns the list into text and stores it in the file.

---

## 📁 Project structure

```
expense-tracker/
├── expense_tracker.py   # the whole app
├── ETracker.json        # your saved data (created automatically)
├── .gitignore
└── README.md
```

---

## 📚 What I learned

- Variables, input, print and f-strings
- Loops, lists, dictionaries and functions
- Saving and loading data with the `json` module
- Handling errors with `try / except`
- Using Git and GitHub to publish a project

---

## 🔮 Ideas to improve next

- Show a summary for one chosen month
- Edit an existing expense
- Export expenses to CSV
- Add automated tests

---

Made by **<Kamal Teja Goud M>** · Part of my 16-week AI Engineer roadmap
