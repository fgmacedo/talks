from __future__ import unicode_literals
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Score(models.Model):
    points = models.IntegerField(max_length=4)
    course = models.ForeignKey('Course')
    student = models.ForeignKey('Student')

    def __str__(self):
        return "{s} has {p} points.".format(s=self.student, p=self.points)
