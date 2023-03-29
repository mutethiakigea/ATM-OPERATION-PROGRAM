class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

# Create a new BankAccount object with an initial balance of 0
account = BankAccount()

# Loop to prompt for transactions until the user chooses to quit
while True:
    # Prompt the user for a transaction
    transaction = input("Enter 'd' for deposit, 'w' for withdrawal, 'q' to quit: ")
    
    if transaction == "d":
        # Prompt the user for the amount to deposit
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        print(f"New balance: {account.get_balance()}")
    
    elif transaction == "w":
        # Prompt the user for the amount to withdraw
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print(f"New balance: {account.get_balance()}")
    
    elif transaction == "q":
        # Quit the loop
        break
    
    else:
        print("Invalid input")
