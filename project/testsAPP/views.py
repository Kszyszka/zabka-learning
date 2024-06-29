import logging
import re as regex
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from .models import *

logger = logging.getLogger('django')

def attend_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'test/attendquiz.html', {'quiz': quiz})

def results(request):
    if request.method == 'POST':
        try:
            questions = request.POST                  # read from form (via POST)
            given,correct = "",""                     # strings for answers to questions
            quiz = get_object_or_404(Quiz, id=request.POST['quizid'])

            #logger.error(f'-----------{questions}')
            curr_user = request.user
            taken_by_name = request.user.username
            #logger.error(f'-----------curruser - {curr_user}')


            
            if curr_user.is_anonymous:
                curr_user = None
                taken_by_name = request.POST['username']

            #logger.error(f'-----------curruser: {curr_user}')

            for q in questions:
                if regex.match(r'^question\d+$',q):         # łał nawet regexa wykorzystali ale ambitni studenci mysle ze zasłużyli na 5 :--D
                    logger.error(f'-----------{q}')
                    logger.error(f'-------------{questions[q]}')
                    
                    q_id = int(q[8::])                        # "question" is an 8 letter word - skip those 8 letters :)
                    q_db = Question.objects.get(id=q_id)
                    ans_given = questions[q]
                    ans_correct = q_db.correct_answer
                    
                    given += str(ans_given)
                    correct += str(ans_correct)  

            logger.error(f'-----------klucze: {given} {correct}')    

               
                    
            TestAttempt.objects.create(
                taken_by = curr_user,
                taken_by_name = taken_by_name,
                quiz = quiz, #NIE MAM POJECIA JAK TO SPRAWDZIC, BEDE MUSIAL CHYBA WZIAC TO POPRZEZ JEDNO Z PYTAŃ Z QUIZU
                correct_key = given,
                given_key = correct,
                score_percent = 200,   # dummy data,  will be replaced in constructor
                passed = False           # dummy data,  will be replaced in constructor
            )

        except Exception as e:
            logger.error(f'-----------Rzucam exception: {e}')
            return redirect('testlist')

    return render(request, 'test/results.html')

def attend_quiz_guest(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'test/attendquizguest.html', {'quiz': quiz})