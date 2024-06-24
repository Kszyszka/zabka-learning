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
        quiz_title = request.POST.get('quiz-name')
        questions = request.POST.getlist('questions')
        
        # Create the Quiz
        quiz = Quiz.objects.create(
            title=quiz_title,
            created_by=request.user
        )
        
        # Add Questions to Quiz
        for question_data in questions:
            question_text = question_data['question_text']
            answer1 = question_data['answer1']
            answer2 = question_data['answer2']
            answer3 = question_data['answer3']
            answer4 = question_data['answer4']
            correct_answer = question_data['correct_answer']

            Question.objects.create(
                quiz=quiz,
                question_text=question_text,
                answer1=answer1,
                answer2=answer2,
                answer3=answer3,
                answer4=answer4,
                correct_answer=correct_answer
            )
        
        return redirect('quizlist')  # Redirect to the quiz list view
    
    return render(request, 'quiz/login_createquiz.html')



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
    return render(request, 'quiz/login_quizy.html', {'quizzes': quizzes})  # Replace with your actual template for quiz list

def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/questionlist.html', {'quiz': quiz})
