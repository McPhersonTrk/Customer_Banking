"""Imports the SavingsAccount class and attributes from the Account.py file."""
from Account import Account
class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interest_rate, months):
        self.account_holder = account_holder
        self.balance = balance
        self.interest = interest_rate
        self.months = months
        balance = float(int(self.balance))
    def deposit(self, amount):
        self.balance += amount        
        print(f" Deposited ${amount}. New Balance is ${self.balance}")
    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance -= amount        
            print(f" Withdrew ${amount}. New Balance is ${self.balance}")
        else:
            print("Insufficient Funds")
        account_holder = SavingsAccount(Account(account_holder=""))
    def calculate_interest(self):
        interest_earned = float(int((self.balance * self.interest * self.months) / 100))
        self.balance += interest_earned
        print(f"Interest earned: ${interest_earned}. New balance: ${self.balance}")
        return self.balance, interest_earned
"""Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.
    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    
    #######MISSING VALUE FOR INTEREST#########
    
    # ADD YOUR CODE HERE
    # Define a function for the Savings Account
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # Calculate interest earned
    # ADD YOUR CODE HERE
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE--->
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE--->line23
