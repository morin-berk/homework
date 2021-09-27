import pytest

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)


def test_homework_class():
    """Testing if Homework().is_active method
    raises DeadlineError Exception"""
    hw = Homework('something', 0)
    with pytest.raises(DeadlineError):
        hw.is_active()


def test_student_do_homework_negative():
    """Testing if Student().do_homework() raises an exception
    and returns the error message if homework has timed out"""
    student_hw = Student('Nobody', 'Nobody')
    hw = Homework('something', 0)
    assert student_hw.do_homework(hw, 'solution') == 'You`re late'


def test_student_do_homework_positive():
    """Testing if Student().do_homework() returns
    a class object if homework has not timed out"""
    student = Student('Nobody', 'Nobody')
    hw = Homework('something', 1)
    assert student.do_homework(hw, 'solution')


def test_homework_result_class():
    """Testing if HomeworkResult class raises ValueError when
    the second argument does not belong to Homework class"""
    student = Student('Nobody', 'Nobody')
    with pytest.raises(ValueError):
        HomeworkResult(student, 'hw', "solution")


def test_teacher_check_homework_len_solution():
    """Testing if Teacher.check_homework() returns False
    if the third argument, solution, is shorter than 5 symbols"""
    student = Student('Nobody', 'Nobody')
    hw = Homework('something', 1)
    hw_result = HomeworkResult(student,  hw, "not")
    assert not Teacher.check_homework(hw_result)


def test_teacher_check_homework_dictionary():
    """Testing if Teacher.check_homework() adds solution arguments
    from HomeworkResult class as values in homework_done dict, and
    links them with corresponding Homework arguments from HomeworkResult
    class as keys
    """
    student = Student('Nobody', 'Nobody')
    hw = Homework('something', 1)
    hw_result1 = HomeworkResult(student,  hw, "I've done some task")
    hw_result2 = HomeworkResult(student, hw, "The task is done")
    Teacher.check_homework(hw_result1)
    Teacher.check_homework(hw_result2)
    assert Teacher.homework_done[hw] == \
           ["I've done some task", "The task is done"]


def test_teacher_reset_results():
    """Testing if Teacher.reset_results() deletes corresponding
    Homework objects from homework_done dictionary"""
    student = Student('Nobody', 'Nobody')
    hw1 = Homework('something', 1)
    hw2 = Homework('another task', 2)
    hw_result1 = HomeworkResult(student,  hw1, "I've done some task")
    hw_result2 = HomeworkResult(student,  hw2, "The task is done")
    Teacher.check_homework(hw_result1)
    Teacher.check_homework(hw_result2)
    print(Teacher.homework_done)
    Teacher.reset_results(hw1)
    assert Teacher.homework_done[hw1] == []
    assert Teacher.homework_done[hw2] == ["The task is done"]
