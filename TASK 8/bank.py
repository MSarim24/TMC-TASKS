import json

class BankAccount:
    def __init__(self, owner=""):
        self.owner = owner
        self.balance = 0.0
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        self.save_to_file("bank_account.json") 
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        self.save_to_file("bank_account.json") 

    
    def display_balance(self):
        print(f"Owner:{self.owner}\nCurrent Balance: {self.balance}")
    
    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    
    def save_to_file(self, filename):
        data = {
            "owner": self.owner,
            "balance": self.balance,
            "transactions": self.transactions
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
    
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.owner = data["owner"]
            self.balance = data["balance"]
            self.transactions = data["transactions"]

account = BankAccount("John Doe")
account.deposit(100)
account.withdraw(30)
account.display_balance()
account.display_transactions()
new_account = BankAccount()
new_account.load_from_file("bank_account.json")
new_account.deposit(50)
new_account.deposit(55)
new_account.withdraw(20)
new_account.display_balance()
new_account.display_transactions()
