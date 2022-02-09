from UsersWithBankAccounts import BankAccount


class User:
#
    bank_name = "First National Dojo"
#
    def __init__(self , name):
        self.name = name
        self.account = {
            "checking": BankAccount(1.02, 1000),
            "saving": BankAccount(1.02, 2000)
        }

##function
    def display_user_balance(self):
        print(f"Welcome {self.name} your  checking balance is: {self.account['checking'].balance}")
        print(f"Welcome {self.name} your saving balance is: {self.account['saving'].balance}")

"""##withdraw
    def make_withdrawal(self):
        self.account.withdrawal()
        return self
##deposit
    def make_deposit(self):
        self.account.deposit()
        return self"""
##transfer
"""    def transfer_money(self, other_user, amount):
        self.make_withdrawal (amount)
        other_user.make_deposit (amount)
        return self"""



## user info
User1 = User("Guido van Rossum")
User2 = User("Monty Python")
User3 = User("John Heine")
## print transfer
# User1.transfer_money(User3,100)
# print(User1)
# User1.make_deposit(100).make_deposit(15).make_deposit(35).make_withdrawal(150).display_user_balance()
# # print(User2)
# User2.make_withdrawal(2500).make_deposit(500).make_withdrawal(250).make_deposit(5).display_user_balance()
# # print(User3)
# User3.make_withdrawal(900).make_deposit(1000).make_withdrawal(500).make_withdrawal(599).display_user_balance()
##Transaction##
User1.display_user_balance()
User1.account['checking'].deposit(100)
User1.account['saving'].withdraw(400)
User1.display_user_balance()