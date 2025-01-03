class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def __str__(self):
        return self.name + " " + self.balance

class Bank:
    def __init__(self):
        self.accounts = dict()
        self.file_name = "accounts.txt"
        self.number = 1
    def create_account(self, name, initial_deposit):
        if not isinstance(name, str):
            raise ValueError("Name should be string")
        if not isinstance(initial_deposit, (int, float)):
            raise ValueError("Deposit should be a number")
        
        acc_number = self.number
        self.number += 1
        self.accounts[acc_number] = Account(acc_number, name, initial_deposit)

        self.save_to_file(self.accounts[acc_number])

    def view_account(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer!")
        
        return self.accounts[account_number]
    
    def deposit(self, account_number, amount):
        self.accounts[account_number].balance += amount

        self.save_to_file(self.account[account_number])


    def withdraw(self, account_number, amount):
        pass

    def save_to_file(self, account):
        pass

    def load_from_file(self):
        pass