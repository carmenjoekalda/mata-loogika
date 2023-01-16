"""Return a."""


class Student:
    """Return a."""

    def __init__(self, name: str):
        """Return a."""
        self.name = name
        self.__id = None
        self.grades = []

    def set_id(self, id: int):
        """Return a."""
        if self.__id is None:
            self.__id = id
        else:
            pass

    def get_id(self) -> int:
        """Return a."""
        return self.__id

    def add_grade(self, grade):
        """Return a."""
        self.grades.append(grade)

    def get_grades(self):
        """Return a."""
        return self.grades

    def get_average_grade(self):
        """Return a."""
        if len(self.grades):
            total = 0
            for grade in self.grades:
                total += grade[1]
            average = total / len(self.grades)
            return average
        else:
            return int(-1)

    def __repr__(self) -> str:
        """Return a."""
        return self.name
