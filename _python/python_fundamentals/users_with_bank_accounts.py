class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, balance, amount):
        self.balance = balance + amount
        return self, self.balance

    def withdrawal(self, balance, amount):
        self.balance = balance - amount
        return self, self.balance

    def yield_interest(self, balance):
        self.balance = (balance * self.int_rate) + balance
        return self, self.balance


class User:
    def __init__(self, account_info):
        self.account_info = account_info
        self.name = account_info.get("Name")
        self.email = account_info.get("Email Address")
        self.account = BankAccount(int_rate=0.02, balance=0)
                
    def make_deposit(self, amount, account_num):
        self.account.deposit(amount, self.account_info.get(account_num))
        self.account_info.update({account_num:self.account.balance})
        return self
        
    def make_withdrawal(self, amount, account_num):
        self.account.withdrawal(amount, self.account_info.get(account_num))
        self.account_info.update({account_num:self.account.balance})
        return self
    
    def get_interest(self, account_num):
        balance = self.account_info.get(account_num)
        self.account.yield_interest(balance)
        self.account_info.update({account_num:self.account.balance})
        return self
        
    def transfer(self, amount, other_user, origin_account_num, receiving_account_num):
        self.other_user=other_user
        self.make_withdrawal(amount, origin_account_num)
        self.other_user.make_deposit(amount, receiving_account_num)
        return self
    
    def display_user_balance(self, account_num):
        print("\n" + "*"*20)
        print(self.name)
        print(f"Balance on account number {account_num}: ${self.account_info.get(account_num)}")
        print("\n" + "*"*20)
        return self


russ = User({"Name": "Russ", "Email Address":"russ@thisemail.moc","1":10, "2":20, "3":30})
ben = User({"Name":"Ben", "Email Address":"ben@thisemail.moc", "1":0, "2":0}) 
bob = User({"Name":"Bob", "Email Address":"bob@thisemail.moc", "1":0, "2":0, "3":0, "4":0})

russ.make_deposit(50, "1").make_deposit(100, "2").display_user_balance("1").display_user_balance("2").transfer(50, bob, "1", "1").display_user_balance("1")
bob.display_user_balance("1").get_interest("1").display_user_balance("1")