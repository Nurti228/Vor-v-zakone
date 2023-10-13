class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _combine_balance(self, other_account):
        self._balance += other_account._balance

bank1 = Bank("Alice", 100)
bank2 = Bank("Bob", 100)

print("Баланс до объединения:")
print("Банк 1:", bank1._balance)
print("Банк 2:", bank2._balance)

# Вызываем метод для объединения баланса
bank1._combine_balance(bank2)

print("\nБаланс после объединения:")
print("Банк 1:", bank1._balance)
print("Банк 2:", bank2._balance)