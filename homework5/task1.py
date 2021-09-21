import datetime


class Homework:
    """
    Takes a homework task, deadline as an input,
    saves a creation date.
    is_active method checks if a homework has timed out
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        """
        Checks if a homework has timed out
        """
        time_now = datetime.datetime.today()
        return time_now - self.created < self.deadline


class Student:
    """
    Takes a students first, second name.
    do_homework method takes a Homework object as an input,
    checks if it has timed out
    """
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Homework or None:
        """
        Takes as an input a Homework class object and
        checks if it has timed out
        """
        if homework.is_active():
            return homework
        print('You`re late')
        return None


class Teacher:
    """
    Takes a teacher`s first, second name as an input.
    create_homework creates a Homework object,
    taking a task and a deadline as an input
    """
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(task_text: str, deadline: int) -> Homework:
        """
        Takes a task and a deadline as an input and
        creates a Homework object
        """
        return Homework(task_text, deadline)
