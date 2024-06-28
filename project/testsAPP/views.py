from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def attend(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}

    current_user = request.user

    return render(request, 'attend/home.html', context)

def attend_quiz(request):
    #quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'attendquiz.html')