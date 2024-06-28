from django.shortcuts import render

def attend(request):    
    return render(request, 'attend/home.html')