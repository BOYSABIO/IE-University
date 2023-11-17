import random

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.borrowed_amount = 0
        self.interest_rate = 0.1  # Initial interest rate
        self.investments = 0
        self.debt = 0

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
        print(f"Your current debt is: {self.debt}")

    def borrow_money(self):
        borrow_amount = int(input("How much would you like to borrow? "))
        self.interest_rate += 0.1
        interest_amount = int(borrow_amount * self.interest_rate)
        self.debt += borrow_amount + interest_amount
        print(f"You borrowed {borrow_amount} with an interest rate of {self.interest_rate}")
        self.balance += borrow_amount

    def make_investment(self, amount):
        if amount > self.balance:
            borrow_option = input("You have insufficient funds. Would you like to borrow money? (yes/no) ").lower()
            if borrow_option == 'yes':
                self.borrow_money()
            else:
                print("Investment canceled due to insufficient funds.")
                return

        self.investments += 1
        investment_rate = random.uniform(-1, 1)
        investment_return = amount * investment_rate
        self.balance += investment_return
        print(f"Your investment has a rate of {investment_rate}")
        print(f"Your investment has a return of {investment_return}")
        print(f"Your new balance is: {self.balance}")

        remaining_investments = 10 - (self.investments % 10)
        if remaining_investments > 0:
            print(f"You have {remaining_investments} investment(s) remaining before you must pay off your debt.")
        else:
            print("Warning: You have reached the maximum number of allowed investments. Time to pay off your debt.")

    def update_interest_and_debt(self):
        if self.debt > 0:
            self.debt += int(self.debt * self.interest_rate)
            print(f"Your debt has increased to {self.debt}")

    def check_bankruptcy(self):
        if self.balance < 0:
            print("You failed to make the money back. You are now bankrupt.")
            print(f"List of your investments/choices: {self.investments}")
            exit()
    
    def pay_off_debt(self):
        if self.debt == 0:
            print("You don't have any outstanding debt.")
            return

        print(f"Your current account balance is {self.balance}.")
        print(f"Your current debt is {self.debt}.")
        pay_off_amount = int(input("How much would you like to pay off? "))

        if pay_off_amount <= self.balance:
            self.debt -= pay_off_amount
            self.balance -= pay_off_amount
            print(f"You paid off {pay_off_amount}. Remaining debt: {self.debt}")
            self.investments = 0
        else:
            print("You do not have sufficient funds to pay off that amount.")

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
        print("5. Pay Debt")
        print("6. Exit")

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
            account.make_investment(amount)
            account.update_interest_and_debt()
            account.check_bankruptcy()
            
            # Check if the user has reached the maximum number of investments
            if account.investments % 10 == 0:
                print("You have reached the maximum number of allowed investments. Time to pay off your debt.")
                while account.debt > 0:
                    pay_off_option = input("Would you like to pay off your debt? (yes/no) ").lower()
                    if pay_off_option == 'yes':
                        pay_off_amount = int(input("How much would you like to pay off? "))
                        if pay_off_amount <= account.balance:
                            account.debt -= pay_off_amount
                            account.balance -= pay_off_amount
                            print(f"You paid off {pay_off_amount}. Remaining debt: {account.debt}")
                        else:
                            print("You do not have sufficient funds to pay off that amount.")
                    else:
                        print("You must pay off your debt before continuing.")
                        account.check_bankruptcy()
        elif choice == 5:
            account.pay_off_debt()
        elif choice == 6:
            print("Thank you for using our bank!")
            print(f"Your final balance is: {account.balance}")
            break
        else:
            print("Invalid choice")
main()

# Fix invest feature
# - Needs to end the game after 10 investments