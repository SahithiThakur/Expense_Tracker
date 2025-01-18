from tracker import ExpenseTracker
from expense import Expense

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Total Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: $"))
            expense = Expense(description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            tracker.display_expenses()

        elif choice == "3":
            tracker.summarize_expenses()

        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

