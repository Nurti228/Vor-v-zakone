class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def truediv(self):
        if self.num2 == 0:
            return "Division by zero is not allowed."
        else:
            return self.num1 / self.num2

calculator = Calculator(10, 5)

print("\nРезультаты операций:")
print("Сложение:", calculator.add())
print("Вычитание:", calculator.sub())
print("Умножение:", calculator.mul())
print("Деление:", calculator.truediv())