class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject

    def printNameSubject(self):
        print("Student:", self.fname, self.lname, "  |  Currently studying ", self.subject)

class Teacher(Person):
    def __init__(self, fname, lname, course):
        super().__init__(fname, lname)
        self.course = course

    def printNameCourse(self):
        print("Teacher:", self.fname, self.lname, "  |  Teacher in the course:", self.course)

