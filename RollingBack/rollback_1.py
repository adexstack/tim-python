class Account:

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}. ", end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn")
            return amount
        else:
            print("The amount must be greater than zero and no more than your account balance")

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance}")


if __name__ == '__main__':
    john = Account("John")
    john.deposit(10.10)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()  # Balance shown is Balance on account John is 9.999999999999998 (Not acceptable). See improved in rollback_keep.py
