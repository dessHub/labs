class BankAccount(object):
    def withdraw():
        pass

    def deposit():
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        elif (self.balance - amount) < 500:
            return "Cannot withdraw beyond the minimum account balance"
        else:
            self.balance -= amount
        return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif self.balance < amount:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            return self.balance
