#bank_account.py

class BankAccount:

    def __init__(self, initial_balance=0.00):
        self.account_balance = float(initial_balance)


    def deposit(self, amount):
        '''This adds to the balance'''
        self.account_balance += amount
        

    def withdraw(self, amount):
        '''This subtracts the balance'''
        if (self.account_balance - amount) < 0:
            return False
        else:    
            self.account_balance -= amount
            return True

    def display_balance(self):
        '''This displays the current balance'''
        print(f"Current Balance: ${self.account_balance:.2f}")