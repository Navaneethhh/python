class Customer:
    def getdata(self, name, accno, acctype, balance):
        self.name = name
        self.accno = accno
        self.acctype = acctype
        self.balance = balance

    def displaycustomer(self):
        print("Customer name:", self.name)
        print("Account number:", self.accno)
        print("Account type:", self.acctype)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient balance")
        else:
            self.balance -= amount

ch = 0

while ch != 5:
    print("1. New customer")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj = Customer()
        n = input("Enter your name: ")
        no = int(input("Enter acc no: "))
        t = input("Enter acc type: ")
        b = int(input("Enter the initial balance: "))
        obj.getdata(n, no, t, b)
    elif ch == 2:
        if obj is not None:
            b = int(input("Enter the amount to deposit: "))
            obj.deposit(b)
        else:
            print("Please create a customer first.")
    elif ch == 3:
        if obj is not None:
            b = int(input("Enter the amount to withdraw: "))
            obj.withdraw(b)
        else:
            print("Please create a customer first.")
    elif ch == 4:
        if obj is not None:
            obj.displaycustomer()
        else:
            print("Please create a customer first.")
    elif ch == 5:
        print("Exiting the program.")
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
