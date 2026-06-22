class BankAccount:

    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully!")
        else:
            print("Invalid amount!")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully!")

    # Check Balance
    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

    # Display Account Details
    def display_account(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.acc_no)
        print("Account Holder :", self.name)
        print("Account Type   :", self.acc_type)
        print("Balance        :", self.balance)
        print("---------------------------")


# Dictionary to store accounts
accounts = {}


# Create Account
def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current/Student): ")

    account = BankAccount(acc_no, name, acc_type)
    accounts[acc_no] = account

    print("Account Created Successfully!")


# Deposit Money
def deposit_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Amount to Deposit: "))
        accounts[acc_no].deposit(amount)
    else:
        print("Account Not Found!")


# Withdraw Money
def withdraw_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        accounts[acc_no].withdraw(amount)
    else:
        print("Account Not Found!")


# Check Balance
def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        accounts[acc_no].check_balance()
    else:
        print("Account Not Found!")


# Display All Accounts
def display_all_accounts():

    if not accounts:
        print("No Accounts Available!")
        return

    for account in accounts.values():
        account.display_account()


# Main Menu
while True:

    print("\n====== MINI BANKING SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        display_all_accounts()

    elif choice == "6":
        print("Thank You For Using Mini Banking System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")