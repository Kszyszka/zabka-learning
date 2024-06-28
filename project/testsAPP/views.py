import logging
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

logger = logging.getLogger('django')

def attend_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'attend/attendquiz.html', {'quiz': quiz})

def results(request):
    if request.method == 'POST':
        try:
            dbquestions = Question.objects.all()    #read from DB 
            questions = request.POST    #read from form (via POST)
            for q in questions:
                q_id = q[8::] # "question" is an 8 letter word - skip those 8 letters :)
                ans_given = questions[q]

                logger.error(f'-----------{q_id}')
                logger.error(f'-------------{questions[q]}')
     
        except Exception as e:
            logger.error(f'-----------Rzucam exception: {e}')
            return redirect('../../quiz/quizlist')

    return render(request, 'attend/results.html')