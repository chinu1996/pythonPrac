class Computer:
    def __init__(self):
        self.name = "Priyansh"
        self.age = 23

    def update(self):
        self.age = 25

        # self will point to that object for which this method is being called
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
if c1.compare(c2):
    print("They are same")
else:
    print("Different")

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

# Call update to change the age
c2.update()

# Now compare to see the result
if c1.compare(c2):
    print("They are same")
else:
    print("Different")


