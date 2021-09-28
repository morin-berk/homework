import pytest

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)


class TestHomework:
    @staticmethod
    def test_homework_class():
        """Testing if Homework().is_active method
        raises DeadlineError Exception"""
        hw = Homework('something', 0)
        with pytest.raises(DeadlineError):
            hw.is_active()


class TestStudent:
    student = Student('Nobody', 'Nobody')

    @classmethod
    def test_student_do_homework_negative(cls):
        """Testing if Student().do_homework() raises an exception
        and returns the error message if homework has timed out"""
        hw = Homework('something', 0)
        assert cls.student.do_homework(hw, 'solution') == 'You`re late'

    @classmethod
    def test_student_do_homework_positive(cls):
        """Testing if Student().do_homework() returns
        a class object if homework has not timed out"""
        hw = Homework('something', 1)
        assert cls.student.do_homework(hw, 'solution')

    @classmethod
    def test_homework_result_class(cls):
        """Testing if HomeworkResult class raises ValueError when
        the second argument does not belong to Homework class"""
        with pytest.raises(ValueError):
            HomeworkResult(cls.student, 'hw', "solution")


class TestTeacher:
    student = Student('Nobody', 'Nobody')
    hw = Homework('something', 1)

    @classmethod
    def test_teacher_check_homework_len_solution(cls):
        """Testing if Teacher.check_homework() returns False
        if the third argument, solution, is shorter than 5 symbols"""
        hw_result = HomeworkResult(cls.student,  cls.hw, "not")
        assert not Teacher.check_homework(hw_result)

    @classmethod
    def test_teacher_check_homework_dictionary(cls):
        """Testing if Teacher.check_homework() adds solution arguments
        from HomeworkResult class as values in homework_done dict, and
        links them with corresponding Homework arguments from HomeworkResult
        class as keys
        """
        hw_result1 = HomeworkResult(cls.student,
                                    cls.hw, "I've done some task")
        hw_result2 = HomeworkResult(cls.student,
                                    cls.hw, "The task is done")
        Teacher.check_homework(hw_result1)
        Teacher.check_homework(hw_result2)
        assert Teacher.homework_done[cls.hw] == \
               ["I've done some task", "The task is done"]

    @classmethod
    def test_teacher_reset_results(cls):
        """
        Testing if Teacher.reset_results() deletes corresponding
        Homework objects from homework_done dictionary
        """
        hw2 = Homework('another task', 2)
        hw_result1 = HomeworkResult(cls.student,
                                    cls.hw, "I've done some task")
        hw_result2 = HomeworkResult(cls.student,
                                    hw2, "The task is done")
        Teacher.check_homework(hw_result1)
        Teacher.check_homework(hw_result2)
        print(Teacher.homework_done)
        Teacher.reset_results(cls.hw)
        assert Teacher.homework_done[cls.hw] == []
        assert Teacher.homework_done[hw2] == ["The task is done"]
