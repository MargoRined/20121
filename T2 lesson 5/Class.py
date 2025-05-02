class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.course = dict()

    def add_offering(self, course_teamplate):
        self.course[course_teamplate.code] = course_teamplate

class CourseTemplate:
    def __init__(self, title, code, credits):
        self.title = title
        self.code = code
        self.credits = credits
        self.offerings = set()

    def add_offering(self, offering):
        self.offerings.add(offering)

class CourseOffering:
    def __init__(self, year):
        self.year = year
        self.student = set()

    def enrol(self, student):
        self.students.add(student)
        student.offerings.add(self)

class Student:
    def __init__(self, name, student_no):
        self.name = name
        self.student_no = student_no
        self.offerings = set()

    def enrol(self, offering):
        offering.enrol(self)