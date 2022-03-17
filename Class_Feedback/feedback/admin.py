from django.contrib import admin

from .models import CourseIcon, Course, Feedback, Vote

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseIcon)
admin.site.register(Feedback)
admin.site.register(Vote)