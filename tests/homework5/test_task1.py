from homework5.task1 import Homework, Student, Teacher


def test_homework_student_teacher():
    """
    Checks if the connection between Homework,
    Student, Teacher classes works fine
    """
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')

    expired_homework = teacher.create_homework('Learn functions', 0)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)

    assert isinstance(student.do_homework(oop_homework), Homework)
    assert student.do_homework(expired_homework) is None
