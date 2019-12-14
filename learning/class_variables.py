class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.fullname = self.first + self.last

    def promotion(self):
        new_pay =  (self.pay * self.raise_amount)
        self.pay = new_pay
        return  new_pay

    @classmethod
    def increase_raise_amount(cls, amount):
        cls.raise_amount = amount

emp1 = Employee('Priyansh', 'das', 60000)
emp2 = Employee('Test', 'user', 50000)
print(emp1.pay)
print(emp1.promotion())
#
# print(emp2.pay)
# emp2.raise_amount = 2
# print(emp2.promotion())
# print(emp2.pay)

# print(emp1.__dict__)
# print(emp2.__dict__)


Employee.increase_raise_amount(1.50)
print(emp1.pay)
print(emp1.promotion())

# print(emp2.pay)
# emp2.raise_amount = 2
# print(emp2.promotion())
# print(emp2.pay)

print(emp1.__dict__)
print(emp2.__dict__)
