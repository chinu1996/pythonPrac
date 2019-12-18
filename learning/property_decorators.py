class Employee:

    # this is the base class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting the name")
        self.first = None
        self.last = None


emp1 = Employee("priyansh", "das", 15000)

print(emp1.email)
print(emp1.fullname)

emp1.fullname = "Charlie Sheen"

print(emp1.email)
print(emp1.fullname)

del emp1.fullname
print(emp1.email)
print(emp1.fullname)