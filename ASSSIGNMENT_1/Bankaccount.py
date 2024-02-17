#hs759
#Name: Harshitha Saripalli
#Date of Submission: 02/17/2024
# Task 2 (50 Points)
# This task is divided into sub parts.
# Part 1: Bank Account Class
# 1. Create BankAccount class with following attributes and methods:
# Attributes:
        # account_number: An integer.
        # balance: A float. 
        # account_holder: A string.
class bankaccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    # Methods:
    # deposit(self, amount): Adds the amount to current balance.
    def get_deposit(self,amount) :   
        self.balance += amount 
        print(self.balance)
    # withdraw(self, amount): Subtracts the amount from current balance.
    def get_withdrawl(self,amount) :
        self.balance -= amount
        print(self.balance)
    # get_balance(self): Returns the current balance.
    def get_balance(self):
        print(self.balance)
 # call the BankAccount class by creating an instance of it and pass in the values.
 # pass the balance as 1000, give a account number and account holder name    
 # call deposit() method, withdraw() method by passing deposit amount as 200, withdraw amount as 700
 # then print the total balance of the account (call the get_balance() method)     
p = bankaccount(9010011077, 1000.00, "rama")
p.get_deposit(200)
p.get_withdrawl(700)
p.get_balance()


# Part 2: Checking Account Class
# 1. Create CheckingAccount class that inherits from BankAccount
class CheckingAccount(bankaccount) :
   # 2. Add the following attributes and methods to the CheckingAccount class:
   # Attributes:
      # transaction_fees: A float, transaction fees charged for each transaction.
    def __init__(self, account_number, balance, account_holder, transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees
     # Methods:
        # apply_transaction_fees(self): Subtracts the transaction fees from current balance.
    def  apply_transaction_fees(self) :
        self.balance  -= self.transaction_fees
        print(self.balance)
# call CheckingAccount class by creating an instance of it
# pass the transaction fees as 34.50 and call the apply_transaction_fees() method
# then print the total balance of the account (call the get_balance() method)
q= CheckingAccount(p.account_number, p.balance, p.account_holder, 34.50)
q.apply_transaction_fees()


# Part 3: savings account class
# 1. Create SavingsAccount class that inherits from BankAccount.
class SavingsAccount(bankaccount):
    # 2. Add the following attributes and methods to the SavingsAccount class:
    # Attributes:
        # interest_rate: A float
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate
    # Methods:
        # calculate_interest(self): Calculates and adds the interest to the current balance.
    def calculate_interest_rate(self):
        intrest = self.balance * self.interest_rate
        return self.balance + intrest
# call SavingsAccount class by creating an instance of it
# pass the interest rate as 0.12 and call the calculate_interest() method
# then print the total balance of the account (call the get_balance() method)   
r= SavingsAccount(9010011077, p.balance, "rama", 0.12)
print(r.calculate_interest_rate())
