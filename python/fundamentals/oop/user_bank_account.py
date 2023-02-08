class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.03, balance=0)

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, sep="\n")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} is now enrolled as a rewards member and has {self.gold_card_points} gold card points!")
        elif self.is_rewards_member == True:
            print(f"{self.first_name} is already enrolled as a rewards member.")
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount > 0:
            self.gold_card_points = self.gold_card_points - amount
            print(f"{self.first_name} now has a balance of {self.gold_card_points} gold card points.")
        elif self.gold_card_points - amount < 0:
            print(f"{self.first_name} has a balance of {self.gold_card_points} gold card points and no points to spend.")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your balance is now at ${self.balance}.")
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance = self.balance - amount
            print(f"Your balance is now at ${self.balance}.")
        elif self.balance - amount < 0:
            self.balance = self.balance - 5
            print(f"Insufficient funds: Charging a $5 fee.")
            print(f"Your balance is now at ${self.balance}.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"Your balance is now at ${self.balance}.")
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            print(f"Account balance: ${account.balance}", f"Interest rate: ${account.int_rate}", sep="\n")


victoria = User("Victoria","Smuk","vicsmuk@icloud.com",22)
felix = User("Felix", "S", "felix@gmail.com", 25)
ella = User("Ella", "A", "ella@gmail.com", 20)

victoria.display_user_balance().make_deposit(200)