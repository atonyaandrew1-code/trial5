from datetime import datetime

class BankAccount:
    def __init__(self,owner,number,balance):
        self.owner = owner
        self.number =number
        self.__balance =balance

    def deposit(self,amount):
        self.__balance +=amount
        print(f"Deposited:{amount}")

    def get_balance(self):
        return self.__balance

    def print_receipt(self):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        print("-"*20)
        print("Bank reciept")
        print(f" Date:{dt_string}")
        print("-"*20)
        print(f"Account Number:{self.number}")
        print(f"Account Owner: {self.owner}")
        print(f"Total Balance: {self.__balance}")
        print("_"*20)

acc = BankAccount(input("enter your name: "),input("account no: "),int(input("enter initial balance: ")))
acc.deposit(int(input("How much do you want to deposit? ")))
acc.print_receipt()
