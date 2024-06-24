from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm


# Create your views here.

basepath = "..\\templates\\quiz\\"

def home(request):
    return render(request, f'{basepath}home.html')

def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.created_by = request.user  # Set the current user
            quiz.save()
            
            # Optionally, add a success message
            messages.success(request, 'Quiz created successfully!')
            
            # Store the quiz ID in the session
            request.session['current_quiz_id'] = quiz.id
            
            return redirect('quiz_list')  # Redirect to quiz list or any other page
    else:
        quiz_form = QuizForm()
    
    # Ensure the question form is empty when rendering the create_quiz form
    question_form = QuestionForm()
    quizzes = Quiz.objects.all()
    previous_questions = Question.objects.all()
    
    context = {
        'quiz_form': quiz_form,
        'question_form': question_form,
        'quizzes': quizzes,
        'previous_questions': previous_questions,
    }
    return render(request, f'{basepath}quizwizard.html', context)



def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return redirect('add_question')  # Adjust as necessary
    
    # Ensure the quiz form is empty when rendering the add_question form
    quiz_form = QuizForm()
    quizzes = Quiz.objects.all()
    previous_questions = Question.objects.all()
    
    context = {
        'quiz_form': quiz_form,
        'question_form': question_form,
        'quizzes': quizzes,
        'previous_questions': previous_questions,
    }
    return render(request, f'{basepath}quizwizard.html', context)


def quiz_list(request):
    quizzes = Quiz.objects.all()  # Replace Quiz with your actual Quiz model - to be added once 
    return render(request, 'quiz/quizlist.html', {'quizzes': quizzes})  # Replace with your actual template for quiz list

def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/questionlist.html', {'quiz': quiz})
