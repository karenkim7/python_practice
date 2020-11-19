# Student.py
class Student:
    def __init__(self, name, student_id, year):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.is_attending = True
        self.major = "SWC"
        self.remaining_school_break = 6
        self.current_semester_remaining_credits = 18

karen = Student("Karen", "2020105689", "1")
print("Name: {}\nStudent ID: {}\nYear: {}".format(karen.name, karen.student_id, karen.year))
print("Is Attending School?: {}\nMajor: {}".format(karen.is_attending, karen.major))
print("Remaining School Break: {}".format(karen.remaining_school_break))
print("Current Semester Remaining Credits: {}".format(karen.current_semester_remaining_credits))