class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"\n{self.name} made a deposit of ${amount}")
        self.display_user_balance()
        return self
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"\n{self.name} made a withdrawal of ${amount}")
        self.display_user_balance()
        return self
        
    def transfer(self, amount, other_user):
        self.make_withdrawal(amount)
        self.other_user=other_user
        other_user.make_deposit(amount)
        print(f"\n{self.name} transfered ${amount} to {other_user.name}")
        self.display_user_balance()
        other_user.display_user_balance()
        return self
    
    def display_user_balance(self):
        print(f"{self.name} has a balance of ${self.account_balance}")


russ = User("Russ", "russ@thisemail.moc")
ben = User("Ben", "ben@thisemail.moc") 
bob = User("Bob", "bob@thisemail.moc")

russ.make_deposit(100).make_deposit(75).make_deposit(50).make_withdrawal(50).transfer(25, bob)

ben.make_deposit(200).make_deposit(100).make_withdrawal(75)

bob.make_deposit(100).make_withdrawal(5).make_withdrawal(10).make_withdrawal(15)
