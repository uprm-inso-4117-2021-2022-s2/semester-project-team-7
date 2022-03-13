from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None: 
                login(request, user)
                return redirect('/')
        
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')

        return render(request, 'registration.html', {
            'form':form
        })