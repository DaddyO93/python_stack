class BankAccount:
    def __init__(self, int_rate=.01, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += float(amount)
        return self

    def withdrawal(self, amount):
        self.balance -= float(amount)
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        self.display_account_info
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self


user1 = BankAccount()
user2 = BankAccount()

user1.deposit(100).deposit(200).deposit(50).withdrawal(25).yield_interest().display_account_info()
user2.deposit(200).deposit(200).withdrawal(5).withdrawal(5).withdrawal(5).withdrawal(5).yield_interest().display_account_info()