

class Account:
    """
    An account of the current monetary holdings.
    Must be initialized with current holdings.

    Account(starting_holdings)

    Methods:

    add_transaction(sum)
    take a number and add it to holdings. 
    The number can be negative to describe 
    spent money.

    get()
    Will return current holdings in the account.
    """
    def __init__(self, starting_holdings):
        if type(float(starting_holdings)) == float():
            self.account_holding = float(starting_holdings)
        else:
            print("Error: Starting holdings must be a float or int...")

    def add_transaction(self, sum):
        if type(float(sum)) == float():
            self.account_holding += float(sum)
        else:
            print("Error: sum must be a float or int...")

    def get(self):
        return self.account_holding