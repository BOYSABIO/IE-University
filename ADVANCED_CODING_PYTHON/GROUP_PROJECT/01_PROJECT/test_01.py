import random

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.borrowed_amount = 0
        self.interest_rate = 0.1  # Initial interest rate
        self.investments = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You do not have enough money to withdraw that amount")
        else:
            self.balance -= amount
            print(f"Your new balance is: {self.balance}")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def borrow_money(self):
        borrow_amount = int(input("How much would you like to borrow? "))
        self.borrowed_amount += borrow_amount
        print(f"You borrowed {borrow_amount} with an interest rate of {self.interest_rate}")
        self.balance += borrow_amount

    def invest(self, amount):
        if amount > self.balance:
            borrow_option = input("You have insufficient funds. Would you like to borrow money? (yes/no) ").lower()
            if borrow_option == 'yes':
                self.borrow_money()
            else:
                print("Investment canceled due to insufficient funds.")
                return

        #self.balance -= amount
        self.investments += 1
        investment_rate = random.uniform(-1, 1)
        investment_return = amount * investment_rate
        self.balance = self.borrowed_amount + amount + investment_return

        print(f"Your investment has a rate of {investment_rate}")
        print(f"Your investment has a return of {investment_return}")
        print(f"Your new balance is: {self.balance}") #Indicate the amount borrowed

        self.balance += investment_return

        # Check if the user needs to borrow money
        if self.balance < 0 and self.borrowed_amount == 0:
            borrow_option = input("You have insufficient funds. Would you like to borrow money? (yes/no) ").lower()
            if borrow_option == 'yes':
                self.borrow_money()

    def update_interest_rate(self):
        # Increase interest rate after each investment
        if self.investments % 10 == 0:
            self.interest_rate += 0.1
            print(f"Your interest rate has increased to {self.interest_rate}")

    def check_bankruptcy(self):
        if self.balance < 0:
            print("You failed to make the money back. You are now bankrupt.")
            print(f"List of your investments/choices: {self.investments}")
            exit()

def main():
    name = input("What is your name? ")
    balance = 0
    account_number = random.randint(100000, 999999)
    account = BankAccount(name, balance, account_number)
    print(f"Welcome {name} to your bank account")
    print(f"Your account number is: {account_number}")

    while True:
        print("What would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Invest")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            amount = int(input("How much would you like to deposit? "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("How much would you like to withdraw? "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            amount = int(input("How much would you like to invest? ")) #Also plan to allow shorting
            account.invest(amount)
            account.update_interest_rate()
            account.check_bankruptcy()
        elif choice == 5:
            print("Thank you for using our bank!")
            print(f"Your final balance is: {account.balance}")
            break
        else:
            print("Invalid choice")
main()
