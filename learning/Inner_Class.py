class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.laptop = self.Laptop(0,0,0)

    def show(self):
        print(self.name, self.roll)

    class Laptop:
        # This is a class inside a class

        def __init__(self, brand, CPU, ram):
            self.brand = brand
            self.CPU = CPU
            self.ram = ram

        def show(self):
            print(self.brand, self.CPU, self.ram)

#outer class's object
s1 = Student("Priyansh", 25)
s2 = Student("Das", 53)

#inner class object instantiate
s1.laptop.__init__('Lenovo', 'Core i5', 4)
s2.laptop.__init__('Dell', 'Dual Core', 8)


s1.show()
s1.laptop.show()
s2.show()
s2.laptop.show()