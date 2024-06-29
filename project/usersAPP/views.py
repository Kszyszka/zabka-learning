from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('quizlist')
        else:
            messages.error(request, 'Failed to log in')
    return render(request, 'users/log_full.html')

def signup_user(request):
    """Funkcja tworząca widok obsługujący formularz rejestracji."""
    if request.method == 'POST':
        if not User.objects.filter(username=request.POST["username"]).exists():
            if request.POST["password"] == request.POST["password2"]:
                user = User.objects.create_user(username=request.POST["username"],
                                                password=request.POST["password"],)
                user = authenticate(request, username=request.POST["username"],
                                    password=request.POST["password"])
                login(request, user)
                messages.success(request, 'Signed up successfully')
                return redirect('quizlist')
            else:
                messages.error(request, 'Sign up Failed, Passwords do not match')
        else:
            messages.error(request, 'Sign up Failed, User already exists')
    return render(request, 'users/reg_full.html')

def logout_user(request):
    logout(request)
    return redirect('mainpage')