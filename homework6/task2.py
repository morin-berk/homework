import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Error occurs when homework is overdue"""


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
        the time of a homework creation."""
        time_now = datetime.datetime.today()
        return time_now - self.created < self.deadline


class EducationPerson:
    """
    Superclass over Student, Teacher classes.
    :param last_name: person`s last name
    :param first_name: person`s first name
    """
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(EducationPerson):
    """This is a simple model of a student."""
    @staticmethod
    def do_homework(homework: Homework, solution: str):
        """Takes as an input a Homework class object and
        checks if it has timed out though is_active() method.
        :param homework: takes Homework class obj
        :param solution: text of a homework solution
        :return: Homework obj, if it hasn`t timed out, else None"""
        if homework.is_active():
            return HomeworkResult(Student, homework, solution)
        raise DeadlineError('You`re late')


class HomeworkResult:
    """
    This is a simple model of o homework result.
    :param author: takes a student
    :param homework: takes a homework, checks
    if Homework arg belongs to Homework class
    :param solution: text of a homework solution
    Also creates datetime.datetime.today() object, marking
    when Homework is created.
    """
    def __init__(self, author, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise ValueError('You gave not a Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.today()


class Teacher(EducationPerson):
    """
    This is a simple model of a teacher.
    Stores a defaultdict(list), which saves data from
    HomeworkResult: homework obj as a key,
    solution str as a value.
    """
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(task_text: str, deadline: int) -> Homework:
        """Creates a Homework object.
        :param task_text: takes task
        :param deadline: takes int > 0, responsible for generating
        datetime.timedelta object`s days
        :return: Homework class object
        """
        return Homework(task_text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult) -> bool:
        """Takes HomeworkResult object as an argument,
        checks if it`s longer than 5 symbols, and, in positive case,
        adds Homework object as a key, solution as a value in
        homework_done dictionary
        :param hw_result: HomeworkResult obj, containing Homework obj,
        solution str"""
        if len(hw_result.solution) > 5:
            cls.homework_done[hw_result.homework].append(hw_result.solution)
            return True
        return False

    @classmethod
    def reset_results(cls, result=None) -> None:
        """
        Takes one or no arguments.
        If it takes one argument, checks if it belongs to
        Homework class, if yes, then deletes corresponding
        key from homework_done dict.
        If there is no arguments, then it clears out the dict
        :param result: Homework result
        """
        if result is None:
            cls.homework_done.clear()
        elif isinstance(result, Homework):
            Teacher.homework_done.pop(result)


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
