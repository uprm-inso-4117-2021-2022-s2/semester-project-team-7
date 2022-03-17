from django.shortcuts import render
from .models import Course, Feedback, Vote

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

    if(len(course) == 0):
        context = {
            'code' : code,
            'course' : course
        }

        return render(request, 'course.html', context)

    feedbacks = Feedback.objects.filter(course=code).order_by('date').reverse()

    user = request.user

    uservotes = Vote.objects.filter(user=user).filter(feedback__course=course[0]).values_list('feedback', flat=True)

    context = {
        'code' : code,
        'course' : course,
        'feedbacks' : feedbacks,
        'uservotes' : uservotes
    }

    return render(request, 'course.html', context)

def submitfeedback(request):
    user = request.user

    course = request.GET.get('course', '')

    print("Course: " + str(course))

    course = Course.objects.filter(course_code=course)

    #If course not found, ignore request 
    if(len(course) == 0):
        print("Course not found. Ignoring Feedback")
        return render(request, 'browse.html')

    text = request.POST.get('feedbacktext', '')

    anonymous = request.POST.get('anonymous', '')

    if(anonymous == 'true'):
        anonymous = "True"
    else:
        anonymous = "False"

    date = '2022-3-17'

    print("Submitting Feedback:")
    print("User: " + user.username)
    print("Text: " + text)
    print("Anonymous: " + anonymous)

    Feedback.objects.create(course=course[0], text=text, date=date, user=user, anonymous=anonymous, score=0)

    return render(request, 'browse.html')

def upvote(request):
    # Get the id that will get an upvote 
    id = request.GET.get('id', '')
    user = request.user

    # Get the feedback corresponding to the id provided
    feedback = Feedback.objects.filter(id=id)

    # If there's no feedback with this id, ignore the request
    if(len(feedback) == 0):
        print("Ignoring upvote request")
        return render(request, 'browse.html')

    feedback = feedback[0]

    # Try to find an upvote corresponding to the user and the feedback id provided 
    found = Vote.objects.filter(user = user) & Vote.objects.filter(feedback = feedback)

    # If not found, create it 
    # If there already is one, delete it 
    if(len(found) == 0):
        Vote.objects.create(feedback = feedback, user = user)
        print("Created new upvote: ")
        print("User: " + str(user))
        print("Feedback: " + str(Feedback))
    else:
        Vote.objects.filter(feedback = feedback, user = user).delete()
        print("Deleting upvote")
        print(feedback.id)

    # Update feedback score 

    votes = Vote.objects.filter(feedback__id = feedback.id)

    Feedback.objects.filter(id=feedback.id).update(score=len(votes))

    return render(request, 'browse.html')