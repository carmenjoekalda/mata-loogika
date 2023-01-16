"""Return a."""


class Course:
    """Return a."""

    def __init__(self, name: str):
        """Return a."""
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        """Return a."""
        self.grades.append(grade)

    def get_grades(self):
        """Return a."""
        return self.grades

    def get_average_grade(self):
        """Return a."""
        all_grades = 0
        if len(self.grades) == 0:
            return -1
        else:
            for grade in self.grades:
                all_grades += grade[1]
            average_grade = all_grades / len(self.grades)
            return average_grade

    def __repr__(self):
        """Return a."""
        return self.name
