from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models
from django.contrib.auth.models import User


class CourseIcon(models.Model):
    course_code = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=60)
    html = models.CharField(max_length=60)

    def __str__(self):
        return (self.course_code + " - " + self.name)

class Course(models.Model):
    course_code = models.CharField(primary_key = True, max_length=9)
    course_name = models.CharField(max_length=60)
    icon = models.ForeignKey(CourseIcon, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.course_code + " - " + self.course_name)

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.course) + " - " + "Feedback" + " - " + str(self.date))

class Vote(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("User " + str(self.user) + " - " + "ID " + str(self.feedback.id))