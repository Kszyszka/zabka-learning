from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def attend_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'attend/attendquiz.html', {'quiz': quiz})

def results(request):
    return render(request, 'attend/results.html')