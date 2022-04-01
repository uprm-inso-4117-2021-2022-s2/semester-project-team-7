from django.contrib import admin

from .models import CourseIcon, Course, Feedback, Permission, PermissionRequest, Vote

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseIcon)
admin.site.register(Feedback)
admin.site.register(Vote)
admin.site.register(Permission)
admin.site.register(PermissionRequest)