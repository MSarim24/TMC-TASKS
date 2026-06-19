import json

class BankAccount:
    def __init__(self, owner=""):
        self.owner = owner
        self.__balance = 0.0
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposit: {amount}")
        self.save_to_file("bank_account.json")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance ")
            return
        self.__balance -= amount
        self.__transactions.append(f"Withdrew: {amount}")
        self.save_to_file("bank_account.json")
    
    def display_balance(self):
        print("\n\n---DISPLAYING BALANCE---")
        print(f"{self.owner}: {self.__balance}")

    def display_transactions(self):
        print("\n\nTransaction History:")
        for transaction in self.__transactions:
            print(transaction)

    def save_to_file(self,filename):
        data = {
            "owner" : self.owner,
            "balance": self.__balance,
            "transactions" : self.__transactions
        }

        with open(filename,'w') as file:
            json.dump(data,file)

    def load_from_file(self,filename):
        with open(filename,'r') as file:
            data = json.load(file)
            self.owner =  data["owner"]
            self.__balance = data["balance"]
            self.__transactions = data["transactions"]


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
