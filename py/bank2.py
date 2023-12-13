class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def display_balance(self):
        print(f"Account Balance for {self.name} : RS{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into the account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from the account.")

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, name, initial_balance)

def main():
    account = None

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account = create_account()
        elif choice == '2':
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            else:
                print("Please create an account first.")
        elif choice == '3':
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Please create an account first.")
        elif choice == '4':
            if account:
                account.display_balance()
            else:
                print("Please create an account first.")
        elif choice == '5':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
