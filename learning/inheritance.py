class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class B(A):

    def feature3(self):
        print("This is feature 3")


class C:

    def feature4(self):
        print("This is feature 4")


class D(B,C):
    # This is an example of multiple inheritance
    def feature5(self):
        print("this is feature 5")


a1 = A() # This is an object of class A
a1.feature1() # Calling instance method

b1 = B() # This is an object of class B which inherited everything from class A
b1.feature2()
b1.feature3()

d1 = D() # This is an object of class D which inherited everything from class B and class C
d1.feature1()