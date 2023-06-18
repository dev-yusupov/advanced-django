
class Operation:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

class Addition(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def __str__(self):
        return str(self.num1 + self.num2)

class Subtraction(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def __str__(self):
        return str(self.num1 - self.num2)

class Multiply(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def __str__(self):
        return str(self.num1 * self.num2)

class Division(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def __str__(self):
        return str(self.num1 / self.num2)

