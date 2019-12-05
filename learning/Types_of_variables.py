class   Car:

    wheels = 4
    # This is a class variable

    def __init__(self):
        # These are the instance variables
        self.mileage = 10
        self.brand = "Mercerdes"


c1 = Car()
c2 = Car()
print(c1.mileage, c1.brand, c1.wheels)
print(c2.mileage, c2.brand, c2.wheels)

# Changing the instance variable
c1.mileage = 20


# Changing the class variable
Car.wheels = 5

print(c1.mileage, c1.brand, c1.wheels)
print(c2.mileage, c2.brand, c2.wheels)

