import logging
import array
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm
from testsAPP.models import TestAttempt



# Create your views here.

#basepath = "..\\templates\\quiz\\"
logger = logging.getLogger('django')



def quizhome(request):    
    return render(request, 'quiz/home.html')

def create_quiz(request):    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quiz_title = data.get('quizName')
            questions = data.get('questions')
            quiz_desc = data.get('quizDescription')
            
            # Create the Quiz
            quiz = Quiz.objects.create(
                title=quiz_title,
                created_by=request.user,
                description=quiz_desc
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
            return redirect('quizlist')  # Redirect to home or another view upon error
    
    logger.info('------------------renderuje createquiz') 
    return render(request, 'quiz/login_createquiz.html')

def quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}

    current_user = request.user

    logger.info('------------------renderuje quizlist')
    return render(request, 'quiz/login_quizy.html', context)

#def quiz_listv2(request):
    #quizzes = Quiz.objects.all()
    #context = {'quizzes': quizzes}

    #quizzes = Quiz.objects.all()  # Replace Quiz with your actual Quiz model - to be added once
    #logger.info('------------------renderuje quizlist') 
    #return render(request, 'quiz/quizlist.html', context)

def question_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz/questionlist.html', {'quiz': quiz})

def test_list(request):
    quiz_list = Quiz.objects.all().filter(created_by = request.user)
    return render(request,"quiz/testlist.html",{'quizzes': quiz_list})

def test_list_guest(request):
    quiz_list = Quiz.objects.all()
    return render(request,"quiz/testlistguest.html",{'quizzes': quiz_list})

def stats(request):
    quiz_list = Quiz.objects.all().filter(created_by = request.user)
    #logger.error(f'--------------------attempt----{len(quiz_list)}\n')

    attempts = {}
    attemptcount = 0
    #x = TestAttempt.objects.all().filter(quiz = quiz_list[0])
    #logger.error(f'--------------------attempt----{len(x)}\n')

    query = TestAttempt.objects.all().filter(quiz__in = quiz_list)

    for quiz in quiz_list:
        attempts[quiz.id] = [att for att in query if att.quiz == quiz]
        logger.error(f'------------WAS ATTEMPTED? VAL OF ATT: {attempts[quiz.id]}')
       
        #if not query.exists():
           #attempts[quiz.id] = []
        #else:
            #attempts[quiz.id] = list(query)
          
    #logger.error(f'--------------------passed? = {attempts[61][0].taken_by}\n')
    logger.error(f'--------------------attempts total = {len(attempts)}\n')
        
    #logger.error(f'-----------------------------------------LIST OF ALL ATTEMPTS: {attempts}')

    return render(request, "quiz/quizstats.html",{'quizzes': quiz_list, 'tests' : attempts})