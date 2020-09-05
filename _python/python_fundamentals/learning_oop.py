class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def transfer(self, amount, other_user):
        self.make_withdrawal(amount)
        self.other_user=other_user
        other_user.make_deposit(amount)


russ = User("Russ", "russ@thisemail.moc")
ben = User("Ben", "ben@thisemail.moc") 
bob = User("Bob", "bob@thisemail.moc")

russ.make_deposit(100)
print(f"\n{russ.name} made a deposit")
print(f"The account balance for {russ.name} is ${russ.account_balance}")

russ.make_deposit(75)
print(f"\n{russ.name} made a deposit")
print(f"The account balance for {russ.name} is ${russ.account_balance}")

russ.make_deposit(50)
print(f"\n{russ.name} made a deposit")
print(f"The account balance for {russ.name} is ${russ.account_balance}")

russ.make_withdrawal(50)
print(f"\n{russ.name} made a withdrawal")
print(f"The new balance for {russ.name} is ${russ.account_balance}")


ben.make_deposit(200)
print(f"\n{ben.name} made a deposit")
print(f"The account balance for {ben.name} is ${ben.account_balance}")
ben.make_deposit(100)
print(f"\n{ben.name} made a deposit")
print(f"The account balance for {ben.name} is ${ben.account_balance}")

ben.make_withdrawal(75)
print(f"\n{ben.name} made a withdrawal")
print(f"The new balance for {ben.name} is ${ben.account_balance}")


bob.make_deposit(100)
print(f"\n{bob.name} made a deposit")
print(f"The account balance for {bob.name} is ${bob.account_balance}")

bob.make_withdrawal(5)
print(f"\n{bob.name} made a withdrawal")
print(f"The new balance for {bob.name} is ${bob.account_balance}")

bob.make_withdrawal(10)
print(f"\n{bob.name} made a withdrawal")
print(f"The new balance for {bob.name} is ${bob.account_balance}")

bob.make_withdrawal(15)
print(f"\n{bob.name} made a withdrawal")
print(f"The new balance for {bob.name} is ${bob.account_balance}")


russ.transfer(25, bob)
print(f"\n{russ.name} transfered money into {bob.name}'s' account.")
print(f"{bob.name} has a new balance of ${bob.account_balance}")
print(f"{russ.name} has a new balance of ${russ.account_balance}")