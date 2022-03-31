from django.shortcuts import render
from .models import Course, Feedback, Vote, User
import datetime

from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required(login_url='/login')
def browse(request):
    courses = Course.objects.order_by('-course_code').reverse

    context = {
        'courses' : courses,
    }

    return render(request, 'browse.html', context)

@login_required(login_url='/login')
def search(request):
    
    #Get the text entered in the search form from the url parameter
    text = request.GET.get('text', '')

    courses = Course.objects.filter(course_code__contains=text) | Course.objects.filter(course_name__contains=text)

    context = {
        'text' : text,
        'courses' : courses
    }
    
    return render(request, 'search.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
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

    date = datetime.date.today()

    print("Submitting Feedback:")
    print("User: " + user.username)
    print("Text: " + text)
    print("Anonymous: " + anonymous)

    Feedback.objects.create(course=course[0], text=text, date=date, user=user, anonymous=anonymous, score=0)

    return render(request, 'browse.html')

@login_required(login_url='/login')
def renderfeedback(request):
    
    user = request.user

    feedback = Feedback.objects.filter(user=user).order_by('-id')

    print(feedback[0])

    print(feedback[0].user)

    context = {
        'feedback' : feedback[0]
    }

    return render(request, 'renderfeedback.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def myFeedback(request):

    user = request.user

    feedbacks = Feedback.objects.filter(user=user).order_by('-id')

    context = {
        'feedbacks' : feedbacks
    }

    return render(request, 'myfeedback.html', context)

@login_required(login_url='/login')
def user(request):
    name = request.GET.get('name', '')
    
    user = User.objects.filter(username=name).first()

    feedbacks = Feedback.objects.filter(user=user).filter(anonymous=False).order_by('-id')

    context = {
        'name' : name,
        'feedbacks' : feedbacks
    }

    return render(request, 'user.html', context)

@login_required(login_url='/login')
def deletefeedback(request):
    # Get the id of the feedback that will get removed 
    id = request.GET.get('id', '')
    user = request.user

    # Get the feedback corresponding to the id provided
    feedback = Feedback.objects.filter(id=id)

    # If there's no feedback with this id, ignore the request
    if(len(feedback) == 0):
        print("Ignoring upvote request")
        return render(request, 'browse.html')

    feedback = feedback[0]

    # Also ignore it if the feedback submitter does not match the user requesting the deletion of it 
    # The only exception is admins which can delete any feedback 
    if(feedback.user != user and user.is_superuser == False):
        print("Ignoring upvote request")
        return render(request, 'browse.html')

    print(feedback.user)
    print(user)

    feedback.delete()

    return render(request, 'browse.html')

@login_required(login_url='/login')
def requestpermission(request):

    if(request.method == 'POST'):
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

    courses = Course.objects.all().order_by('-course_code').reverse()

    context = {
        'courses' : courses
    }

    return render(request, 'requestpermission.html', context)