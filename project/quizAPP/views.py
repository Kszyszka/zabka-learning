import logging
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm



# Create your views here.

#basepath = "..\\templates\\quiz\\"
logger = logging.getLogger('django')



def home(request):    
    return render(request, 'quiz/home.html')

def create_quiz(request):    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quiz_title = data.get('quizName')
            questions = data.get('questions')
            
            # Create the Quiz
            quiz = Quiz.objects.create(
                title=quiz_title,
                created_by=request.user
            )
            
            # Add Questions to Quiz
            for question_data in questions:
                question_text = question_data.get('question')
                answer1 = question_data.get('answers')[0]
                answer2 = question_data.get('answers')[1]
                answer3 = question_data.get('answers')[2]
                answer4 = question_data.get('answers')[3]
                correct_answer = int(question_data.get('correctAnswer'))

                Question.objects.create(
                    quiz=quiz,
                    question_text=question_text,
                    answer1=answer1,
                    answer2=answer2,
                    answer3=answer3,
                    answer4=answer4,
                    correct_answer=correct_answer
                )
                
            messages.success(request, 'Quiz został dodany do bazy danych.')
            return redirect('quizlist')  # Redirect to quiz list view after success
        
        except Exception as e:
            logger.error(f'-----------------------------------------EXCEPTION Error creating quiz: {str(e)}')
            messages.error(request, 'Wystąpił błąd podczas dodawania quizu.')
            return redirect('home')  # Redirect to home or another view upon error
    
    logger.info('------------------renderuje createquiz') 
    return render(request, 'quiz/login_createquiz.html')

def quiz_list(request):
    #quizzes = Quiz.objects.all()  # Replace Quiz with your actual Quiz model - to be added once
    logger.info('------------------renderuje quizlist') 
    return render(request, 'quiz/login_quizy.html')

def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/questionlist.html', {'quiz': quiz})
