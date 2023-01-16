"""Return a."""

import random
from course import Course
from student import Student


class School:
    """Return a."""

    def __init__(self, name):
        """Return a."""
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course: Course):
        """Return a."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Return a."""
        if student not in self.students:
            id = random.randint(1, 101)
            while any(student.get_id() == id for student in self.students):
                id = random.randint(1, 101)
            student.set_id(id)
            self.students.append(student)

    def add_student_grade(self, student, course, grade: int):
        """Return a."""
        if student in self.students and course in self.courses:
            student.add_grade(tuple([course, grade]))
            course.add_grades(tuple([student, grade]))

    def get_students(self):
        """Return a."""
        return self.students

    def get_courses(self):
        """Return a."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[str]:
        """Return a."""
        for i in range(len(self.students) - 1):
            if self.students[i].get_average_grade() < self.students[i + 1].get_average_grade():
                help = self.students[i]
                self.students[i] = self.students[i + 1]
                self.students[i + 1] = help
        return self.students
