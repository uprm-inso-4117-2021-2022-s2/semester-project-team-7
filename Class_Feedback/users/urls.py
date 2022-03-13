from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registration),
    path('login', views.loginPage),
    path('logout', views.logoutUser)
]