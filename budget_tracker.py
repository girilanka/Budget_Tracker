import pickle

total_income = 0
expenses_list = []
expense_categories = {}

def main():
    load_data()  
    while True:
        print("Budget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Remaining Budget")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            view_remaining_budget()
        elif choice == "5":
            save_data()
            break
        else:
            print("Invalid choice. Please try again.")

def add_income():
    global total_income
    amount = float(input("Enter income amount: "))
    total_income += amount

def add_expense():
    global total_income
    global expenses_list
    global expense_categories
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses_list.append((category, amount))
    total_income -= amount
    expense_categories[category] = expense_categories.get(category, 0) + amount

def view_expenses():
    global expenses_list
    for category, amount in expenses_list:
        print(f"Category: {category}, Amount: {amount}")

def view_remaining_budget():
    global total_income
    global expenses_list
    remaining_budget = total_income - sum(amount for _, amount in expenses_list)
    print(f"Remaining Budget: {remaining_budget}")

def save_data():
    global total_income
    global expenses_list
    global expense_categories
    data = {
        "total_income": total_income,
        "expenses_list": expenses_list,
        "expense_categories": expense_categories,
    }
    with open("budget_data.pkl", "wb") as file:
        pickle.dump(data, file)

def load_data():
    global total_income
    global expenses_list
    global expense_categories
    try:
        with open("budget_data.pkl", "rb") as file:
            data = pickle.load(file)
            total_income = data["total_income"]
            expenses_list = data["expenses_list"]
            expense_categories = data["expense_categories"]
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()
