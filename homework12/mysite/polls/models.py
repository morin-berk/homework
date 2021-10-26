from django.db import models
from django.utils import timezone


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    task = models.CharField(max_length=255)


class Homework(models.Model):
    task = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    deadline = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()


class HomeworkResults(models.Model):
    author = models.ForeignKey(Student,
                               related_name='student_author',
                               on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework,
                                 related_name='student_homework',
                                 on_delete=models.CASCADE)
    solution = models.ForeignKey(Student,
                                 related_name='student_solution',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
