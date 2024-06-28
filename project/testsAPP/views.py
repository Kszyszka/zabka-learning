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
            questions = request.POST
            for q in questions:
                logger.error(f'-----------{q}')
                logger.error(f'-------------{questions[q]}')
                #for d in q:
                    #logger.error(f'-------------{d}')                
                #logger.error(f'-----------{questions[question]}')
                #logger.error(f'-----------{questions[question]['test']}')

            pass        
        except Exception as e:
            logger.error(f'-----------Rzucam exception: {e}')
            return redirect('../../quiz/quizlist')

    return render(request, 'attend/results.html')