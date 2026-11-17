class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []  

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposit: +{amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append(f"Withdraw: -{amount}")
            print("Withdraw successful!")

    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance}")

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
            return
        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item}")

    def transfer(self, other, amount):
        if other is self:
            print("Can't transfer to the same account!")
        elif amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            other.balance += amount
            self.history.append(f"Transfer to {other.name}: -{amount}")
            other.history.append(f"Transfer from {self.name}: +{amount}")
            print("Transfer successful!")


def read_amount(prompt="Amount: "):
    try:
        return float(input(prompt))
    except ValueError:
        return -1  


def main():
    accounts = {}

    def get_account(prompt="Account name: "):
        name = input(prompt).strip()
        acc = accounts.get(name)
        if not acc:
            print("Account not found!")
        return acc

    menu = """
===== Bank System =====
1. Create account
2. Deposit
3. Withdraw
4. Show balance
5. Show history
6. Transfer
7. Exit
"""
    while True:
        print(menu)
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            if not name or name in accounts:
                print("Invalid or existing name!")
                continue
            initial = read_amount("Initial balance: ")
            if initial < 0:
                print("Invalid amount!")
                continue
            accounts[name] = Bank(name, initial)
            print("Account created!")
        elif choice in ("2", "3", "4", "5"):
            acc = get_account()
            if not acc:
                continue
            if choice == "2":
                acc.deposit(read_amount())
            elif choice == "3":
                acc.withdraw(read_amount())
            elif choice == "4":
                acc.show_balance()
            else:
                acc.show_history()
        elif choice == "6":
            sender = get_account("From account: ")
            receiver = get_account("To account: ") if sender else None
            if sender and receiver:
                sender.transfer(receiver, read_amount())
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()