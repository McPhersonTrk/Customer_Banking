# Import the create_cd_account and create_savings_account functions
from Account import Account
from cd_account import Cd_Account
from savings_account import SavingsAccount

Class Savings_Account:
def create_savings_account(Savings):
    def __init__(self, savings_balance, savings_interest, savings_maturity):
        self.savings_balance = savings_balance
        self.savings_interest = savings_interest
        self.savings_maturity = savings_maturity
        savings_balance = float(input("Please enter the starting balance: ,.2f "))
        savings_interest = float(input("Please enter the interest rate: %."))
        savings_maturity = float(input("Please enter the term in months: "))
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
            


# ADD YOUR CODE HERE

# Define the main function

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
