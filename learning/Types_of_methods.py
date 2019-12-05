class Student:

    school = "Apeejay school"

    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.marl2 = mark2

    def avg(self):
        # This is an instance method since it is using "self"
        return (self.mark1 + self.marl2)/2

    @classmethod
    def getSchool(cls):
        # This is a class method since it is using "cls"
          return cls.school

    @staticmethod
    def info():
        return "This is a static method.... "


s1 = Student(70, 90)
s2 = Student(80, 40)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

print(Student.info())
