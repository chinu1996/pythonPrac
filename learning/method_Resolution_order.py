class A:
    def __init__(self):
        print("in init of A")

    def feature1(self):
        print("This is feature 1-a")

    def feature2(self):
        print("This is feature 2")


class B:
    def __init__(self):
        print("in init of B")

    def feature1(self):
        # this method is also there in the class A
        print("This is feature 1-B")


class C(A, B): # interchange A and B and see what happens
    # It inherits from left to right so super() will point towards init of A
    def __init__(self):
        super().__init__()
        print("in init of C")


a1 = C()
a1.feature1() # this will call the feature in class A and not in class B since it is left to right
