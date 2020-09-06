class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
                
    def make_deposit(self, amount):
        self.balance += amount
        return self
        
    def make_withdrawal(self, amount):
        self.balance-= amount
        return self
        
    def transfer(self, amount, other_user):
        self.other_user=other_user
        self.make_withdrawal(amount)
        self.other_user.make_deposit(amount)
        return self
    
    def display_user_balance(self):
        print("\n" + "*"*20)
        print(self.name)
        print(f"Balance in account: ${self.balance}")
        print("\n" + "*"*20)
        return self

russ = User("Russ", "russ@thisemail.moc")
ben = User("Ben", "ben@thisemail.moc") 
bob = User("Bob", "bob@thisemail.moc")

russ.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()
ben.make_deposit(50).make_deposit(50).make_withdrawal(10).make_withdrawal(10).display_user_balance()
bob.make_deposit(500).make_withdrawal(50).make_withdrawal(50).make_withdrawal(10).display_user_balance()
russ.transfer(50, bob).display_user_balance()
bob.display_user_balance()