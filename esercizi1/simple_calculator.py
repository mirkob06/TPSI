class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


num1 = 10
num2 = 5

print(f"{num1} + {num2} = {Calculator.add(num1, num2)}")
print(f"{num1} - {num2} = {Calculator.subtract(num1, num2)}")
print(f"{num1} * {num2} = {Calculator.multiply(num1, num2)}")
print(f"{num1} / {num2} = {Calculator.divide(num1, num2)}")
