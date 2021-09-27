import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Error occurs when homework is overdue"""


class Homework:
    """
    Takes a homework task, deadline as an input,
    saves the date of creation.
    is_active method checks if a homework has timed out
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool or DeadlineError:
        """Checks if a homework has timed out"""
        time_now = datetime.datetime.today()
        if not time_now - self.created < self.deadline:
            raise DeadlineError
        return True


class EducationPerson:
    """
    Takes the first, the second name as an input.
    Superclass over Student, Teacher classes
    """
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(EducationPerson):
    """
    Takes a students first, second name.
    do_homework method takes a Homework object as an input,
    checks if it has timed out
    """
    @staticmethod
    def do_homework(homework: Homework, solution: str):
        """Takes as an input a Homework class object and
        checks if it has timed out"""
        try:
            homework.is_active()
            return HomeworkResult(Student, homework, solution)
        except DeadlineError:
            return 'You`re late'


class HomeworkResult:
    """
    Takes Student class object, Homework class objects,
    solution(str) as arguments.
    Checks if Homework arg belongs to Homework class.
    If not, raises ValueError
    """
    def __init__(self, author, homework, solution: str):
        if not isinstance(homework, Homework):
            raise ValueError('You gave not a Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.today()


class Teacher(EducationPerson):
    """
    Takes a teacher`s first, second name as an input.
    create_homework creates a Homework object,
    taking a task and a deadline as an input
    """
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(task_text: str, deadline: int) -> Homework:
        """
        Takes a task and a deadline as an input and
        creates a Homework object
        """
        return Homework(task_text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult) -> bool:
        """Takes HomeworkResult object as an argument,
        checks if it`s longer than 5 symbols, and in positive case
        adds Homework object as a key, solution as a value in
        homework_done dictionary"""
        hw_done = cls.homework_done
        hw_solution, hw_hw = hw_result.solution, hw_result.homework
        if len(hw_solution) > 5:
            hw_done[hw_hw].append(hw_solution)
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
