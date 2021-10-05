from homework5.task1 import Homework, Student, Teacher


def test_homework_is_active():
    """Testing Homework`s is_active() method."""
    assert Homework('OOP task', 1).is_active()
    assert not Homework('OOP task', -1).is_active()


def test_student_do_homework():
    """Testing Student`s do_homework() method."""
    task1 = Homework('OOP task1', 5)
    assert Student('Some', 'Student').do_homework(task1) == task1

    task2 = Homework('OOP task2', 0)
    assert not Student('Another', 'Student').do_homework(task2)


def test_homework_student_teacher():
    """
    Checks if the connection between Homework,
    Student, Teacher classes works fine.
    """
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)

    assert isinstance(student.do_homework(oop_homework), Homework)
    assert student.do_homework(expired_homework) is None
