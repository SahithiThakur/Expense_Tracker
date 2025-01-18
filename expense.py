from datetime import datetime

class Expense:
    def __init__(self, description: str, amount: float, date: str = None):
        """
        Initializes the expense with description, amount, and date.
        If no date is provided, it will use the current date.
        """
        self.description = description
        self.amount = amount
        self.date = date or datetime.today().strftime('%Y-%m-%d')

    def __str__(self):
        """
        Returns a string representation of the expense.
        """
        return f"Description: {self.description}, Amount: ${self.amount:.2f}, Date: {self.date}"
