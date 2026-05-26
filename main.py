import json

FILE_NAME = "expenses.json"


def load_expenses():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):

    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):

    category = input("Enter Category: ")
    amount = int(input("Enter Amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense Added Successfully!")


def view_expenses(expenses):

    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    print("\n===== Expenses List =====\n")

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. {expense['category']} -> ₹{expense['amount']}"
        )


def total_expense(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense = ₹{total}")


def delete_expense(expenses):

    view_expenses(expenses)

    if len(expenses) == 0:
        return

    number = int(input("\nEnter Expense Number To Delete: "))

    if 1 <= number <= len(expenses):

        deleted = expenses.pop(number - 1)

        save_expenses(expenses)

        print(
            f"{deleted['category']} Expense Deleted Successfully!"
        )

    else:
        print("Invalid Expense Number!")


def search_expense(expenses):

    category = input("Enter Category To Search: ")

    found = False

    print()

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(
                f"{expense['category']} -> ₹{expense['amount']}"
            )

            found = True

    if not found:
        print("No Matching Expense Found!")


def highest_expense(expenses):

    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print("\nHighest Expense:")
    print(
        f"{highest['category']} -> ₹{highest['amount']}"
    )


def main():

    expenses = load_expenses()

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Highest Expense")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            search_expense(expenses)

        elif choice == "6":
            highest_expense(expenses)

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


main()