from django.urls import path

from . import views

urlpatterns = [
    path('browse', views.browse),
    path('search', views.search),
    path('course', views.viewCourse)
]