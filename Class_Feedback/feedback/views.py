from django.shortcuts import render
from .models import Course, Feedback

# Create your views here.

def browse(request):
    courses = Course.objects.order_by('-course_code').reverse

    context = {
        'courses' : courses,
        
    }

    return render(request, 'browse.html', context)

def search(request):
    
    #Get the text entered in the search form from the url parameter
    text = request.GET.get('text', '')

    courses = Course.objects.filter(course_code__contains=text) | Course.objects.filter(course_name__contains=text)

    context = {
        'text' : text,
        'courses' : courses
    }
    
    return render(request, 'search.html', context)

def viewCourse(request):
    code = request.GET.get('code', '')

    course = Course.objects.filter(course_code = code)

    feedbacks = Feedback.objects.filter(course=code)

    context = {
        'code' : code,
        'course' : course,
        'feedbacks' : feedbacks
    }

    print(course)

    return render(request, 'course.html', context)