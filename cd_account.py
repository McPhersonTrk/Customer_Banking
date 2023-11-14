"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
class Cd_Account(Account):
    def __init__(self, account_holder, balance, interest_rate, months):
            self.account_holder = account_holder
            self.balance = balance
            self.interest = interest_rate
            self.months = months
            balance = float(int(self.balance))
            account_holder = Cd_Account(Account(account_holder=""))
    def deposit(self, amount):
            self.balance += amount        
            print(f" Deposited ${amount}. New Balance is ${self.balance}")
    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount        
                print(f" Withdrew ${amount}. New Balance is ${self.balance}")
            else:
                print("Insufficient Funds")
            balance = float(int(self.balance))
            if self.balance.isdigit:
                    print(f"Account Balance is ${self.balance}, .2f")
            else:
                print("Error, entry must be a whole number. Please try again.")
            interest_rate = float(int(self.interest))
            interest_rate = float(int(input("Enter Interest Rate:")) / 100, .2f):
            if self.interest.isdigit:
                print(f"Account Balance is {interest_rate}, .2f%")
            else:
                print("Error, entry must be a whole number. Please try again.") 
    def calculate_interest(self):
            interest_earned = float(int((self.balance * self.interest * self.months) / 100))
            self.balance += interest_earned
            print(f"Interest earned: ${interest_earned}. New balance: ${self.balance}")
            return self.balance, interest_earned
    def create_cd_account(account_holder, balance, interest_rate, months):
            cd_account = Cd_Account(account_holder, balance, interest_rate, months)
            updated_balance, interest_earned = cd_account.calculate_interest()
            cd_account.set_balance(updated_balance)
            cd_account.set_interest(interest_earned)
            return updated_balance, interest_earned
            
    """Creates a CD account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.
    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # Calculate interest earned
    # ADD YOUR CODE HERE
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
