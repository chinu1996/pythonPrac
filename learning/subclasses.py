class Employee:

    # this is the base class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Manager(Employee):

    # Manager class will inherit employees class and will also have list of employees working under the manager

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def __repr__(self):
        return "Manager('{}','{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} is an object".format(self.fullname())


emp1 = Employee('Piyush', 'something', 30000)
emp2 = Employee('yash', 'ui/ux', 15000)

mgr1 = Manager('kartik', 'agarwal', 250000, [emp1])

print(mgr1.fullname)
print(mgr1.print_emps())

mgr1.add_emp(emp2)
print(mgr1.print_emps())

# now lets use some magic methods


print(repr(mgr1))
# OR
print(mgr1.__repr__())

print(str(mgr1))