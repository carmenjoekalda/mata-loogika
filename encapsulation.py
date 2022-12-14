"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, id: int, status = "Active"):
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_status(self, status):
        if status == "Active" or status == "Expelled" or status == "Finished" or status == "Inactive":
            self.__status = status
        else:
            pass

    def get_status(self):
        return self.__status





