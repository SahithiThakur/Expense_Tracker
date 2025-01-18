from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        """
        Adds a new expense to the tracker.
        """
        self.expenses.append(expense)

    def display_expenses(self):
        """
        Displays all the recorded expenses.
        """
        if self.expenses:
            print("\n--- All Expenses ---")
            for expense in self.expenses:
                print(expense)
        else:
            print("\nNo expenses recorded yet.")

    def summarize_expenses(self):
        """
        Summarizes the total expenses.
        """
        total = sum(expense.amount for expense in self.expenses)
        print(f"\n--- Total Expenses ---\nTotal: ${total:.2f}")
