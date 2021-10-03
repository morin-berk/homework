import datetime
from typing import Optional


class Homework:
    """
    This is a simple model of a homework. Additionally to arguments,
    creates datetime.datetime.today() object, marking
    when Homework is created.
    :param text: task
    :param deadline: int > 0, responsible for generating
    datetime.timedelta object`s days
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        if deadline < 0:
            self.deadline = datetime.timedelta(days=0)
        else:
            self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        """Checks if a homework has timed out.
        Creates today`s datetime obj, compares it to
        the time of a homework creation.
        """
        time_now = datetime.datetime.today()
        return time_now - self.created < self.deadline


class Student:
    """
    This is a simple model of a student.
    :param last_name: student`s last name
    :param first_name: student`s first name
    """
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        """
        Takes as an input a Homework class object and
        checks if it has timed out though is_active() method
        :param homework: takes Homework class obj
        :return: Homework obj, if it hasn`t timed out, else None
        """
        if homework.is_active():
            return homework
        print('You`re late')


class Teacher:
    """
    This is a simple model of a teacher.
    :param last_name: teacher`s last name
    :param first_name: teacher`s first name
    """
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(task_text: str, deadline: int) -> Homework:
        """Creates a Homework object.
        :param task_text: takes task
        :param deadline: takes int > 0, responsible for generating
        datetime.timedelta object`s days
        :return: Homework class object
        """
        return Homework(task_text, deadline)
