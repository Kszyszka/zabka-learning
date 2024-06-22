from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def user_home(request):
    return render(request, 'users/home.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Logged in Fail')
    return render(request, 'users/signin.html')

def signup_user(request):
    return render(request, 'users/signup.html')

def join_quiz(request):
    return render(request, 'users/joinquiz.html')