# Student.py
class Student:
    def __init__(self, name, student_id, year):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.is_attending = True
        self.major = None
        self.remaining_school_break_terms = 7
        self.current_semester_remaining_credits = 18
        self.current_enrolling_courses = []

    def sign_up_course(Self, course):
        if (self.is_attending):
            if (self.current_semester_remaining_credits > course.Credit     # 학점이 남을 때
                and course.student_count > 0                                # 해당 교과목 인원이 남을 때
                and course.available_year <= self.year):                    # 해당 교과목 수강 가능 학년일 때
                self.current_semester_remaining_credits -= course.Credit
                self.current_enrolling_courses.append(course)

    def take_school_break(Self):
        if (self.is_attending): 
            if (self.remaining_school_break_terms > 0):
                self.remaining_school_break_terms -= 1
                self.is_attending = False
                self.current_enrolling_courses.clear()
                self.current_semester_remaining_credits = 0

    def apply_major(self, major):
        if (self.major == None and self.is_attending):                      # 현재 전공이 없으며 재학 중일 때
            self.major = major

# main.py
karen = Student("Karen", "2020105689", 1
karen.take_school_break()
if (karen.is_attending):
    print(karen.name +" is attending school")
else:
    print(karen.name + " is taking a school break!")

karen.apply_major("SWC")
if (karen.major != None):
    print(karen.name + " is " + karen.major)
else:
    print(karen.name + " has no")

# print("Name: {}\nStudent ID: {}\nYear: {}".format(karen.name, karen.student_id, karen.year))
# print("Is Attending School?: {}\nMajor: {}".format(karen.is_attending, karen.major))
# print("Remaining School Break: {}".format(karen.remaining_school_break_terms))
# print("Current Semester Remaining Credits: {}".format(karen.current_semester_remaining_credits))